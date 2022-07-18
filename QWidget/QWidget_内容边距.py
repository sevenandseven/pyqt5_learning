import sys
from PyQt5.Qt import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("内容边距的设定")
    window.resize(500, 500)

    label = QLabel(window)
    label.setText("界面学习")
    label.resize(300, 300)
    label.setStyleSheet("background-color:cyan")
    # 输出内容的矩形
    print(label.contentsRect())
    # 分别对应左上右下的间距,设置内容边距
    label.setContentsMargins(100, 200, 0, 0)
    print(label.getContentsMargins())

    window.show()

    sys.exit(app.exec_())