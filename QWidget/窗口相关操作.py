from PyQt5.Qt import *
import sys

class Window(QWidget):
    def mousePressEvent(self, QMouseEvent):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

app = QApplication(sys.argv)
window = Window()

# # 创建icon对象,设置图标图像
# icon = QIcon(r'C:\Users\22104\Desktop\OIP-C.jpg')
# window.setWindowIcon(icon)
# window.setWindowTitle("W1")
# # window.resize(500, 500)
# # window.setWindowOpacity(0.7)
# # # 获取
# #print(window.windowOpacity())
#
# # 输出结果为true则证明窗口是无状态窗口
# #print(window.windowState() == Qt.WindowNoState)
#
# # 有最大化、最小化、全屏，全屏无法关闭只能通过任务管理器处理
# w2 = QWidget()
# w2.setWindowTitle("w2")
# #window.setWindowState(Qt.WindowMaximized)
# # 后展示的窗口会显示在上边
# # 可以通过对w1窗口进行活跃设置，使他显示在2的上边
#
# window.setWindowState(Qt.WindowActive)
# window.show()
# w2.show()

window.showMaximized()
sys.exit(app.exec_())