import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("QTextEdit父类功能的测试")
window.resize(500, 500)

# 创建对象，接收用户输入的多行文本
text = QTextEdit("功能测试", window)
# 设置垂直滚动条一直存在,可以使用鼠标滚轮滚动
text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
# 水平滚动条设置
text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

# 设置角落控件
btn = QPushButton(window)
btn.setIcon(QIcon("xxx.png"))

# 监听按钮的点击事件
btn.clicked.connect(lambda: print("xxxx"))

# 将按钮设置为角落控件
text.setCornerWidget(btn)

window.show()
sys.exit(app.exec_())
