from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressBar---简介的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pb = QProgressBar(self)
        pb.resize(400, 30)
        # 输出默认的最小值和最大值
        print(pb.minimum())
        print(pb.maximum())

        # 设置当前值
        pb.setValue(49)

        # 重置进度条
        def test():
            pb.reset()
            print(pb.minimum())
            print(pb.maximum())
            print(pb.value())
        btn = QPushButton(self)
        btn.move(200, 200)
        btn.setText("测试按钮")
        btn.clicked.connect(test)

        # 展示当前数值以及总值
        #pb.setFormat("当前人数 / 总人数 %p %")
        #pb.setFormat("当前人数 %v / 总人数 %m")
        pb.setFormat("当前人数 {} / 总人数 %m".format(pb.value() - pb.minimum()))

        # 水平居中
        #pb.setAlignment(Qt.AlignHCenter)

        # 获取文本标签中的内容
        print(pb.text())
        # 设置文本标签不可见
        pb.setTextVisible(False)

        # 改变进度条的方向
        pb.setOrientation(Qt.Vertical)
        # 手动改变进度条的尺寸
        pb.resize(30, 400)
        # 需要手动设置文本标签的方向,仍然不会显示文本标签
        pb.setTextDirection(QProgressBar.TopToBottom)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
