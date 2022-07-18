from PyQt5.Qt import *

# 重写，意味着子类化控件类别
class SB(QSpinBox):
    # 改变控件内部的数值，会调用该方法,将数值传给你，得到字符串
    # 只修改了展示层面
    def textFromValue(self,p_int):
        print(p_int)
        # 1*1，做一个拼接
        return str(p_int) + "*" + str(p_int)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSpinBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 直接创建控件会限制范围（0-99）,且不能输入非数字的其他字符
        sb = QSpinBox(self)
        self.sb = sb
        sb.resize(100, 25)
        sb.move(100, 100)
        # 显示那种类型的数据通过[]选择
        sb.valueChanged[str].connect(lambda val: print(type(val), val))

        test_btn = QPushButton(self)
        test_btn.setText("测试按钮")
        test_btn.move(150, 150)
        test_btn.clicked.connect(lambda: self.前缀和后缀())

        # self.最大值最小值()
        # self.数值循环()

    def 最大值最小值(self):
        # 设置步长调节器的最大值
        self.sb.setMaximum(180)
        print(self.sb.maximum())
        # 设置步长调节器的最小值
        self.sb.setMinimum(18)
        # 最大值和最小值都可以取到
        self.sb.setRange(18, 180)

    def 前缀和后缀(self):
        # self.sb.setRange(1, 12)
        # self.sb.setSuffix("月")
        self.sb.setRange(0, 6)
        self.sb.setPrefix("周")
        self.sb.setSpecialValueText("周日")

    def 步长设置(self):
        # 3个3个的跳
        self.sb.setSingleStep(3)

    def 数值循环(self):
        print(self.sb.wrapping())
        self.sb.setWrapping(True)
        print(self.sb.wrapping())

    def 设置以及获取数值(self):
        # 获取数据,只能获取数据（指数值部分），不能获得前后缀
        print(self.sb.value())
        # 获取单行文本框中的内容,可以获得所有内容
        print(self.sb.lineEdit().text())
        self.sb.setRange(0, 9)
        self.sb.prefix("撩课")
        # 设置数值超过给定范围，会按照最大值或者最小值设定
        self.sb.setValue(66)

    def 显示进制数(self):
        # 以二进制的方式显示文本框数据
        self.sb.setDisplayIntegerBase(2)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
