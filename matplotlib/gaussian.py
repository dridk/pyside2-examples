from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys

import numpy as np
from scipy.stats import norm


from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT


class PlotWidget(QWidget):
    """docstring for ClassName"""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.view = FigureCanvas(Figure(figsize=(5, 3)))
        self.axes = self.view.figure.subplots()
        self.toolbar = NavigationToolbar2QT(self.view, self)
        self.mu_input = QDoubleSpinBox()
        self.std_input = QDoubleSpinBox()

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.mu_input)
        input_layout.addWidget(self.std_input)

        self.button = QPushButton("valider")
        vlayout = QVBoxLayout()

        self.mu_input.setPrefix("μ: ")
        self.std_input.setPrefix("σ: ")
        self.std_input.setValue(10)

        vlayout.addWidget(self.toolbar)
        vlayout.addWidget(self.view)
        vlayout.addLayout(input_layout)
        vlayout.addWidget(self.button)
        self.setLayout(vlayout)

        self.button.clicked.connect(self.on_valid)

        self.on_valid()

    def on_valid(self):
        mu = self.mu_input.value()
        std = self.std_input.value()

        x = np.linspace(-100, 100)
        y = norm.pdf(x, mu, std)

        self.axes.clear()
        self.axes.plot(x, y)
        self.view.draw()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = PlotWidget()
    w.show()
    app.exec_()
