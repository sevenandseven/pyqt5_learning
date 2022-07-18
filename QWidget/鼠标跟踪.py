import sys
from PyQt5.Qt import *

class MyWindow(QWidget):
    def mouseMoveEvent(self, me):
        # 获取全局的坐标
        print("鼠标移动了！", me.globalPos())

app = QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("鼠标操作")
window.resize(500, 500)
window.setMouseTracking(True)
print(window.hasMouseTracking())

window.show()

sys.exit(app.exec_())