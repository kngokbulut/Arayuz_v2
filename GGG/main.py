from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)







class Dialog(QDialog):


    def __init__(self):
        super(Dialog, self).__init__()

        self.createGridGroupBox()
        self.createGridGroupBox2()
        self.createGridGroupBox3()



        mainLayout = QVBoxLayout()

        mainLayout.addWidget(self.gridGroupBox)
        mainLayout.addWidget(self.gridGroupBox2)
        mainLayout.addWidget(self.gridGroupBox3)



        self.setLayout(mainLayout)
        self.setWindowTitle("Proje Yükleme Arayüzü")
        self.resize(480, 320)


    def createGridGroupBox(self):
        self.gridGroupBox = QGroupBox("İçerik Bölümü")

        layout = QGridLayout()
        label = QLabel("DEVİCE NAME:")
        lineEdit = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(lineEdit)

        label= QLabel("IP ADD:")
        lineEdit = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(lineEdit)

        label = QLabel("SUBMASK:")
        lineEdit = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(lineEdit)

        label = QLabel("GATEWAY:")
        lineEdit = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(lineEdit)

        self.gridGroupBox.setLayout(layout)


    def createGridGroupBox2(self):
        self.gridGroupBox2 = QGroupBox("Proje Seçim Bölümü")

        layout2 = QGridLayout()

        popupButton = QPushButton("PROJELER")
        menu = QMenu(self)
        menu.addAction("1. PROJE ")
        menu.addAction("2. PROJE ")
        menu.addAction("3. PROJE")
        menu.addAction("4. PROJE")
        popupButton.setMenu(menu)

        layout2.addWidget(popupButton)


        label2= QLabel("SİDE :")
        lineEdit2 = QLineEdit()

        layout2.addWidget(label2)
        layout2.addWidget(lineEdit2)

        label3 = QLabel("VERSİYON :")
        lineEdit3 = QLineEdit()

        layout2.addWidget(label3)
        layout2.addWidget(lineEdit3)




        popupButton = QPushButton("PROJELER")
        menu = QMenu(self)
        menu.addAction("1. PROJE ")
        menu.addAction("2. PROJE ")
        menu.addAction("3. PROJE")
        menu.addAction("4. PROJE")
        popupButton.setMenu(menu)




        self.gridGroupBox2.setLayout(layout2)


    def createGridGroupBox3(self):
        self.gridGroupBox3 = QGroupBox("Gönderme Bölümü")
        layout3 = QGridLayout()

        self.label4 = QLabel("Gönderme Emri Bekleniyor")
        layout3.addWidget(self.label4)

        b1 = QPushButton(self)
        b1.setText("GÖNDER")
        b1.clicked.connect(self.button_clicked)

        layout3.addWidget(b1)

        self.gridGroupBox3.setLayout(layout3)


    def button_clicked(self):
        self.label4.setText("Gönderildi")

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
