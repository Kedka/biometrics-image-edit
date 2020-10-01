from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from image_reader import Image

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.resize(500, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # Load file button and edit field
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        # Save file button and edit field
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 10, 75, 23))

        # Upscale and downscale image buttons
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.pushButton_downscale = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_downscale.setGeometry(QtCore.QRect(100, 40, 75, 23))

        # Scale input field
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 71, 113, 20))

        # Pixel value: x, y, red, green, blue
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 100, 101, 16))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 47, 13))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 47, 13))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 47, 13))
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 150, 55, 13))
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 150, 47, 13))

        # Edit pixel: red, green, blue input fields and labels
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 180, 61, 16))
        self.label_red = QtWidgets.QLabel(self.centralwidget)
        self.label_red.setGeometry(QtCore.QRect(10, 200, 61, 16))
        self.label_green = QtWidgets.QLabel(self.centralwidget)
        self.label_green.setGeometry(QtCore.QRect(10, 230, 61, 16))
        self.label_blue = QtWidgets.QLabel(self.centralwidget)
        self.label_blue.setGeometry(QtCore.QRect(10, 260, 61, 16))
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 200, 113, 20))
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 230, 113, 20))
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(60, 260, 113, 20))

        # Histograms
        self.pushButton_hist = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_hist.setGeometry(QtCore.QRect(267, 10, 110, 23))
        self.pushButton_lUp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_lUp.setGeometry(QtCore.QRect(245, 40, 75, 23))
        self.pushButton_lDown = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_lDown.setGeometry(QtCore.QRect(325, 40, 75, 23))
        self.pushButton_histStretch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_histStretch.setGeometry(QtCore.QRect(285, 80, 75, 23))
        self.pushButton_histEq = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_histEq.setGeometry(QtCore.QRect(285, 150, 75, 23))
        self.lineEdit_stretchA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_stretchA.setGeometry(QtCore.QRect(245, 110, 75, 23))
        self.lineEdit_stretchB = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_stretchB.setGeometry(QtCore.QRect(325, 110, 75, 23))

        #Binarization
        self.pushButton_manual_bin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_manual_bin.setGeometry(QtCore.QRect(245, 200, 110, 23))
        self.pushButton_auto_bin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_auto_bin.setGeometry(QtCore.QRect(245, 240, 110, 23))
        self.pushButton_local_bin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_local_bin.setGeometry(QtCore.QRect(245, 280, 110, 23))
        self.lineEdit_threshold = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_threshold.setGeometry(QtCore.QRect(360, 200, 75, 23))
        self.lineEdit_window = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_window.setGeometry(QtCore.QRect(245, 310, 75, 23))
        self.lineEdit_k = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_k.setGeometry(QtCore.QRect(325, 310, 75, 23))

        #Filters
        self.pushButton_blur = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_blur.setGeometry(QtCore.QRect(90,300,75,23))
        self.pushButton_prewitt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_prewitt.setGeometry(QtCore.QRect(10,340,75,23))
        self.pushButton_sobel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sobel.setGeometry(QtCore.QRect(90,340,75,23))
        self.pushButton_laplace = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_laplace.setGeometry(QtCore.QRect(10,380,75,23))
        self.pushButton_corners = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_corners.setGeometry(QtCore.QRect(90,380,75,23))
        self.pushButton_kuwahara = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_kuwahara.setGeometry(QtCore.QRect(300,350,75,23))
        self.pushButton_median3x3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_median3x3.setGeometry(QtCore.QRect(260,380,75,23))
        self.pushButton_median5x5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_median5x5.setGeometry(QtCore.QRect(340,380,75,23))
        self.lineEdit_window2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_window2.setGeometry(QtCore.QRect(10, 300, 75, 23))
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons to methods
        self.pushButton.clicked.connect(self.load_image)
        self.pushButton_2.clicked.connect(self.upscale_image)
        self.pushButton_downscale.clicked.connect(self.downscale_image)
        self.pushButton_3.clicked.connect(self.save)
        self.pushButton_hist.clicked.connect(self.show_histogram)
        self.pushButton_histEq.clicked.connect(self.show_equalized)
        self.pushButton_histStretch.clicked.connect(self.show_stretched)
        self.pushButton_lUp.clicked.connect(self.change_brightnessUp)
        self.pushButton_lDown.clicked.connect(self.change_brightnessDown)
        self.pushButton_manual_bin.clicked.connect(self.manual_bin)
        self.pushButton_auto_bin.clicked.connect(self.auto_bin)
        self.pushButton_local_bin.clicked.connect(self.local_bin)
        self.pushButton_blur.clicked.connect(self.blur)
        self.pushButton_prewitt.clicked.connect(self.prewitt)
        self.pushButton_sobel.clicked.connect(self.sobel)
        self.pushButton_laplace.clicked.connect(self.laplace)
        self.pushButton_corners.clicked.connect(self.corners)
        self.pushButton_kuwahara.clicked.connect(self.kuwahara)
        self.pushButton_median3x3.clicked.connect(self.median3x3)
        self.pushButton_median5x5.clicked.connect(self.median5x5)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.pushButton.setText(_translate("MainWindow", "Load image"))
        self.pushButton_3.setText(_translate("MainWindow", "Save"))

        self.pushButton_2.setText(_translate("MainWindow", "Upscale"))
        self.pushButton_downscale.setText(_translate("MainWindow", "Downscale"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Input for scale"))
        
        self.label.setText(_translate("MainWindow", "Pixel value:"))
        self.label_2.setText(_translate("MainWindow", "x:"))
        self.label_3.setText(_translate("MainWindow", "y: "))
        self.label_4.setText(_translate("MainWindow", "Red: "))
        self.label_5.setText(_translate("MainWindow", "Green: "))
        self.label_6.setText(_translate("MainWindow", "Blue: "))

        self.label_7.setText(_translate("MainWindow", "Edit pixel:"))
        self.lineEdit_2.setText(_translate("MainWindow", '0'))
        self.lineEdit_3.setText(_translate("MainWindow", '0'))
        self.lineEdit_4.setText(_translate("MainWindow", '0'))
        self.label_red.setText(_translate("MainWindow", "Red: "))
        self.label_green.setText(_translate("MainWindow", "Green: "))
        self.label_blue.setText(_translate("MainWindow", "Blue: "))

        self.pushButton_hist.setText(_translate("MainWindow", "Show histograms"))
        self.pushButton_lUp.setText(_translate("MainWindow", "Lighten"))
        self.pushButton_lDown.setText(_translate("MainWindow", "Darken"))
        self.pushButton_histStretch.setText(_translate("MainWindow", "Stretch"))
        self.pushButton_histEq.setText(_translate("MainWindow", "Equalize"))
        self.lineEdit_stretchA.setPlaceholderText(_translate("MainWindow", "a"))
        self.lineEdit_stretchB.setPlaceholderText(_translate("MainWindow", "b"))

        self.pushButton_manual_bin.setText(_translate("MainWindow", "Manual binarization"))
        self.pushButton_auto_bin.setText(_translate("MainWindow", "Auto binarization"))
        self.pushButton_local_bin.setText(_translate("MainWindow", "Local binarization"))
        self.lineEdit_threshold.setPlaceholderText(_translate("MainWindow", "threshold"))
        self.lineEdit_window.setPlaceholderText(_translate("MainWindow", "window"))
        self.lineEdit_k.setPlaceholderText(_translate("MainWindow", "k"))

        self.pushButton_blur.setText(_translate("MainWindow", "Blur"))
        self.pushButton_prewitt.setText(_translate("MainWindow", "Prewitt"))
        self.pushButton_sobel.setText(_translate("MainWindow", "Sobel"))
        self.pushButton_laplace.setText(_translate("MainWindow", "Laplace"))
        self.pushButton_corners.setText(_translate("MainWindow", "Corners"))
        self.pushButton_kuwahara.setText(_translate("MainWindow", "Kuwahara"))
        self.pushButton_median3x3.setText(_translate("MainWindow", "Median 3x3"))
        self.pushButton_median5x5.setText(_translate("MainWindow", "Median 5x5"))
        self.lineEdit_window2.setPlaceholderText(_translate("MainWindow", "3 -> 3x3"))



    def load_image(self):
        fileName, _ = QFileDialog.getOpenFileName()
        self.img = Image(fileName)
        self.img.show_image()
        self.img.set_callback()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_label)
        self.timer.start(0)

    def upscale_image(self):
        d = int(self.lineEdit.text())
        self.img.upscale(d)

    def downscale_image(self):
        d = int(self.lineEdit.text())
        self.img.downscale(d)

    def update_label(self):
        self.label_2.setText("x: " + str(self.img.x))
        self.label_3.setText("y: " + str(self.img.y))
        self.label_4.setText("Red: " + str(self.img.colorR))
        self.label_5.setText("Green: " + str(self.img.colorG))
        self.label_6.setText("Blue: " + str(self.img.colorB))

        red = self.lineEdit_2.text()
        green = self.lineEdit_3.text()
        blue = self.lineEdit_4.text()

        if red > '0':
            red = int(self.lineEdit_2.text())
            self.img.editR = red
        else:
            self.img.editR = 0

        if green > '0':
            green = int(self.lineEdit_3.text())
            self.img.editG = green
        else:
            self.img.editG = 0

        if blue > '0':
            blue = int(self.lineEdit_4.text())
            self.img.editB = blue
        else:
            self.img.editB = 0

    def save(self):
        fileName, _ = QFileDialog.getSaveFileName()
        self.img.save(fileName)

    def show_histogram(self):
        self.img.histogram()

    def show_equalized(self):
        self.img.equalize()

    def show_stretched(self):
        a = float(self.lineEdit_stretchA.text())
        b = float(self.lineEdit_stretchB.text())
        self.img.stretch(a, b)

    def change_brightnessUp(self):
        self.img.brightness(1)
    def change_brightnessDown(self):
        self.img.brightness(0)

    def manual_bin(self):
        threshold = float(self.lineEdit_threshold.text())
        self.img.manual_bin(threshold)

    def auto_bin(self):
        self.img.auto_bin()

    def local_bin(self):
        window = int(self.lineEdit_window.text())
        k = float(self.lineEdit_k.text())
        self.img.local_bin(window, k)

    def blur(self):
        window = int(self.lineEdit_window2.text())
        self.img.blur(window)

    def prewitt(self):
        window = int(self.lineEdit_window2.text())
        self.img.prewitt(window)

    def sobel(self):
        window = int(self.lineEdit_window2.text())
        self.img.sobel(window)

    def laplace(self):
        window = int(self.lineEdit_window2.text())
        self.img.laplace(window)
    
    def corners(self):
        window = int(self.lineEdit_window2.text())
        self.img.corners(window)

    def kuwahara(self):
        self.img.kuwahara()

    def median3x3(self):
        self.img.median(3)

    def median5x5(self):
        self.img.median(5)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
