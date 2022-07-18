from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        # 调用父类的方法
        super().__init__()
        self.setWindowTitle("QLable学习")
        self.resize(500, 500)
        # 设置子控件
        self.setup_ui()

    def setup_ui(self):
        # QLabel的父控件是self
        label = QLabel(self)
        label.setText("xxx")

if __name__ =="__main__":
    import sys
    app = QApplication(sys.argv)
    # 实例化对象
    window = Window()
    window.show()

    sys.exit(app.exec_())
