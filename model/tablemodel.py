from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys


class GameTableModel(QAbstractTableModel):
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

    def columnCount(self, parent=QModelIndex()):
        """ override : return column count """
        return 2

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole
    ):
        """ override : display header data according section and orientation """

        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if section == 0:
                return "name"
            if section == 1:
                return "description"

        return None

    def data(self, index: QModelIndex(), role: Qt.ItemDataRole):
        """ override : Display data according index and role """

        # Return none, in index is not valid
        if not index.isValid():
            return None

        item = self.items[index.row()]

        if role == Qt.DisplayRole:
            if index.column() == 0:
                return item["name"]

            if index.column() == 1:
                return item["description"]

        if role == Qt.DecorationRole and index.column() == 0:
            return qApp.style().standardIcon(QStyle.SP_DirIcon)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    view = QTableView()
    model = GameTableModel()
    view.setModel(model)
    view.horizontalHeader().setStretchLastSection(True)
    view.setAlternatingRowColors(True)
    view.setSelectionBehavior(QAbstractItemView.SelectRows)
    view.show()

    app.exec_()
