import sys
from PyQt5.Qt import *

# 做成活动模块，修改方便
# 1、创建应用程序,可以传递参数给app，通过命令行输入参数
app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("Qlabel的学习")
window.resize(500, 500)

label = QLabel(window)
label.setText("xxx")

window.show()
sys.exit(app.exec_())
