from PyQt5.Qt import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #window = QWidget()
    # 换成组合控件,由很多部分组成
    window = QMainWindow()
    # 其中很多控件是懒加载，用到的时候才会创建
    # 尝试访问窗口的状态栏
    window.statusBar()
    window.setWindowTitle("信息提示案例")
    window.resize(500, 500)
    # 鼠标右上角显示？按钮
    window.setWindowFlags(Qt.WindowContextHelpButtonHint)

    # 当鼠标停在窗口控件身上之后，在状态栏提示的一段文本
    # 设置的文本内容
    window.setStatusTip("这是窗口")
    # 获取
    print(window.statusTip())

    label = QLabel(window)
    label.setText("信息交互")
    label.setStatusTip("这是标签")
    label.setToolTip("这是一个提示标签")
    print(label.toolTip())
    # 这个标签的显示时长是有限的,单位是ms，控制展示时长
    label.setToolTipDuration(100)
    # 获取展示时长
    print(label.toolTipDuration())

    label.setWhatsThis("这是啥？这是标签")
    window.show()
    sys.exit(app.exec_())
