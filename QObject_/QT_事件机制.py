from PyQt5.Qt import *
import sys

class App(QApplication):
    # 方法的重写,一个是事件的接收者，一个是被包装的事件
    # 优先调用子类的方法
    def notify(self,receiver, evt):
        # 过滤不需要的事件对象,只显示QPushButton按钮的事件
        # 并过滤其他除鼠标按下事件的其他按事件
        if receiver.inherits("QPushButton") and evt.type() == QEvent.MouseButtonPress:
            print(receiver, evt)
        # 继承父类的方法,分发事件，使事件传下去，
        # 分发给事件接收者按钮，按钮中有evet方法
        # 可以拦截but中的evt

        return super().notify(receiver, evt)

class Btn(QPushButton):
    # 很多事件都包含在其中，绘制事件、点击事件等
    # evt具体的事件对象有很多类型
    # 会根据evt的事件类型（鼠标事件、键盘事件）分发给receiver具体的事件函数
    # 具体的事件函数，重写了btn的事件接收者方法，导致信号被覆盖，无法调用槽函数
    def event(self, evt):
        if evt.type() == QEvent.MouseButtonPress:
            print(evt)

        # 让事件继续往下分发
        return super().event(evt)

    # 重写父类的方法，如果没有重写父类的方法
    # 他就会调用父类的方法，发出信号，调用自定义的槽函数
    def mousePressEvent(self, *args, **kwargs):
        print("鼠标被按下了.....")
        # 直接返回父类的消息
        return super().mousePressEvent(*args, **kwargs)

if __name__=="__main__":
    # 创建app对象
    #app = QApplication(sys.argv)
    # 他会先使用App中的方法，如果子类没有，则会调用父类
    app = App(sys.argv)
    window = QWidget()
    btn = Btn(window)
    btn.setText("按钮")
    btn.move(100, 100)

    def cao():
        print("按钮被点击了")

    # 鼠标点下去就触发
    btn.pressed.connect(cao)

    window.show()
    # 创建退出方法，
    sys.exit(app.exec_())
