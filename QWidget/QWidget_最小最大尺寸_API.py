import sys
from PyQt5.Qt import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("最小最大窗口")
    # window.setMinimumSize(200, 200)
    # window.setMaximumSize(500, 500)
    # 单独设置宽和高
    window.setMaximumWidth(600)
    window.setMinimumWidth(200)
    # 设置之后resize不起作用,会按最大值起作用
    window.resize(1000, 1000)

    window.show()

    sys.exit(app.exec_())