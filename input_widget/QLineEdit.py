import sys
from PyQt5.Qt import *

# 做成活动模块，修改方便
# 1、创建应用程序,可以传递参数给app，通过命令行输入参数
app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("QLineEdit---功能测试")
window.resize(500, 500)

# 设置文本编辑器,设置字符串会自动将内容补充到输入文本之前
# 所以字符串会自动调用设置文本的构造函数
le = QLineEdit("sz:", window)
# 文本的设置与获取
le.setText("lobe")
print(le.text())
# 插入文本，默认插入到光标之后
le.insert("2718")

# 使用按钮控制文本内容
btn = QPushButton(window)
btn.move(100, 100)
btn.setText("按钮")
# 插入文本
#btn.pressed.connect(lambda: le.insert("44"))
# 获取文本内容并输出
#btn.pressed.connect(lambda : print(le.text()))
# # 展示文本内容
btn.pressed.connect(lambda : print(le.displayText()))

window.show()
sys.exit(app.exec_())
