from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

# 设置窗口无边框,方法一
#window = QWidget(flags=Qt.FramelessWindowHint)
# 方法二
window = QWidget()
window.setWindowFlags(Qt.FramelessWindowHint)
window.resize(500, 500)

# 每一个按钮距顶端有一个间距
top_margin = 10
# 每一个按钮给定宽和高，因为自定义调整出来结果之间可能会有间隙
btn_w = 80
btn_h = 40
# 添加三个子控件，放置在窗口的右上角
close_btn = QPushButton(window)
close_btn.setText("关闭")
close_btn.resize(btn_w, btn_h)
# close_btn_w = close_btn.width()
window_w = window.width()
close_btn_x = window_w - btn_w
close_btn_y = top_margin
close_btn.move(close_btn_x, close_btn_y)

# def close():
#     window.close()
# close_btn.pressed.connect(close)
close_btn.pressed.connect(window.close)

# 设置最大化按钮
max_btn = QPushButton(window)
max_btn.setText("最大化")
max_btn.resize(btn_w, btn_h)
max_btn_x = close_btn_x - btn_w
max_btn_y = top_margin
max_btn.move(max_btn_x, max_btn_y)

def max_normal():
    if window.isMaximized():
        window.showNormal()
        max_btn.setText("最大化")
    else:
        window.showMaximized()
        max_btn.setText("恢复")

max_btn.pressed.connect(max_normal)

mini_btn = QPushButton(window)
mini_btn.setText("最小化")
mini_btn.resize(btn_w, btn_h)
mini_btn_x = max_btn_x - btn_w
mini_btn_y = top_margin
mini_btn.move(mini_btn_x, mini_btn_y)
mini_btn.pressed.connect(window.showMaximized)

window.setWindowTitle("顶层窗口操作案例")
window.show()

sys.exit(app.exec_())