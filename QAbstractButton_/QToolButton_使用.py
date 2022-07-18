import sys
from PyQt5.Qt import *

# 做成活动模块，修改方便
# 1、创建应用程序,可以传递参数给app，通过命令行输入参数
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QToolButton的使用")
window.resize(500, 500)

tb = QToolButton(window)
tb.setText("按钮")
tb.setArrowType(Qt.LeftArrow)
tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
tb.setAutoRaise(True)

menu = QMenu(tb)
menu.setTitle("菜单")
# 给菜单中放子菜单和行为

sub_menu = QMenu(menu)
sub_menu.setTitle("子菜单")

# 放置在meun父对象中
action = QAction("行为", menu)
action.setData([1,2,3])
# 监听action中的信号
#action.triggered.connect(lambda : print("点击了行为"))
menu.addMenu(sub_menu)
menu.addSeparator()
menu.addAction(action)

tb.clicked.connect(lambda: print("工具按钮被点击"))
tb.setMenu(menu)

# 可以获得相关的action对象
def do_action(action):
    print("点击了行为2", action.data())

tb.triggered.connect(do_action)

# 修改菜单的弹出方式
tb.setPopupMode(QToolButton.InstantPopup)
window.show()
sys.exit(app.exec_())
