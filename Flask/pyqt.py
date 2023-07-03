from PyQt5.QtWidgets import *

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(200, 200, 300, 400)
    window.setWindowTitle("Perkenalan")
    
    layout = QVBoxLayout()
    
    label = QLabel("Selamat Datang Di Lab TI")
    button = QPushButton("Next Page")

    button.clicked.connect(on_clicked)
    layout.addWidget(label)
    layout.addWidget(button)
    
    window.setLayout(layout)
    window.show()
    app.exec_()
    
def on_clicked():
    message = QMessageBox()
    message.setText("perkenalkan nama saya Naufal Arkan Zhafran")
    message.exec_()
    
if __name__ == '__main__':
    main ()
    