
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.figure import Figure

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setWindowTitle("Simple plot GUI")
        self.resize(900, 700)

        self.centralwidget = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)

        # 'Point 1' groupBox
        #
        #
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("Membuat garis dari titik nol")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)

        # 'x coordinate' Point1 spinBox
        self.spinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spinBox.valueChanged.connect(self.passInfo)
        self.spinBox.setMaximum(10)
        self.gridLayout_2.addWidget(self.spinBox, 0, 1)

        # 'x coordinate' Point1 slider (connected to spinBox)
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.valueChanged.connect(self.slider2spin)
        self.slider.setMaximum(100)
        self.gridLayout_2.addWidget(self.slider, 1, 1)

        # 'y coordinate' Point1 spinBox
        self.spinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spinBox_2.valueChanged.connect(self.passInfo)
        self.spinBox_2.setMaximum(10)
        self.gridLayout_2.addWidget(self.spinBox_2, 2, 1, 1, 1)

        # 'y coordinate' Point1 slider (connected to spinBox_2)
        self.slider_2 = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_2.valueChanged.connect(self.slider2spin)
        self.slider_2.setMaximum(100)
        self.gridLayout_2.addWidget(self.slider_2, 3, 1)

        # 'y coordinate' label
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setText("kordinat sumbu y")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        # 'x coordinate' label
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setText("kordinat sumbu x")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        # Adding groupBoxes
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        # MatPlotLib

        self.m = PlotCanvas()
        self.gridLayout.addWidget(self.m, 1, 0, 1, 2)

        # 'Erase' pushButton
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setText("Clear")
        self.pushButton.clicked.connect(self.erase)
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 2)

        # Fonts
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPixelSize(15)
        self.setFont(font)

        # Central Widget
        self.setCentralWidget(self.centralwidget)

    def passInfo(self):
        self.m.x1 = self.spinBox.value()
        self.m.y1 = self.spinBox_2.value()
        self.m.x2 = 0
        self.m.y2 = 0

        self.m.plot()

        self.spin2slider()

    def erase(self):
        self.slider.setValue(0)
        self.slider_2.setValue(0)
        self.slider2spin()
        self.passInfo()

    def slider2spin(self):
        self.spinBox.setValue(self.slider.value()/10)
        self.spinBox_2.setValue(self.slider_2.value()/10)

    def spin2slider(self):
        self.slider.setValue(self.spinBox.value()*10)
        self.slider_2.setValue(self.spinBox_2.value()*10)


class PlotCanvas(FigureCanvas):

    def __init__(self):

        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0

        fig = Figure()

        FigureCanvas.__init__(self, fig)

        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        FigureCanvas.updateGeometry(self)

        self.plot()


    def plot(self):

        rgb1 = (self.rgb(53), self.rgb(53), self.rgb(53))
        rgb2 = (self.rgb(200), self.rgb(200), self.rgb(200))
        rgb3 = (self.rgb(240), self.rgb(240), self.rgb(240))


        ax = self.figure.add_subplot()
        ax.cla()

        if self.x1 != 0 or self.x2 != 0 or self.y1 != 0 or self.y2 != 0:
            ax.plot([self.x1, self.x2], [self.y1, self.y2], color=rgb2)

            ax.plot([self.x1, self.x2], [self.y1, self.y2], 'ro', color=rgb3)

        ax.set_facecolor(rgb1)

        self.figure.set_facecolor(rgb1)

        ax.axis([0, 10, 0, 10])

        ax.tick_params(color=rgb2, labelcolor=rgb2)
        for spine in ax.spines.values():
            spine.set_edgecolor(rgb2)

        self.draw()

    def rgb(self, value):
        return value/255


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = Main()
    app.setStyle('Fusion')

    # Dark Mode
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(40, 40, 40))
    palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(200, 200, 200))

    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(45, 45, 45))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtGui.QColor(200, 200, 200))
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(200, 200, 200))
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)

    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(37, 110, 217))
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)

    GUI.show()
    sys.exit(app.exec_())
