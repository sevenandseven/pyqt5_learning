from PyQt5.Qt import *
import sys

class Btn(QPushButton):
    def hitButton(self, point):
        # print(point)
        # if point.x() > self.width() / 2:
        #     return False
        # return True

        # 通过给定点坐标计算他与圆心的距离
        # 求解圆心
        center_x = self.width() / 2
        center_y = self.height() / 2

        # 给定点
        point_x = point.x()
        point_y = point.y()

        # 计算两点之间的距离
        import math
        distance = math.sqrt(math.pow(point_x - center_x, 2) + math.pow(point_y - center_y, 2))
        if distance < self.width() / 2:
            return True
        return False


    # 在整个按钮的内部绘制一个内切圆，使用绘制方法
    def paintEvent(self, QPointEvent):
        # 并将该事件传入，即在父类绘制的基础上在绘制一个内切圆
        super().paintEvent(QPointEvent)
        # 创建一个画家,画布为整个按钮
        painter = QPainter(self)
        # 创建一个画笔
        painter.setPen(QPen(QColor(100, 219, 234), 6))

        # 画圆,将整个按钮的矩形传入
        painter.drawEllipse(self.rect())
        # 文本内容为绘制出来的，重写了该方法之前的内容会覆盖，故需要调用父类相同的方法


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("按钮点击模拟")
window.resize(500, 500)

btn = Btn(window)
btn.setText("这是按钮")
btn.move(200, 200)
btn.resize(200, 200)

# 使按钮支持被选中
btn.setChecked(True)
# btn.pressed.connect(lambda: print("点击了这个按钮"))
# btn.released.connect(lambda: print("释放了这个按钮"))
btn.clicked.connect(lambda value: print("按钮被点击", value))
btn.toggled.connect(lambda value: print("按钮选中状态发生了改变", value))

# 方法一：使用btn.click模拟用户的点击
#btn.click()
# 方法二：两秒之后自动松开按钮
#btn.animateClick(2000)

btn2 = QPushButton(window)
btn2.setText("按钮")
#
# def signal():
#     #btn.click()
#     btn.animateClick(1000)
#
# btn2.pressed.connect(signal)

window.show()
sys.exit(app.exec_())