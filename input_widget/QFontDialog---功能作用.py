from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontDialog---功能作用的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 设置一个默认值
        font = QFont()
        font.setFamily("宋体")
        font.setPointSize(36)
        # # 设置当前默认值
        # fd = QFontDialog(font, self)
        # # 设置当前字体
        # #fd.setCurrentFont(font)
        #
        # # 选项控制，不显示确认和取消按钮
        # fd.setOption(QFontDialog.NoButtons)
        # # 选项控制，希望多个同时生效
        # fd.setOptions(QFontDialog.NoButtons | QFontDialog.MonospacedFonts)

        # 测试某一个选项是否生效
        #print(fd.testOption(QFontDialog.MonospacedFonts))
        btn = QPushButton(self)
        btn.setText("字体选择")
        btn.move(200, 200)
        # def font_sel():
        #     # 获得当前所选择的最终字体
        #     print("字体已经被选择", fd.selectedFont())

        #btn.clicked.connect(lambda: fd.open(font_sel))

        #btn.clicked.connect(fd.open)
        # 通过输出结果可以判读用户最终选择什么结果
        #print(fd.exec())
        # if fd.exec():
        #     print(fd.selectedFont().family())
        #fd.show()

        label = QLabel(self)
        label.move(200, 100)
        label.setText("社会顺哥")

        # def cfc(font):
        #     label.setFont(font)
        #     label.adjustSize()
        #
        # fd.currentFontChanged.connect(cfc)

        def font_sel():
            # 静态方法一
            #result = QFontDialog.getFont(self)
            # 静态方法二
            result = QFontDialog.getFont(font, self, "选择一个好看的字体")
            print(result)
            # 取元组中最后一个元素，返回的True或者False指点击的对话窗口的确认或取消键
            if result[1] == True:
                label.setFont(result[0])
                label.adjustSize()

        btn.clicked.connect(font_sel)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
