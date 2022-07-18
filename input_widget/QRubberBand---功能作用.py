from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRubberBand的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 橡皮控件需要定义其尺寸大小，位置对应尺寸
        # 借助其他方法设置一定的区域才可以显示出来
        rb = QRubberBand(QRubberBand.Rectangle, self)
        rb.setGeometry(10, 10, 60, 60)
        # 判断当前橡皮筋属性是否被显示
        print(rb.isVisible())
        rb.show()
    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
