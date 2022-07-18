from PyQt5.Qt import *

# # 为了兼容引入如下参数
class Slider(QSlider):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent=None, *args, **kwargs)
        self.setTickPosition(QSlider.TicksBothSides)
        self.setup_ui()

    # 添加子控件方法
    def setup_ui(self):
        self.label = QLabel(self)
        self.label.setText("0")
        self.label.setStyleSheet("color:red")
        # 隐藏标签,一开始隐藏标签
        self.label.hide()

    # 监听鼠标按下事件
    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        x = (self.width() - self.label.width()) / 2
        y = ((1 - self.value() / (self.maximum() - self.minimum())) * (self.height() - self.label.height()))
        # 点击鼠标之后显示标签
        self.label.show()
        self.label.move(x, y)

    # 鼠标移动方法
    def mouseMoveEvent(self, evt):
        super().mouseMoveEvent(evt)
        x = (self.width() - self.label.width()) / 2
        y = (1 - self.value() / (self.maximum() - self.minimum()) * self.height() - self.height())
        self.label.show()
        self.label.move(x, y)
        # 改变标签内部的数值
        self.label.setText(str(self.value()))
        self.label.adjustSize()

    # 监听鼠标释放方法
    # def mouseReleaseEvent(self, evt):
    #     super().mouseReleaseEvent(evt)
    #     #self.label.hide()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSlider的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 控件1
        slider = Slider()
        slider.setParent(self)
        slider.move(200, 200)
        slider.resize(30, 200)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
