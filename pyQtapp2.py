import sys;
import numpy as np;
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QPushButton, QLineEdit, QMessageBox;

class Application(QWidget):

    def __init__(self):
        super().__init__();
        self.initUI();
    
    def initUI(self):
        self.setWindowTitle("PyQt Example");
        self.resize(400,300);

        self.labelName = QLabel(self);
        self.labelName.setText("Please Enter Your Name: ")
        self.labelName.move(20,10);

        self.txtName = QLineEdit(self);
        self.txtName.setText("");
        self.txtName.move(20,30);
        self.txtName.resize(200,20);

        self.btnShowName = QPushButton("Show Name", self);
        self.btnShowName.move(15,60);
        self.btnShowName.clicked.connect(self.btnShowName_clicked);

        self.show();
    
    def btnShowName_clicked(self):
        self.showMessage();
    
    def showMessage(self):
        name = self.txtName.text();
        text = "Is it your Name: "+ name + "?";
        reply = QMessageBox.question(self, "Message", text, QMessageBox.Yes | QMessageBox.No , QMessageBox.No);
        if reply == QMessageBox.No:
            self.txtName.setText("");
        else:
            self.correctName();
    
    def correctName(self):
        self.messageBox = QMessageBox();
        self.messageBox.setText("Thank You ...");
        self.messageBox.exec_(sys.exit());


if __name__ == '__main__':
    app = QApplication(sys.argv);
    app.setStyle('Fusion');
    window = Application();
    sys.exit(app.exec_());