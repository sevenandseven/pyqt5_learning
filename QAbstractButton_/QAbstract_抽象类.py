import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("按钮的功能测试--抽象类")
window.resize(500, 500)

# # 文本操作
# def one_plus():
#     num = int(btn.text()) + 1
#     btn.setText(str(num))
#
btn = QPushButton(window)
# btn.setText("1")
# btn.pressed.connect(one_plus)

def dian_ji():
    print("按钮被点击")

# 快捷键的设置
#btn.setText("a&bc")
btn.setShortcut("Alt+b")
btn.pressed.connect(dian_ji)


# 图标操作
icon = QIcon(r"C:\Users\22104\Desktop\OIP-C.jpg")
btn.setIcon(icon)
size = QSize(50, 50)
btn.setIconSize(size)

window.show()
sys.exit(app.exec_())
