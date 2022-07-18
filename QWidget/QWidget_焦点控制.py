from PyQt5.Qt import *
import sys

class Window(QWidget):
    def mousePressEvent(self, evt):
        print(self.focusWidget())
        # 聚焦到下一个子控件，即当鼠标聚焦时，焦点会跑到下一个子控件
        self.focusNextChild()
        # 聚焦到上一个子控件，当鼠标聚焦时，焦点会跑到上一个子控件
        self.focusPreviousChild()
        # 以上两种方法有一个方法原型,True则表示聚焦到下一个子控件
        self.focusNextPrevChild(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.setWindowTitle("焦点控制")
    window.resize(500, 500)

    le1 = QLineEdit(window)
    le1.move(50, 50)
    le2 = QLineEdit(window)
    le2.move(100, 100)
    le3 = QLineEdit(window)
    le3.move(150, 150)

    le2.setFocus()
    # 第二个控件获取焦点
    #le2.setFocus()
    # 通过tab键获取
    # le2.setFocusPolicy(Qt.TabFocus)
    # # 通过鼠标点击获取
    # le2.setFocusPolicy(Qt.ClickFocus)
    # # 两种策略同时获取
    # le2.setFocusPolicy(Qt.StrongFocus)
    #le2.clearFocus()

    # 静态方法调用如何、通过类名
    # le1之后由le3获取焦点
    QWidget.setTabOrder(le1, le3)
    # le3之后由le2获取焦点
    QWidget.setTabOrder(le3, le2)


    # 获取当前窗口内部，所有子控件当中获取焦点的哪个控件
    window.show()

    print(window.focusWidget())
    sys.exit(app.exec_())
