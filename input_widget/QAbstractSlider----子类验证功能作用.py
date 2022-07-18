from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractSlider的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText("0")
        label.move(200, 200)
        label.resize(100, 30)

        sd = QSlider(self)
        sd.move(100, 100)
        sd.valueChanged.connect(lambda val: label.setText(str(sd.value())))

        sd.setMaximum(100)
        sd.setMinimum(66)

        # 设置当前数值
        sd.setValue(88)

        # 设置步长，设置的时键盘上的上下键控制
       # sd.setSingleStep(5)
        # 设置的pageup和pagedown的步长
        sd.setPageStep(8)

        # 跟踪设置
        print(sd.hasTracking())
        sd.setTracking(False)

        # 滑块位置的设置
        sd.setValue(88)

        # # 倒立外观
        # sd.setInvertedAppearance(True)
        #
        # # 反转控制
        # sd.setInvertedControls(True)

        # 改成水平的滑块
        #sd.setOrientation(Qt.Horizontal)

        # 监听移动信号
        sd.sliderMoved.connect(lambda val: print(val))
        # 行为触发信号,val:每一个数值有对应的行为标志数
        sd.actionTriggered.connect(lambda val: print(val))

        # 值域范围发生改变时发生的信号
        sd.rangeChanged.connect(lambda min,max: print(min, max))
        sd.setMaximum(99)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
