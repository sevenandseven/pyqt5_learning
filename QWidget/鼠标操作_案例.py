import sys
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("鼠标操作案例")
        self.resize(500, 500)
        self.move(500, 200)
        # 设置鼠标跟踪之后会调用window内部的mouseMoveEvent事件
        self.setMouseTracking(True)

        pixmap = QPixmap(r"C:\Users\22104\Desktop\OIP-C.jpg").scaled(20, 20)
        cursor = QCursor(pixmap)
        self.setCursor(cursor)

        label = QLabel(self)
        self.label = label
        label.setText("鼠标鼠标")
        label.move(100, 100)
        label.setStyleSheet("background-color:cyan")

    def mouseMoveEvent(self, mv):
        print("鼠标移动", mv.localPos())
        # 应用在父控件中查找子控件的方法，则可查到label控件
        label = self.findChild(QLabel)
        label.move(mv.localPos().x(), mv.localPos().y())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())