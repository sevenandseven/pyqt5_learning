from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("基类QLayout的学习")
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

        # 1、创建布局管理器对象
        lay_out = QBoxLayout(QBoxLayout.TopToBottom)
        # 2、直接把布局管理器对象设置给需要布局的父控件
        self.setLayout(lay_out)

        # # 设置内边距
        # lay_out.setSpacing(60)
        # # 设置外边距
        # lay_out.setContentsMargins(30, 30, 40, 40)
        #
        # # 获取边距值
        # print(lay_out.contentsMargins().left())
        #
        # # 替换子控件
        # lay_out.replaceWidget(label2, label4)
        # # 隐藏label2但他并未被释放
        # label2.hide()
        # label2.setParent(None)
        # print(label2.parent())
        #
        # label2.destroyed.connect(lambda: print("标签2被释放"))

        # 添加子布局（借助布局的嵌套可以完成复杂功能）
        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color:pink")
        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color:blue")
        label7 = QLabel("标签7")
        label7.setStyleSheet("background-color:cyan")

        h_layout = QBoxLayout(QBoxLayout.RightToLeft)
        h_layout.addWidget(label5)
        h_layout.addWidget(label6)
        h_layout.addWidget(label7)

        # 3、把需要布局的子控件添加到布局管理器中
        lay_out.addWidget(label1)
        lay_out.addLayout(h_layout)
        lay_out.addWidget(label2)
        lay_out.addWidget(label3)
        # 布局管理器的能用性设置
        lay_out.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
