from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("信号与槽")
        self.resize(500, 500)

        self.Object_信号与槽2()

    def Object_信号与槽2(self):
        # 当我点击按钮的时候会打印一句话
        # self是因为最后要添加到窗口上，所以传入窗口对象
        btn = QPushButton(self)
        btn.setText("点击我")

        def cao():
            print("点我干啥！")

        # 连接信号与槽
        btn.clicked.connect(cao)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    # window = Window()
    # window.show()

    window = QWidget()
    # 连接窗口标题变化的信号 与 槽
    def cao_function(title):
        #print("窗口标题变化了！", title)
        window.windowTitleChanged.disconnect()
        # 或者临时终止
        #window.blockSignals(True)
        window.setWindowTitle("新课-" + title)
        window.windowTitleChanged.connect(cao_function)

    window.windowTitleChanged.connect(cao_function)

    window.setWindowTitle("Hello Sz")
    window.show()
    sys.exit(app.exec_())