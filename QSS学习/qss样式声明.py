from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("样式声明的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel("标签测试", self)
        label.resize(300, 300)
        label.move(100, 100)
        self.qss边框(label)

    def qss边框(self, label):
        # 这个label的选择范围包括：label控件和他的子控件
        # 四条线设置统一的格式
        label.setStyleSheet("""
            QLabel{
            background-color:cyan;
            border-width:6px 20px;
            border-color:red;
            border-top-left-radius:300px;
            border-style:dotted soild dashed double;
            border-top-style:groove;
            }
        """)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
