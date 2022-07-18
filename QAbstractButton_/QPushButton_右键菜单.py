import sys
from PyQt5.Qt import *

class Window(QWidget):
    def contextMenuEvent(self, ContextMenuEvent):
        print("调用菜单")
        # 菜单的设置
        # 首先创建一个menu对象
        menu = QMenu(self)
        new_action = QAction("新建", menu)
        # 监听行为的信号
        new_action.triggered.connect(lambda: print("新建文件"))
        open_action = QAction("打开", menu)
        open_action.triggered.connect(lambda: print("打开文件"))
        exit_action = QAction("退出", menu)
        exit_action.triggered.connect(lambda: print("退出文件"))

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
        menu.exec_(ContextMenuEvent.globalPos())

app = QApplication(sys.argv)
window = Window()

btn = QPushButton("xxx", window)
btn.setStyleSheet("background-color: red")

window.setWindowTitle("按钮的功能")
window.resize(500, 500)

def show_menu(point):
    menu = QMenu(window)
    new_action = QAction("新建", menu)
    # 监听行为的信号
    new_action.triggered.connect(lambda: print("新建文件"))
    open_action = QAction("打开", menu)
    open_action.triggered.connect(lambda: print("打开文件"))
    exit_action = QAction("退出", menu)
    exit_action.triggered.connect(lambda: print("退出文件"))

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

    # 使用映射的方法将局部坐标点转换为全局点
    dest_point = window.mapToGlobal(point)
    menu.exec_(dest_point)


# 自定义上下文菜单,会发射一个信号
window.setContextMenuPolicy(Qt.CustomContextMenu)
window.customContextMenuRequested.connect(show_menu)

window.show()
sys.exit(app.exec_())
