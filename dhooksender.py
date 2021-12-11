from PyQt5 import QtCore, QtGui, QtWidgets
from dhooks import Webhook, File

webhook_url = Webhook('WEBHOOK TOKEN')

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 330)
        self.sendButton = QtWidgets.QPushButton(Dialog)
        self.sendButton.setGeometry(QtCore.QRect(150, 220, 91, 31))
        self.sendButton.setObjectName("sendButton")
        self.sendButton.clicked.connect(self.send_button_clicked)
        self.textBox = QtWidgets.QTextEdit(Dialog)
        self.textBox.setGeometry(QtCore.QRect(100, 70, 191, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.textBox.setFont(font)
        self.textBox.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBox.setObjectName("textBox")
        self.mainLabel = QtWidgets.QLabel(Dialog)
        self.mainLabel.setGeometry(QtCore.QRect(80, 10, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(12)
        self.mainLabel.setFont(font)
        self.mainLabel.setObjectName("mainLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

#   SENDING DISCORD WEBHOOK
    def send_button_clicked(self):

        dhook_message = str(self.textBox.toPlainText())
        try:
            webhook_url.send(dhook_message)
        except ValueError:
            print("Oops! This string was empty. Write something...")


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Discord Webhook Sender"))
        self.sendButton.setText(_translate("Dialog", "SEND"))
        self.mainLabel.setText(_translate("Dialog", "Dhook Sender - Send A Message!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
