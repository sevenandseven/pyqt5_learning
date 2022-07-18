from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTimeEdit----功能作用")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        te = QTimeEdit(QTime.currentTime(), self)
        # 设置格式
        te.setDisplayFormat("hh:m:zz a")
        print(te.time())


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
