import sys
from PyQt5.Qt import *

# 做成活动模块，修改方便
# 1、创建应用程序,可以传递参数给app，通过命令行输入参数
app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("QFrame功能测试")
window.resize(500, 500)

# 创建一个QFrame对象
frame = QFrame(window)
frame.resize(100, 100)
frame.move(100, 100)
frame.setStyleSheet("background-color:cyan;")

# 设置frame的外观形状
frame.setFrameShape(QFrame.Box)
# 凸起效果主要通过几条线营造出这样一个效果
frame.setFrameShadow(QFrame.Raised)
# 设置最外层的线宽
frame.setLineWidth(6)
# 设置中层线宽(灰色部分)
# 当整个形状为一个平面时，他是没有中线宽度的
frame.setMidLineWidth(12)

#frame.setFrameStyle(QFrame.Box | QFrame.Raised)

# 输出总线宽度
print(frame.frameWidth())

# 设置整个框架所占的范围
frame.setFrameRect(QRect(20, 20, 60, 60))

window.show()
sys.exit(app.exec_())
