from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLCDNumber的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 5表示最终所能展示的位数是5位
        lcd = QLCDNumber(self)

        # 设置限制位数
        lcd.setDigitCount(2)
        lcd.move(0, 0)
        lcd.resize(300, 100)
        # 展示字符串
        lcd.display("12345")
        # 展示数值类型数据
        lcd.display(10)
        # 以2进制的格式展示数据
        #lcd.setMode(QLCDNumber.Bin)

        lcd2 = QLCDNumber(self)
        lcd2.move(0, 100)
        lcd2.resize(300, 100)
        lcd3 = QLCDNumber(self)
        lcd3.move(0, 200)
        lcd3.resize(300, 100)

        # btn = QPushButton(self)
        # btn.move(100, 100)
        # btn.resize(100, 30)
        # btn.setText("测试按钮")
        # btn.clicked.connect(lambda: print(lcd.value()))
        #
        # print(lcd.checkOverflow(100))
        # print(lcd.checkOverflow(98))
        lcd.setSegmentStyle(QLCDNumber.Outline)
        lcd2.setSegmentStyle(QLCDNumber.Filled)
        lcd3.setSegmentStyle(QLCDNumber.Flat)

        # 先连接信号，在展示，否则溢出之后并无法传递信号
        lcd.overflow.connect(lambda: print("数值溢出"))
        lcd.display(200)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
