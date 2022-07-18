import sys
from PyQt5.Qt import *

# 做成活动模块，修改方便
# 1、创建应用程序,可以传递参数给app，通过命令行输入参数
app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("功能测试")
window.resize(500, 500)

le = QLineEdit(window)
le.move(100, 100)
le.resize(100, 100)
# 设置内容边距，改变整体的区域（我们的可视区域）
# le.setContentsMargins(100, 0, 0, 0)
le.setStyleSheet("background-color:cyan;")
# # 设置文本间距
# le.setTextMargins(100, 0, 0, 0)
#
# # 设置一个文本是水平靠右、垂直方向靠下
# le.setAlignment(Qt.AlignRight | Qt.AlignBottom)

btn = QPushButton(window)
btn.setText("按钮")
btn.move(100, 200)

def cusor_move():
#     # 属于单行文本编辑器的实例方法
#     # 向后移动，即鼠标向左移动
#     #le.cursorBackward(True, 2)
#     # 像前移动，即鼠标向右移动
#     #le.cursorForward(True, 3)
#     # 往后移动一个单词
    le.cursorBackward(True, 2)
    le.backspace()
#     # 移动到行首
#     le.home(True)
#     # 移动到行尾
#     le.end(True)
#     le.setCursorPosition(len(le.text() / 2))
    le.setFocus()

btn.clicked.connect(cusor_move)

# 监听文本编辑时发射的信号
le.textEdited.connect(lambda val: print("文本框编辑的时候", val))
# 文本框内容发生改变时的信号
le.textChanged.connect(lambda val: print("文本框内容发生改变的时候", val))

le.selectionChanged.connect(lambda: print("选中文本发生改变", le.selectedText()))

window.show()
sys.exit(app.exec_())
