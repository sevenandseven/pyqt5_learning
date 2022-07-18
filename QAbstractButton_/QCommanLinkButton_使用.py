import sys
from PyQt5.Qt import *

# 做成活动模块，修改方便
# 1、创建应用程序,可以传递参数给app，通过命令行输入参数
app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("QCommandLinkButton使用")
window.resize(500, 500)

btn = QCommandLinkButton("标题", "描述", window)
# 修改标题
btn.setText("标题2")
# 修改描述
btn.setDescription("界面")
# 修改图标
#btn.setIcon("路径")

window.show()
sys.exit(app.exec_())
