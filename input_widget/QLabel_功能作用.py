from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel_功能作用的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 文本标签（一个矩形区域）,通过&符号绑定快捷键
        label = QLabel("账号(&s)", self)
        label.setStyleSheet("background-color:cyan")
        label.move(100, 100)
        # 根据文本内容调整控件尺寸
        #label.adjustSize()
        label.resize(300, 300)
        # 设置右对齐方式
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        # 缩进20
        label.setIndent(20)
        # 设置控件内部间距（边与内容的距离,上下左右都留有边距）
        label.setMargin(10)
        # 设置文本格式为普通文本
        label.setTextFormat(Qt.PlainText)

        le1 = QTextEdit(self)
        le1.move(300, 300)

        le2 = QTextEdit(self)
        le2.move(300, 350)
        # 绑定小伙伴1，可通过设置label快捷键获取文本框的焦点
        label.setBuddy(le1)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(700, 700)
    window.show()

    sys.exit(app.exec_())
