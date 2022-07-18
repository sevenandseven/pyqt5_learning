from PyQt5.Qt import *
import sys

class MyLabel(QLabel):
    def enterEvent(self, *args, **kwargs):
        print("鼠标进入")
        self.setText("欢迎光临")

    def leaveEvent(self, *args, **kwargs):
        print("鼠标离开")
        self.setText("谢谢惠顾")

    def keyPressEvent(self, evt):
        # if evt.key() == Qt.Key_Tab:
        #     print("用户点击了Tab键")
        # if evt.modifiers() == Qt.ControlModifier and evt.key() == Qt.Key_S:
        #     print("ctrl + s键被按下")
        if evt.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and evt.key() == Qt.Key_A:
            print("ctrl + Shift + A按下")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("窗口移动的学习")
        self.resize(500, 500)
        self.move_flag = False
        self.setup_ui()

    def setup_ui(self):
        pass
    def mousePressEvent(self, evt):
        # 引入move_flag即鼠标左键点击就会执行该方法
        if evt.button() == Qt.LeftButton:
            self.move_flag = True
            # 因为传入的self对象就是窗口
            print("鼠标按下")

            # 确定两个点，鼠标第一次按下的点、窗口当前所在的原始点
            # 鼠标第一次按下的点
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()
            #print(self.mouse_x, self.mouse_y)

            # 整个窗口左上角的坐标
            self.origin_x = self.x()
            self.origin_y = self.y()
            #print(self.origin_x, self.origin_y)

    def mouseMoveEvent(self, evt):
        #print("鼠标移动")

        if self.move_flag:
            # 每次都可以获取到最新的位置，用最新的位置减去原始的旧位置
            #print(evt.globalX(), evt.globalY())
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y
            #print(move_x, move_y)
            dest_x = self.origin_x + move_x
            dest_y = self.origin_y + move_y
            self.move(dest_x, dest_y)

    def mouseReleaseEvent(self, evt):
        self.move_flag = False
        print("鼠标释放")

app = QApplication(sys.argv)
window = Window()
window.setWindowTitle("鼠标操作的案例1")
window.resize(500, 500)
window.show()
window.setMouseTracking(True)
sys.exit(app.exec_())