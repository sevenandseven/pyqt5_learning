from PyQt5.Qt import *

class MyTextEdit(QTextEdit):
    # 重写鼠标操作事件
    def mousePressEvent(self, me):
        print(me.pos())
        # 获取坐标点位置所对应的锚点
        link_str = self.anchorAt(me.pos())
        if len(link_str) > 0:
            # 通过某一个方法打开对应的地址
            QDesktopServices.openUrl(QUrl(link_str))
        # 保证之前的功能依然生效
        return super().mousePressEvent(me)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit的学习")
        self.resize(500, 500)
        self.setup_ui()
    def text_change(self):
        print("文本内容发生了改变")

    def selection_change(self):
        print("文本选中的内容发生了改变")

    def copy_a(self, yes):
        print("复制是否可用", yes)

    def setup_ui(self):
        te = MyTextEdit("xxxxx", self)
        self.te = te
        te.move(50, 50)
        te.resize(300, 300)
        te.setStyleSheet("background-color:cyan;")
        # 监听文本内容发生改变
        te.textChanged.connect(self.text_change)
        te.selectionChanged.connect(self.selection_change)
        te.copyAvailable.connect(self.copy_a)

        te.insertHtml("xxx" * 30 + "<a href='http://www.itlike.com'>撩课</a>" + "aaa" * 200)

        test_btn = QPushButton(self)
        test_btn.move(10, 10)
        test_btn.setText("按钮")
        test_btn.clicked.connect(self.btn_pressed)

    def btn_pressed(self):
        pass

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
