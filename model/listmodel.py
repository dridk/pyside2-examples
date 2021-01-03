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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QListView()
    w.setIconSize(QSize(20, 20))
    m = GameListModel()
    w.setModel(m)

    w.show()

    app.exec_()
