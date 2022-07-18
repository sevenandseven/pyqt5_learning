from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)

# 创建一个子控件
green = QWidget(window)
green.resize(100, 100)
green.setStyleSheet("background-color:green")
green.move(300, 50)


# 创建一个子控件
red = QWidget(window)
red.resize(100, 100)
red.setStyleSheet("background-color:red")
red.move(300, 0)

window.show()
sys.exit(app.exec_())