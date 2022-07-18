from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDial的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.move(200, 200)
        label.setText("社会我顺哥，人狠话不多")
        dia = QDial(self)
        # 改变值域范围
        # dia.setRange(66, 88)
        # dia.valueChanged.connect(lambda val: print("值发生了改变", val))
        #
        # # 是否显示刻度
        # dia.setNotchesVisible(True)
        # # 改变大刻度的步长
        # dia.setPageStep(5)
        # # 是否启用包裹，刻度包裹整个控件（360°滚动）
        # dia.setWrapping(True)
        # # 刻度目标之间的像素数
        # dia.setNotchTarget(50)
        def test(val):
            label.setStyleSheet("font:{}px".format(val))
            label.adjustSize()
        dia.valueChanged.connect(test)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
