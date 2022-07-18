from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("交互状态案例学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText("标签")
        label.move(100, 50)
        label.hide()

        le = QLineEdit(self)
        # 给文本框默认内容
        le.setText("文本框")
        le.move(100, 100)

        btn = QPushButton(self)
        btn.setText("登录")
        btn.move(100, 150)
        btn.setEnabled(False)

        # 可以监听文本框内容的改变、并且获取内容
        def text_cao(text):
            print("文本内容发生了改变", text)
            # if len(text) > 0:
            #     btn.setEnabled(True)
            # else:
            #     btn.setEnabled(False)
            btn.setEnabled(len(text) > 0)

        def check():
            # 获取文本框内容
            content = le.text()

            # 判断是否是Sz
            if content == "Sz":
                label.setText("登录成功")
            # 是，显示之前隐藏的提示标签，展示文本
            else:
                label.setText("登录失败")

            label.show()
            label.adjustSize()

        le.textChanged.connect(text_cao)
        btn.pressed.connect(check)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
