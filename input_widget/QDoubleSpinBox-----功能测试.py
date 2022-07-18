from PyQt5.Qt import *

class MyDoubleSB(QDoubleSpinBox):
    def textFromValue(self, p_float):
        print("xxxxxx", p_float)
        return str(p_float) + "*" + str(p_float)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDoubleSpinBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        dsb = QDoubleSpinBox(self)
        # dsb.move(100, 100)
        # dsb.resize(100, 30)
        # dsb.setMaximum(88.88)
        # dsb.setMinimum(22.22)
        # dsb.setSingleStep(0.02)
        # dsb.setWrapping(True)
        # dsb.setPrefix("$")
        # dsb.setSuffix("%")
        # dsb.setRange(1.0, 2.0)
        # dsb.setSingleStep(0.5)
        # dsb.setSuffix("倍速")
        # dsb.setSpecialValueText("正常")
        # dsb.setWrapping(True)

        test_btn = QPushButton(self)
        test_btn.move(300, 300)
        test_btn.setText("测试按钮")
        test_btn.clicked.connect(lambda: dsb.setValue(-166.66))
        test_btn.clicked.connect(lambda: print(type(dsb.value()), dsb.value()))
        test_btn.clicked.connect(lambda: print(type(dsb.cleanText()), dsb.cleanText()))
        # 获取全部文本,方法一
        test_btn.clicked.connect(lambda: print(type(dsb.text()), dsb.text()))
        # 方法二
        test_btn.clicked.connect(lambda: print(type(dsb.lineEdit().text()), dsb.lineEdit().text()))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
