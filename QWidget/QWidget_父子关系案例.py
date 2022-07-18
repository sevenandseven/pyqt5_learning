from PyQt5.Qt import *
import sys

# 方法一
class Label(QLabel):
    def mousePressEvent(self, QMouseEvent):
        self.setStyleSheet("background-color:red")

# 方法二
class Window(QWidget):
    def mousePressEvent(self, evt):
        #print("被点击了！")
        local_x = evt.x()
        local_y = evt.y()
        sub_widget = self.childAt(local_x, local_y)
        if sub_widget is not None:
            sub_widget.setStyleSheet("background-color:red")
        # 找到该点的子控件，并改背景，没有则不执行任何操作
        #print("被点击了！", local_x, local_y)


app = QApplication(sys.argv)
window = Window()
window.setWindowTitle("父子关系的学习")
window.resize(500, 500)

for i in range(1, 11):
    #label = Label(window)
    label = QLabel(window)
    label.setText("标签" + str(i))
    label.move(30*i, 30*i)

window.show()
sys.exit(app.exec_())