from PyQt5.Qt import *
import sys

# 用户对界面产生的特定行为会被包装成一个事件消息，该事件消息会被传递给特定对象的特定方法
# 监听特定方法就需要自定义类，继承某一个特定的类别

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("消息时间机制")
        self.resize(500, 500)
        self.setup_ui()

    # 在这里设置子控件
    def setup_ui(self):
        pass

    # 显示关闭事件
    # 在每个事件方法中都会把相关的事件传递给我们
    def showEvent(self, QshowEvent):
        print("窗口被展示出来")

    def closeEvent(self, QCloseEvent):
        print("窗口被关闭了")

    # 未移动之前会打印两遍，是因为展示时，系统需要将窗口摆放在正确位置，所以会移动
    def moveEvent(self, QMoveEvent):
        print("窗口被移动了")

    # 一开始展示窗口，肯定会有个尺寸调整大小，会触发该事件
    def resizeEvent(self, QResize):
        print("窗口改变了尺寸大小")

    def enterEvent(self, QEvent):
        print("鼠标进来了")
        self.setStyleSheet("background-color:cyan")

    def leaveEvent(self, QEvent):
        print("鼠标离开了")
        self.setStyleSheet("background-color:green")

    def mousePressEvent(self, QMouseEvent):
        print("鼠标被按下")

    def mouseReleaseEvent(self, QMouseEvent):
        print("鼠标被释放")

    def mouseDoubleClickEvent(self, QMouseEvent):
        print("鼠标双击")

    def mouseMoveEvent(self, QMouseEvent):
        print("鼠标移动了")

    def keyPressEvent(self, QKeyEvent):
        print("键盘上某一个键被按下了")

    def keyReleaseEvent(self, QKeyEvent):
        print("键盘上某一个键被释放了")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())