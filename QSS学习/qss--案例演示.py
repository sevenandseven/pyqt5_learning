from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("案例的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        w = QTextEdit("按钮", self)
        #w.setEchoMode(QLineEdit.Password)
        w.setReadOnly(True)
        w.resize(200, 200)
        w.move(100, 100)


if __name__ == "__main__":
    import sys
    from tool_ import QSSTool
    app = QApplication(sys.argv)
    QSSTool.setQssToObj("demo_qpushbutton.qss", app)

    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
