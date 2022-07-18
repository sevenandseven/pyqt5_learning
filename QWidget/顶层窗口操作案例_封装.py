from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 公共数据
        self.top_margin = 10
        self.btn_w = 80
        self.btn_h = 40

        # 设置窗口无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.9)
        # 设置控件
        self.setWindowTitle("顶层窗口操作案例")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        close_btn = QPushButton(self)
        # 将局部变量赋给该属性
        self.close_btn = close_btn
        close_btn.setText("关闭")
        close_btn.resize(self.btn_w, self.btn_h)
        # close_btn_w = close_btn.width()

        # def close():
        #     window.close()
        # close_btn.pressed.connect(close)

        def max_normal():
            if self.isMaximized():
                self.showNormal()
                max_btn.setText("最大化")
            else:
                self.showMaximized()
                max_btn.setText("恢复")

        # 设置最大化按钮
        max_btn = QPushButton(self)
        self.max_btn = max_btn
        max_btn.setText("最大化")
        max_btn.resize(self.btn_w, self.btn_h)

        mini_btn = QPushButton(self)
        self.mini_btn = mini_btn
        mini_btn.setText("最小化")
        mini_btn.resize(self.btn_w, self.btn_h)

        close_btn.pressed.connect(self.close)
        max_btn.pressed.connect(max_normal)
        mini_btn.pressed.connect(self.showMaximized)

    # 监听窗口尺寸大小的变化
    def resizeEvent(self, QResizeEvent):
        window_w = self.width()
        close_btn_x = window_w - self.btn_w
        close_btn_y = self.top_margin
        self.close_btn.move(close_btn_x, close_btn_y)

        max_btn_x = close_btn_x - self.btn_w
        max_btn_y = self.top_margin
        self.max_btn.move(max_btn_x, max_btn_y)

        mini_btn_x = max_btn_x - self.btn_w
        mini_btn_y = self.top_margin
        self.mini_btn.move(mini_btn_x, mini_btn_y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())