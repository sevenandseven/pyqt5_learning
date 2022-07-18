from PyQt5.Qt import *

# 子类化控件类别
class MyASB(QAbstractSpinBox):
    # 定义值，不传值的情况下就指默认值
    def __init__(self, parent=None, num=0, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.lineEdit().setText(num)

    def stepEnabled(self):
        # 0--9
        # current_num = int(self.text())
        # if current_num == 0:
        #     return QAbstractSpinBox.StepUpEnabled
        # elif current_num == 9:
        #     return QAbstractSpinBox.StepDownEnabled
        # elif current_num < 0 or current_num > 9:
        #     return QAbstractSpinBox.StepNone
        # else:
        return QAbstractSpinBox.StepDownEnabled | QAbstractSpinBox.StepUpEnabled

    def stepBy(self, p_int):
        #print(p_int)
        current_num = int(self.text()) + p_int
        # 步长调节器包含几个子控件，其中一个就是单行文本调节器
        self.lineEdit().setText(str(current_num))

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractSpinButton的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        asb = MyASB(self, "6")
        self.asb = asb
        asb.resize(100, 30)
        asb.move(100, 100)
        self.asb.editingFinished.connect(lambda: print("结束编辑"))

        # 设置加速
        # asb.setAccelerated(True)
        # asb.setReadOnly(True)
        test_btn = QPushButton(self)
        test_btn.move(200, 200)
        test_btn.setText("测试按钮")
        test_btn.clicked.connect(self.btn_test)

    def btn_test(self):
        # print(self.asb.text())
        # self.asb.lineEdit().setText("88")
        # # 获取单行文本编辑器
        # # 创建提示框
        # cl = QCompleter(["sz", "123", "18"], self.asb)
        # # 单行文本编辑器的很多操作都可以使用
        # self.asb.lineEdit().setCompleter(cl)
        # self.asb.lineEdit().setAlignment(Qt.AlignRight)
        # # 边框格式
        # self.asb.setFrame(True)
        # # 清空
        # self.asb.clear()
        # 设置右侧按钮格式，可以通过键盘上的上下键改变文本
        self.asb.setButtonSymbols(QAbstractSpinBox.NoButtons)

    # 验证器
    def validate(self, p_str, p_int):
        # 18-180
        num = int(p_str)
        if num < 18:
            return (QValidator.Intermediate, p_str,p_int)
        elif num < 180:
            return (QValidator.Acceptable, p_str,p_int)
        else:
            return (QValidator.Invalid, p_str,p_int)

    # 修复功能
    def fixup(self, p_str):
        print(p_str)
        return "18"

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
