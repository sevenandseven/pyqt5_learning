from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        #label = QLabel("账号(&s)", self)
        # 超链接
        #label = QLabel("<a href='http://www.itlike.com'>撩课</a>", self)
        label = QLabel("\n".join("123456789"), self)
        label.setStyleSheet("background-color:cyan")
        label.move(100, 100)
        # 根据文本内容调整控件尺寸
        # label.adjustSize()
        label.resize(300, 300)
        # 标签展示一个图片,设置图片自动根据控件尺寸大小改变
        #label.setPixmap(QPixmap(r"D:\Desktop\OIP-C.jpg"))
        #label.setScaledContents(True)

        # 设置文本交互格式,鼠标选中、键盘选中（shift键按下）、文本可编辑
        # label.setTextInteractionFlags(Qt.TextSelectableByMouse |
        #                               Qt.TextSelectableByKeyboard | Qt.TextEditable)

        # 控制选中文本（即给定选中区域）,从1开始选2个字符
        #label.setSelection(1, 3)

        # 链接和换行,设置打开外部链接
        label.setOpenExternalLinks(True)
        # 按单词换行
        #label.setWordWrap(True)
        # # 图片富文本
        # label.setText("<img src='D:\Desktop\OIP-C.jpg' width=20, height=60>")
        # # 设置数据，可以是整型也可以是浮点型
        # label.setNum(888.99)

        # # 创建一个画布对象
        # pic = QPicture()
        # # 创建一个画家、指名绘画设备
        # painter = QPainter(pic)
        # # 创建画笔或画刷
        # painter.setBrush(QBrush(QColor(255, 0, 255)))
        # painter.drawEllipse(0, 0, 200, 200)
        # # 将画家画好的图形展示在picture上
        # label.setPicture(pic)

        # 展示动图
        label.setScaledContents(True)
        movie = QMovie("gif路径")
        label.setMovie(movie)
        movie.start()
        # 100证明是1倍速显示
        movie.setSpeed(100)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
