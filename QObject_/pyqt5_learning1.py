from PyQt5.Qt import *
import sys

# 导入包
# 创建一个应用程序对象
# 控件操作，设置控件，创建控件
# 展示一个应用程序对象，并进入消息循环

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("自定义QT界面")
window.resize(500, 500)
window.move(400, 200)

label = QLabel(window)
label.setText("hello world!")
label.move(200, 200)

window.show()
sys.exit(app.exec_())