from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QKeySequenceEdit的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 通过这种方法设置默认值
        kse = QKeySequenceEdit(self)
        # 方法一：通过字符串设置快捷键
        #ks = QKeySequence("Ctrl + C")
        # 方法二：通过标准键位序列设置快捷键
        #ks = QKeySequence(QKeySequence.Copy)
        ks = QKeySequence(Qt.CTRL + Qt.Key_C, Qt.CTRL + Qt.Key_A)
        # 方法三：通过枚举值对应的整型数据
        kse.setKeySequence(ks)
        # 清空
        kse.clear()
        # 通过按钮获取他的默认值
        btn = QPushButton(self)
        btn.move(100, 100)
        btn.setText("测试按钮")
        btn.clicked.connect(lambda: print(kse.keySequence().toString(),
                                          kse.keySequence().count()))

        kse.editingFinished.connect(lambda: print("结束编辑"))
        kse.keySequenceChanged.connect(lambda key_val: print("键位序列发生改变", key_val.toString()))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
