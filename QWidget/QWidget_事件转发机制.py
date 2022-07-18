from PyQt5.Qt import *
import sys

class Window(QWidget):
    # def __init__(self):
    #     super().__init__()
    #     self.setWindowTitle("事件转发机制")
    #     self.resize(500, 500)
    #     self.setup_ui()

    def mousePressEvent(self, QMouseEvent):
        print("顶层窗口鼠标按下")

class MidWindow(QWidget):
    def mousePressEvent(self, QMouseEvent):
        print("中间控件被按下")

# 如果label控件没有处理，则会把事件转发到相应的父对象中，
class Label(QLabel):
    def mousePressEvent(self, evt):
        # 相当于告诉系统，自己已经对该对象进行处理，不需要再去找其父对象进行处理
        #evt.accept()
        # 判断该事件是否被接收，接收则证明事件已经被处理
        #print(evt.isAccept())
        # 不去处理事件，自己处理之后再去经过父对象处理
        evt.ignore()
        print("标签控件鼠标按下")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.setWindowTitle("事件转发机制")
    window.resize(500, 500)

    # 中间窗口 的背景样式没有生效，
    mid_window = MidWindow(window)
    mid_window.resize(300, 300)
    # 使样式生效
    mid_window.setAttribute(Qt.WA_StyledBackground, True)
    mid_window.setStyleSheet("background-color:yellow")

    label = Label(mid_window)
    # label和btn都是系统提供的控件
    # 点击按钮不会有任何反应，但点击标签会显示中间控件被按下
    # 是因为按钮就是监听用户的点击
    # 则该类的实例方法中会有对应的相关鼠标点击事件的处理操作，故不会在转发到其他父对象中
    #label = QLabel(mid_window)
    label.setText("这是一个标签")
    label.move(100, 100)
    label.setStyleSheet("background-color:red")

    btn = QPushButton(mid_window)
    btn.setText("我是按钮")
    btn.move(50, 50)
    window.show()

    sys.exit(app.exec_())