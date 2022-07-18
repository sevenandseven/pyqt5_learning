from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QBoxLayou的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color:cyan")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color:yellow")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color:red")
        label4 = QLabel("标签4")
        label4.setStyleSheet("background-color:orange")

        layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(layout)
        # 设置伸缩因子
        # layout.addWidget(label1)
        # #layout.addSpacing(100)
        # layout.addWidget(label2)
        # # 添加空白的伸缩因子,默认伸缩因子为0
        # layout.addStretch()
        #layout.setStretchFactor(label2, 1)
        # layout.addWidget(label3)
        # layout.addWidget(label4)

        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color:pink")
        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color:blue")
        label7 = QLabel("标签7")
        label7.setStyleSheet("background-color:cyan")

        h_layout = QBoxLayout(QBoxLayout.RightToLeft)
        h_layout.addWidget(label5)
        h_layout.addWidget(label6, 1)
        h_layout.addWidget(label7)

        # 3、把需要布局的子控件添加到布局管理器中
        layout.addWidget(label1)
        layout.addLayout(h_layout, 1)
        layout.addWidget(label2)
        layout.addWidget(label3, 0)

        # 在索引为1的位置添加控件,插入控件
        # layout.insertWidget(1, label4)
        # label5 = QLabel("标签5")
        # label5.setStyleSheet("background-color:pink")
        # label6 = QLabel("标签6")
        # label6.setStyleSheet("background-color:blue")
        # label7 = QLabel("标签7")
        # label7.setStyleSheet("background-color:cyan")

        # h_layout = QBoxLayout(QBoxLayout.RightToLeft)
        # h_layout.addWidget(label5)
        # h_layout.addWidget(label6)
        # h_layout.addWidget(label7)
        #
        # # 插入布局
        # layout.insertLayout(2, h_layout)

        # 移除控件,指从布局管理器中移除，但控件本身仍然存在
        # layout.removeWidget(label1)
        #
        # label2.hide()
        # label2.show()

        # timer = QTimer(self)
        #
        # def test():
        #     layout.setDirection((layout.direction() + 1) % 4)
        # timer.timeout.connect(test)
        # timer.start(1000)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
