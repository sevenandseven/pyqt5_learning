from PyQt5.Qt import *
import sys

class Window(QWidget):
    def paintEvent(self, evt):
        print("窗口被绘制")
        return super().paintEvent(evt)

class Btn(QPushButton):
    def paintEvent(self, evt):
        print("按钮被绘制")
        return super().paintEvent(evt)

app = QApplication(sys.argv)
window = QWidget()
w2 = QWidget()
w2.show()
# 想要控制窗口，标识出是否处于被编辑状态
# 首先将标题设置为特定的格式
window.setWindowTitle("交互状态[*]")
window.resize(500, 500)
window.setWindowModified(True)
#print(window.isWindowModified())
print(w2.isActiveWindow())


# btn = Btn(window)
# btn.setText("按钮")
# #btn.pressed.connect(lambda : print("按钮被点击了"))
# #btn.pressed.connect(lambda: btn.setVisible(False))
# btn.setVisible(True)
# 将按钮设置为不可用
# btn.setEnabled(True)
# # 输出按钮是否可用
# print(btn.isEnabled())

window.show()

# btn相对于window窗口是可见还是隐藏
# 结果为true，即父控件显示时子控件是否跟着被显示
#print(btn.isVisibleTo(window))


# print(btn.isHidden())
# print(btn.isVisible())
#window.setVisible(True)
#window.setHidden(False)
sys.exit(app.exec_())