from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QColorDialog的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 修改控件的背景颜色，会影响控件内部的子控件
        # self.setStyleSheet("backcolor:red")
        # self.setStyleSheet("backcolor:rgb(100, 200, 150)")

        # QColorDialog.setCustomColor(4, QColor(200, 10, 40))
        # cd = QColorDialog(QColor(100, 200, 150), self)
        # cd.setWindowTitle("选择一个好看的颜色")
        # def color(col):
        #     # 使用调色板对象
        #     palette = QPalette()
        #     palette.setColor(QPalette.Background, col)
        #     self.setPalette(palette)

        # cd.colorSelected.connect(color)
        # cd.show()

        # def open_color():
        #     palette = QPalette()
        #     palette.setColor(QPalette.Background, cd.selectedColor())
        #     self.setPalette(palette)
        # cd.open(open_color)

        # def exec_color():
        #     # 使用调色板对象
        #     palette = QPalette()
        #     palette.setColor(QPalette.Background, cd.selectedColor())
        #     self.setPalette(palette)

        # if cd.exec():
        #     exec_color()

        # def curr_color():
        #     palette = QPalette()
        #     palette.setColor(QPalette.Background, cd.currentColor())
        #     self.setPalette(palette)
        #
        # cd.currentColorChanged.connect(curr_color)
        # cd.setOptions(QColorDialog.NoButtons | QColorDialog.ShowAlphaChannel)
        # cd.show()

        btn = QPushButton(self)
        btn.move(100, 100)
        btn.setText("测试按钮")
        #btn.clicked.connect(lambda: print(QColorDialog.customCount()))
        # 或者控件调用也可以
        #btn.clicked.connect(lambda: print(cd.customCount()))

        # 使用的是静态方法，每次创建的颜色选择对话框都是全新的对象，不存在上次默认选择颜色是哪一个
        # def test():
        #     color = QColorDialog.getColor(QColor(10, 20, 100), self, "选择颜色")
        #     palette = QPalette()
        #     palette.setColor(QPalette.Background, color)
        #     self.setPalette(palette)
        #     print(color)
        #
        # btn.clicked.connect(test)

        def test_():
            cd = QColorDialog(self)
            cd.setOptions(QColorDialog.NoButtons)
            cd.setWindowTitle("选择一个人生的颜色")

            def sel_color(color):
                palette = QPalette()
                palette.setColor(QPalette.ButtonText, color)
                btn.setPalette(palette)
            # 最终选择颜色确定时所发射的信号
            #cd.colorSelected.connect(sel_color)
            # 当前颜色发生改变时，所发射的信号
            cd.currentColorChanged.connect(sel_color)
            cd.show()
        btn.clicked.connect(test_)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
