from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("级联和冲突的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn1 = QPushButton("b1", self)
        btn2 = QPushButton("b2", self)
        btn1.move(100, 100)
        btn2.move(200, 200)
        # 设置id
        btn1.setObjectName("b1")
        btn2.setObjectName("b2")

        self.setStyleSheet("""
            QPushButton{
                color:red;
            }
            QPushButton#b1{
                color:orange;
            }
        """)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
