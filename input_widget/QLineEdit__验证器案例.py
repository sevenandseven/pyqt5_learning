from PyQt5.Qt import *

class AgeValidator(QValidator):
    def validate(self, input_str, input_pos):
        print(input_str, input_pos)
        # 判断，结果字符串应该是由一些数字组成，return
        try:
            if 18 <= int(input_str) <= 180:
                return (QValidator.Acceptable, input_str, input_pos)
            elif 1 <= int(input_str) <= 17:
                return (QValidator.Intermediate, input_str, input_pos)
            else:
                return (QValidator.Invalid, input_str, input_pos)
        except:
            if len(input_str) == 0:
                return (QValidator.Intermediate, input_str, input_pos)
            return (QValidator.Invalid, input_str, input_pos)

    # 当处于非正常验证通过状态（通过或无效），在进行处理一遍
    def fixup(self, input_str):
        print("xxxx", input_str)
        try:
            if int(input_str) < 18:
                return "18"
            else:
                return "180"
        except:
            return "18"

class MyAgeValidator(QIntValidator):
    def fixup(self, p_str):
        print("xxxx", p_str)
        if len(p_str) == 0 or int(p_str) < 18:
            return "18"

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEdit的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        le = QLineEdit(self)
        le.move(100, 100)
        # 验证器要求输入年龄，且为18-88之间的数字
        # 创建一个QValidator类型的对象,抽象类不能直接使用，需要先进行实例化
        # 自定义一个类，继承QValidator
        #validator = AgeValidator()
        # 使用自带的方法，但他无法限定最小值
        #validator = QIntValidator(18, 180)

        # 自定义修复方法
        validator = MyAgeValidator(18, 180)
        le.setValidator(validator)
        # le2创建是为了使le结束编辑状态
        le2 = QLineEdit(self)
        le2.move(200, 200)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())