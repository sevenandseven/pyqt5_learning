import sys
from PyQt5.Qt import *

# 做成活动模块，修改方便
# 1、创建应用程序,可以传递参数给app，通过命令行输入参数
app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("QCheckBox功能测试")
window.resize(500, 500)
cb = QCheckBox("&Python", window)
# 设置复选框为三态
cb.setTristate(True)
# 设置复选框状态为三态中的部分选中状态
cb.setCheckState(Qt.PartiallyChecked)

# 接收信号，并尝试打印出来信号
cb.stateChanged.connect(lambda state: print(state))

window.show()
sys.exit(app.exec_())
