from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys


class GameTableModel(QAbstractTableModel):
    """A model to store a list of things"""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.items = [
            {"name": "Tomb Raider", "rating": 4},
            {"name": "Super Mario", "rating": 1},
            {"name": "Civilization", "rating": 3},
            {"name": "caramagedon", "rating": 2},
            {"name": "Age of empire", "rating": 4},
            {"name": "Civilization 3", "rating": 2},
            {"name": "Metal gear solid", "rating": 5},
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
                return "rating"

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
                return item["rating"]

        if role == Qt.DecorationRole and index.column() == 0:
            return qApp.style().standardIcon(QStyle.SP_DirIcon)


class GameDelegate(QStyledItemDelegate):
    """docstring for ClassName"""

    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(
        self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex
    ):

        if index.column() == 1:
            #  Draw star
            painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
            rating = int(index.data())
            start_pos = QPoint(option.rect.left() + 10, option.rect.center().y())
            for i in range(5):

                color = "black" if rating > i else "white"

                painter.setBrush(QColor(color))
                painter.drawEllipse(start_pos, 5, 5)
                start_pos += QPoint(20, 0)

        else:
            return super().paint(painter, option, index)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    view = QTableView()
    model = GameTableModel()
    delegate = GameDelegate()
    view.setModel(model)
    view.setItemDelegate(delegate)
    view.horizontalHeader().setStretchLastSection(True)
    view.setAlternatingRowColors(True)
    view.setSelectionBehavior(QAbstractItemView.SelectRows)
    view.show()

    app.exec_()
