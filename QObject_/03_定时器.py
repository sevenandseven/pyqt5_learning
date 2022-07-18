from PyQt5.Qt import *
import sys

class MyObject(QObject):
    # 重写timerEvent方法，形参代表定时器事件
    def timerEvent(self, evt):
        print(evt, '1')


if __name__=="__main__":
    # 创建app对象
    app = QApplication(sys.argv)
    # 创建控件
    window = QWidget()
    window.setWindowTitle("QObject定时器的使用")
    window.resize(500, 500)

    # 创建QObject对象
    obj = MyObject()
    # 第一个参数是ms间隔事件
    # 每个给定ms就会执行QObject对象内部的TimerEvent()方法
    timer_id = obj.startTimer(1000)

    # 通过定时器的id关闭定时器
    obj.killTimer(timer_id)
    window.show()
    # 创建退出方法，
    sys.exit(app.exec_())
