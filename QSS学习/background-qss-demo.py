from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("案例的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 窗口控件内部的所有按钮都设置为相同的背景和颜色
        self.setStyleSheet("""
            QPushButton {
                backgroun-image:url(../source/puke.png);
                border:20px double red;
                background-origin:content;
                background-clip:padding;
                padding-left:-50px;
                padding-top:-68px;   
            } 
        """)
        h_layout = QHBoxLayout(self)
        for i in range(0, 13):
            btn = QPushButton(self)
            # 按钮的尺寸改为只能显示一张牌
            btn.setFixedSize(86, 108)
            # 将按钮的背景设置为某一张扑克牌
            # 把背景图片的移动和padding关联起来
            # 展示多个扑克牌，需要计算参数
            btn.setStyleSheet("""
            QPushButton {
                padding-left:-%dpx;
                padding-top:-%dpx;   
            } 
            """%(i * 49, 0))
            h_layout.addWidget(btn)
    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
