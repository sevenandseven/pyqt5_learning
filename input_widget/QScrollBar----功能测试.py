from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QScrollBar的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        sb = QScrollBar(self)
        # 这个控件需要手动调整大小
        sb.resize(30, 200)
        sb.move(100, 100)

        sb2 = QScrollBar(Qt.Horizontal, self)
        sb2.resize(200, 30)
        sb2.move(100, 100)

        sb.valueChanged.connect(lambda val: print(val))
        # 滑块高度变高
        sb.setPageStep(50)

        # 捕获当前键盘
        sb.grabKeyboard()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
