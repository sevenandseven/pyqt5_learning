from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        box1 = QWidget(self)
        box2 = QWidget(self)
        box2.setObjectName("box2")
        box3 = QWidget(box2)
        box3.resize(150, 150)
        #box3.setStyleSheet("background-color: lightgray")

        # 全局筛选，借用QApplication筛选，设置方式一
        #self.setStyleSheet("QPushButton {background-color:orange}")
        # 可以通过选择器设置部分控件的颜色
        #box1.setStyleSheet("QPushButton {background-color:orange;}")
        #box1.setStyleSheet("background-color:orange")
        #box2.setStyleSheet("background-color:cyan")

        #样式表影响的空间范围，级联关系
        label1 = QLabel("标签1", box1)
        label1.setObjectName("l1")
        label1.move(50, 50)
        btn1 = QPushButton("按钮1", box1)
        btn1.move(150, 50)

        cb = QCheckBox("python", box1)
        cb.move(150, 200)
        cb.resize(100, 50)

        label1.setProperty("notice_level", "warning")
        label1.resize(200, 60)

        label2 = QLabel("标签2", box2)
        label2.move(50, 50)
        btn2 = QPushButton("按钮1", box2)
        btn2.move(150, 50)

        btn2.setObjectName("b2")
        v_layout = QVBoxLayout()
        self.setLayout(v_layout)

        v_layout.addWidget(box1)
        v_layout.addWidget(box2)
        # 当一个控件不设置父控件，他就是一个独立的窗口
        # 局部变量走完这个方法就会被释放，所以将他设置为self，为全局变量
        self.other_btn = QPushButton("按钮3")
        self.other_btn.show()

if __name__ == "__main__":
    import sys
    # 从模块中导入一个模块
    from tool_ import QSSTool
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()
    # 设置方式2，还包含独立的窗口控件，即包含单独的按钮窗口控件
    #app.setStyleSheet("QPushButton {background-color:orange}")

    QSSTool.setQssToObj("test.qss", app)

    # with open("test.qss", "r") as f:
    #     content = f.read()
    #     app.setStyleSheet(content)
    # 通过id选择器定位标签1
    sys.exit(app.exec_())
