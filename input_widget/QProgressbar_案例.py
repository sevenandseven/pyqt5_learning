from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("进度条案例")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pb = QProgressBar(self)
        pb.setValue(39)
        # 生成一个定时器，他的周期归进度条管理
        timer = QTimer(pb)
        def progress_change():
            pb.setValue(pb.value() + 1)

        # 开启定时器之后，每隔一定的时间会发射一定的信号
        timer.timeout.connect(progress_change)
        # 设置间隔为1m
        timer.start(1000)
        pb.valueChanged.connect(lambda val: print("当前进度值为：", val))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
