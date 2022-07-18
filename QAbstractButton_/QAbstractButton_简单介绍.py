import sys
from PyQt5.Qt import *

class Btn(QAbstractButton):
    def paintEvent(self, evt):
        #print("绘制按钮")
        # 绘制按钮上要展示的一个界面内容
        # 创建一个画家
        painter = QPainter(self)

        # 给画家一个笔
        # 常见一个笔
        # 宽度是线条之类的宽度，字符不会发生改变
        pen = QPen(QColor(11, 22, 56), 6)
        # 设置这个笔
        painter.setPen(pen)
        # 画家画画
        # 动态绘制，获取设置过程中的文本
        painter.drawText(20, 20, "shehui")
        painter.drawText(20, 20, self.text())

        painter.drawEllipse(0, 0, 100, 150)


app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("QAbstarctButton学习")
window.resize(500, 500)

btn = Btn(window)
btn.setText("xxx")
btn.resize(100, 100)
btn.pressed.connect(lambda: print("点击了按钮"))

window.show()
sys.exit(app.exec_())
