from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys


class GameListModel(QAbstractListModel):
    """A model to store a list of things"""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.items = [
            {"name": "Tomb Raider", "description": "Action game"},
            {"name": "Super Mario", "description": "Aracade game"},
            {"name": "Civilization", "description": "Strategie game"},
            {"name": "caramagedon", "description": "car racer"},
            {"name": "Age of empire", "description": "Strategie game"},
            {"name": "Civilization 3", "description": "Strategie game"},
            {"name": "Metal gear solid", "description": "action game"},
        ]

    def rowCount(self, parent=QModelIndex()):
        """ override : return row count """
        return len(self.items)

    def data(self, index: QModelIndex(), role: Qt.ItemDataRole):
        """ override : Display data according index and role """

        # Return none, in index is not valid
        if not index.isValid():
            return None

        item = self.items[index.row()]

        if role == Qt.DisplayRole:
            return item["name"]

        if role == Qt.ToolTipRole:
            return item["description"]

        if role == Qt.DecorationRole:
            return qApp.style().standardIcon(QStyle.SP_DirIcon)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QWidget()
    search_edit = QLineEdit()
    view = QListView()
    layout = QVBoxLayout()
    layout.addWidget(search_edit)
    layout.addWidget(view)
    widget.setLayout(layout)

    model = GameListModel()
    proxy_model = QSortFilterProxyModel()
    proxy_model.setSourceModel(model)
    view.setModel(proxy_model)

    search_edit.textChanged.connect(proxy_model.setFilterRegExp)

    widget.show()

    app.exec_()
