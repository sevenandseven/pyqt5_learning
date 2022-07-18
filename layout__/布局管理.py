from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color:cyan")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color:yellow")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color:red")

        # 创建垂直排列的布局管理器对象
        v_layout = QHBoxLayout()
        # 将所有需要布局的子控件，添加到布局管理器中
        v_layout.addWidget(label1)
        v_layout.addWidget(label2)
        v_layout.addWidget(label3)
        # 设置左，上，右，下的外边距；
        v_layout.setContentsMargins(20, 30, 40, 50)
        # 设置元素之间的内边距
        v_layout.setSpacing(60)
        # 将布局管理器设置给子控件的父控件，设置排列方向
        self.setLayout(v_layout)
        self.setLayoutDirection(Qt.RightToLeft)

        # 打印出父控件的所以有子控件
        print(self.children())

        #label2.hide()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
