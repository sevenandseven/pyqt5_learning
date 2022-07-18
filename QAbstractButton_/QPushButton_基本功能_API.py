import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)
window = QWidget()

# 方法一
#btn = QPushButton(window)
# 方法二
# btn = QPushButton()
# btn.setParent(window)
# btn.setText("xxx")
# btn.setIcon(QIcon("路径"))
# 方法三
btn = QPushButton("xxx", window)
# # 方法四
# btn = QPushButton(QIcon("路径"), "xxx", window)

# 菜单的设置
# 首先创建一个menu对象
menu = QMenu()
# menu后可以添加行为、分割线、图标、子菜单等，可以进入类中查看方法
# 子菜单 最近打开
# 行为动作 新建 打开 分割线 退出
# 方案一
# new_action = QAction()
# new_action.setText("新建")
# 方案二
new_action = QAction("新建", menu)
# 监听行为的信号
new_action.triggered.connect(lambda: print("新建文件"))
open_action = QAction("打开", menu)
open_action.triggered.connect(lambda: print("打开文件"))
exit_action = QAction("退出", menu)
exit_action.triggered.connect(lambda:print("退出文件"))

# 子菜单
oprn_recent_menu = QMenu(menu)
oprn_recent_menu.setTitle("最近打开")
file_action = QAction("python-pyqt")
oprn_recent_menu.addAction(file_action)

menu.addAction(new_action)
menu.addAction(open_action)
menu.addSeparator()
menu.addMenu(oprn_recent_menu)

menu.addAction(exit_action)

# 给按钮后添加菜单
btn.setMenu(menu)
# 菜单的获取
print(btn.menu())
btn.setStyleSheet("background-color: red")
# 将按钮设置为扁平状
btn.setFlat(True)

# 将按钮设置为自动默认按钮
# 只有当按钮被点击一次之后，他才会是默认按钮
btn.setAutoDefault(True)
print(btn.autoDefault())
# 不需要点击该按钮，一直是自动默认按钮
btn.setDefault(True)

window.setWindowTitle("按钮的功能")
window.resize(500, 500)

window.show()
# 菜单的显示
#menu.show()
sys.exit(app.exec_())
