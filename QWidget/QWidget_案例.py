from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.move(300, 300)
window.resize(500, 500)
window.show()

# 总的控件个数
widget_count = 100
# 一行有多少列
column_count = 5

# 计算一个控件的宽度
widget_width = window.width()/column_count
# 编号//一行有多少列(整除) + 1, 总共有多少行
row_count = (widget_count - 1) // column_count + 1
widget_height = window.height() / row_count

for i in range(0, widget_count):
    w = QWidget(window)
    w.resize(widget_width, widget_height)
    # 每个控件的x应该是所在列号*控件宽度；编号%一行有多少列
    widget_x = i % column_count * widget_width
    # 每个控件的y应该是行号*控件高度；编号//一行有多少列
    widget_y = i // column_count * widget_height
    w.move(widget_x, widget_y)
    w.setStyleSheet("background-color:red; border:1px solid yellow")
    w.show()

sys.exit(app.exec_())