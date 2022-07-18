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

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("鼠标操作的案例1")
window.resize(500, 500)

label = MyLabel(window)
label.resize(200, 200)
label.move(100, 100)
label.setStyleSheet("background-color:cyan")
# 所有的键盘按键都会传递给标签控件
label.grabKeyboard()

window.show()
sys.exit(app.exec_())