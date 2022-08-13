import sys;
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox;

def button_clicked():
    messageBox = QMessageBox();
    messageBox.setText("You clicked the Button.");
    messageBox.exec_();

if __name__ == "__main__":
    # application = QApplication(sys.argv);
    application = QApplication([]);
    application.setStyle("Fusion");
    window = QWidget();
    window.resize(300,200);
    window.setWindowTitle("Hello World");

    label = QLabel(window);
    label.setText("This is Label");
    label.move(100,50);

    inputbox = QLineEdit(window);
    inputbox.setText("Please enter your name:"); 
    inputbox.setReadOnly(True);
    inputbox.resize(200,30);
    inputbox.move(20,70);

    combobox = QComboBox(window);
    combobox.addItems(["item 1","item 2","item3"]);
    combobox.move(100,110);

    button = QPushButton(window);
    button.setText("Click Me");
    button.move(100,150);
    button.clicked.connect(button_clicked);

    window.show();
    sys.exit(application.exec_());
    
