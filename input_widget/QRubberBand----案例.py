from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRubberBand----案例的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 0，添加子控件，复选框
        # 一行有四列，每列宽度为50
        for i in range(0, 30):
            cb = QCheckBox(self)
            cb.setText("{}".format(i))
            cb.move(i % 4 * 50, i // 4 * 60)
        # 1创建一个橡皮筋选中控件
        self.rb = QRubberBand(QRubberBand.Rectangle, self)

    def mousePressEvent(self, evt):
        # 2尺寸大小：鼠标点击的位置点，00,获取相对于窗口的局部点
        self.origin_pos = evt.pos()
        # 鼠标刚按下去是没有尺寸的，所以给他一个空的尺寸
        self.rb.setGeometry(QRect(self.origin_pos, QSize()))
        # 3展示橡皮筋控件，
        self.rb.show()

    def mouseMoveEvent(self, evt):
        # 调整橡皮筋选中控件的位置及尺寸,
        # .normalized()保证没有负数
        # 新的坐标点减去旧的坐标点，或者分别传递左上角和右下角坐标，显示选中区域
        self.rb.setGeometry(QRect(self.origin_pos, evt.pos()).normalized())

        # 反向选中效果


    def mouseReleaseEvent(self, evt):
        # 1 获取橡皮筋控件的尺寸范围
        rect = self.rb.geometry()
        # 2 遍历所有的子控件，查看，那些子控件在区域范围
        for child in self.children():
            # 判断一个矩形是否包含另外一个点或者另外一个矩形
            if rect.contains(child.geometry()) and child.inherits("QCheckBox"):
                print(child)
                # 切换状态
                child.toggle()

        self.rb.hide()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
