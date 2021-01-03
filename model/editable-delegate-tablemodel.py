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
            {"name": "caramagedon", "description": "Car racer"},
            {"name": "Age of empire", "description": "Strategie game"},
            {"name": "Civilization 3", "description": "Strategie game"},
            {"name": "Metal gear solid", "description": "Action game"},
        ]

        self.game_type = ["Action game", "Strategie game", "Car racer"]

    def rowCount(self, parent=QModelIndex()):
        """ override : return row count """
        return len(self.items)

    def columnCount(self, parent=QModelIndex()):
        """ override : return column count """
        return 2

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        """ override : make column 1 editable """
        if index.column() == 1:
            return Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled
        else:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled

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

        if role == Qt.DisplayRole or role == Qt.EditRole:
            if index.column() == 0:
                return item["name"]

            if index.column() == 1:
                return item["description"]

        if role == Qt.DecorationRole and index.column() == 0:
            return qApp.style().standardIcon(QStyle.SP_DirIcon)

    def setData(self, index: QModelIndex(), value, role=Qt.EditRole):
        """ override : set data value according index """
        if index.column() == 1:
            self.items[index.row()]["description"] = value
            return True

        return False


class GameDelegate(QStyledItemDelegate):
    """docstring for ClassName"""

    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(
        self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex
    ):
        """ Override : Create a widget when cell is edit """
        if index.column() == 1:
            combo = QComboBox()
            combo.addItems(index.model().game_type)
            combo.setParent(parent)
            return combo

    def setEditorData(self, editor: QWidget, index: QModelIndex):
        """ override : model --> widget : Set widget data from model """
        if index.column() == 1:
            editor.setCurrentText(index.data())
        else:
            super().setEditorData(editor, index)

    def setModelData(self, editor: QWidget, model: GameTableModel, index: QModelIndex):
        """ override : widget ---> model : set model data from widget """
        if index.column() == 1:
            model.setData(index, editor.currentText())
        else:
            super().setModelData(editor, model, index)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    view = QTableView()
    model = GameTableModel()
    delegate = GameDelegate()
    view.setModel(model)
    view.setItemDelegate(delegate)
    view.setEditTriggers(QAbstractItemView.AllEditTriggers)
    view.horizontalHeader().setStretchLastSection(True)
    view.setAlternatingRowColors(True)
    view.setSelectionBehavior(QAbstractItemView.SelectRows)
    view.show()

    app.exec_()
