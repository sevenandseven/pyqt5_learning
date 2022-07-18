from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPlainEdit的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pte = QPlainTextEdit(self)
        pte.resize(300, 300)
        pte.move(100, 100)
        self.pte = pte

        test_btn = QPushButton(self)
        test_btn.move(20, 20)
        test_btn.setText("测试按钮")
        test_btn.clicked.connect(self.btn_test)

        # 展示行号，先创建一个控件
        line_num_parent = QWidget(self)
        line_num_parent.resize(30, 300)
        line_num_parent.move(70, 100)
        line_num_parent.setStyleSheet("background-color:cyan")

        self.line_label = QLabel(line_num_parent)
        self.line_label.move(0, 2)

        # 1--100
        # 标签内部不支持竖着排,软换行情况则需要动态调整左侧标签
        line_nums = "\n".join([str(i) for i in range(1, 101)])
        self.line_label.setText(line_nums)
        self.line_label.adjustSize()

    def btn_test(self):
        self.信号的操作()

    def 信号的操作(self):
        self.pte.updateRequest.connect(lambda rect, dy:self.line_label.move
        (self.line_label.x(), self.line_label.y() + dy))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
