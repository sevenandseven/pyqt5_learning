from PyQt5.Qt import *

class Label(QLabel):
    # 设置最小尺寸(200, 300)
    def minimumSizeHint(self):
        return QSize(100, 100)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理器的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label1 = Label("标签1")
        label1.setStyleSheet("background-color:cyan")
        label2 = Label("标签2")
        label2.setStyleSheet("background-color:yellow")
        label3 = Label("标签3")
        label3.setStyleSheet("background-color:red")

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        # 标签1的宽和高都是定的,根据建议的尺寸固定宽和高
        label1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # 显示高的最小尺寸
        label2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        # 限制高的最大尺寸
        label2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        # 可以伸展也可以收缩策略QSizePolicy.Preferred
        label2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        # QSizePolicy.Expanding也可以伸展和收缩，但是优先级高于Preferred
        sp = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        # 如果隐藏控件就保留尺寸,必须在设置策略到标签内部之前
        sp.setRetainSizeWhenHidden(True)
        label3.setSizePolicy(sp)
        label3.hide()

        # QSizePolicy.Ignored忽略建议尺寸的大小
        #label3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Ignored)

        # 设置固定尺寸,它的优先级是最高的
        label1.setFixedSize(200, 200)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
