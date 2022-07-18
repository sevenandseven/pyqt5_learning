import sys
from PyQt5.Qt import *

# 做成活动模块，修改方便
# 1、创建应用程序,可以传递参数给app，通过命令行输入参数
app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("QRadioButton---功能测试")
window.resize(500, 500)

# 创建父控件1
red = QWidget(window)
red.resize(200, 200)
red.move(50, 50)
red.setStyleSheet("background:red")
# 创建父控件2
green = QWidget(window)
green.resize(200, 200)
green.move(red.x() + red.width(),red.y() + red.height())
# print(green.x())
# print(green.y())
green.setStyleSheet("background:green")
# 创建性别为男的单选按钮
rb_nan = QRadioButton("男", red)
rb_nan.setShortcut("Alt+M")
rb_nan.move(50, 50)
# 默认设置选中按钮为男
#rb_nan.setChecked(True)

# 创建性别为女的单选按钮
rb_nv = QRadioButton("女-&Famale", red)
rb_nv.move(50, 100)
# isChecked是是否被选中
# 按钮选中和未选中两种状态相互切换
rb_nv.toggled.connect(lambda isChecked:print(isChecked))

# 独占
#rb_nv.setAutoExclusive(False)
rb_yes = QRadioButton("yes", green)
rb_yes.move(50, 50)
rb_no = QRadioButton("no", green)
rb_no.move(50, 100)

window.show()
sys.exit(app.exec_())

