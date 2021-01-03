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

    def clear(self):
        self.beginResetModel()
        self.items.clear()
        self.endResetModel()

    def add_item(self, name: str, description: str):
        self.beginInsertRows(QModelIndex(), 0, 0)
        self.items.append({"name": name, "description": description})
        self.endInsertRows()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()
    l = QVBoxLayout()
    add_button = QPushButton("Add")
    clear_button = QPushButton("Clear")

    view = QListView()
    view.setIconSize(QSize(20, 20))
    model = GameListModel()
    view.setModel(model)

    add_button.clicked.connect(lambda: model.add_item("test", "a description"))
    clear_button.clicked.connect(model.clear)

    l.addWidget(view)
    l.addWidget(add_button)
    l.addWidget(clear_button)

    w.setLayout(l)

    w.show()

    app.exec_()
