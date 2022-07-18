from PyQt5.Qt import *
import sys

class MyLabel(QLabel):
    # 自定义的子类传递的参数全部传递到父类中去
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("10")
        self.move(100, 100)
        self.setStyleSheet("font-size:22px")

    def setSec(self, sec):
        self.setText(str(sec))

    def startMyTimer(self, ms):
        # 因为label是QObject的子类，所以QObject具有的属性label也有
        # 修改label中的timerEvent方法
        self.timer_id = self.startTimer(ms)


    def timerEvent(self, *args, **kwargs):
        # 获取当前标签的内容
        current_sec = int(self.text())
        current_sec -= 1
        self.setText(str(current_sec))

        if current_sec == 0:
            print("停止")
            self.killTimer(self.timer_id)

class MyWidget(QWidget):
    def timerEvent(self, *args, **kwargs):
        current_w = self.width()
        current_h = self.height()
        self.resize(current_h+10, current_h+10)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.setWindowTitle("QObject定时器的使用")
    window.resize(600, 600)

    # window中timerEvent没办法直接重写，故需要自定义子类
    window.startTimer(100)

    # # 通过类去创建一个控件，在设置一个父控件
    # label = MyLabel(window)
    # label.setSec(11)
    # # 每隔多少ms倒计时一次
    # label.startMyTimer(500)
    window.show()
    sys.exit(app.exec_())