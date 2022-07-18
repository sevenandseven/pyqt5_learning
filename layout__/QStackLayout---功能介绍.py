from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackLayout---的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 以下两步等效于
        #sl = QStackedLayout(self)
        sl = QStackedLayout()
        self.setLayout(sl)

        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color:cyan")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color:yellow")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color:red")
        label4 = QLabel("标签4")
        label4.setStyleSheet("background-color:orange")

        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color:pink")
        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color:blue")
        label7 = QLabel("标签7")
        label7.setStyleSheet("background-color:cyan")

        v_layout = QVBoxLayout()
        v_layout.addWidget(label5)
        v_layout.addWidget(label6)
        v_layout.addWidget(label7)

        sl.addWidget(label1)
        sl.addWidget(label2)
        sl.addWidget(label3)

        print(sl.addWidget(label1))
        print(sl.addWidget(label2))
        print(sl.addWidget(label3))

        # 获取当前正在展示的控件的索引值
        # print(sl.currentIndex())
        # print(sl.insertWidget(0, label4))
        # # 获取改变之后的控件的索引值
        # print(sl.currentIndex())
        # 根据索引值也可以获得相应的控件
        # print(sl.widget(2).text())
        #
        # # 切换当前显示控件
        # sl.setCurrentIndex(2)
        # # 根据控件切换当前控件
        # sl.setCurrentWidget(label5)
        #
        # timer = QTimer(self)
        # timer.timeout.connect(lambda: sl.setCurrentIndex((sl.currentIndex() + 1) % sl.count()))
        # timer.start(1000)

        # 显示所有控件
        sl.setStackingMode(QStackedLayout.StackAll)
        label1.setFixedSize(100, 100)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
