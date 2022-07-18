from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QErroeMessage--的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # em = QErrorMessage(self)
        #
        # # 改变标题，想修改右侧的x或?需要通过flag方法
        # em.setWindowTitle("错误信息")
        # # 不仅设置内容，还可以弹出来
        # # 弹出对话框的模式是非模态窗口
        # em.showMessage("哈维i法海")
        # em.showMessage("哈维i法海")
        # em.showMessage("哈维i法海")
        pass
        # QErrorMessage.qtHandler()
        # qDebug("xxxx")
        # qWarning("12345")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()
    QErrorMessage.qtHandler()
    qDebug("xxxx")

    sys.exit(app.exec_())
