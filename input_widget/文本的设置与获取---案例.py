import sys
from PyQt5.Qt import *

# 做成活动模块，修改方便
# 1、创建应用程序,可以传递参数给app，通过命令行输入参数
app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("文本的设置与获取---案例")
window.resize(500, 500)
le_a = QLineEdit(window)
le_a.move(100, 200)
le_b = QLineEdit(window)
le_b.move(100, 300)
# # 设置输入文本的输出模式
# # 类型一QLineEdit.NoEcho是密文的格式，显示的是一个空白，无法看出长度、内容
# # 类型二Nomal普通模式、password密文的形式、passonecoedit是用户输入过程可以看到文本内容，完成之后则显示为密文
# le_b.setEchoMode(QLineEdit.NoEcho)
# print(le_b.echoMode())
copy_btn = QPushButton(window)
copy_btn.move(100, 400)
copy_btn.setText("复制")
# 监听按钮事件都可
# pressed是监听鼠标按下,clicked是监听鼠标按下并松开那一刻才会发射信号
def copy_text():
    print(le_b.isModified())
    # 将文本框内容设置为未修改状态
    le_b.setModified(False)

    # str = le_a.text()
    # le_b.setText(str)
    # # 方法二
    # le_b.setText("")
    # le_b.insert(str)
    # 获取文本的真实内容
    # print(le_b.text())
    # # 获取文本的显示内容、即用户看到的内容
    # print(le_b.displayText())

# 最大长度限制
le_a.setMaxLength(3)
# 获取最大长度
print(le_a.maxLength())
# 只读限制,不存在焦点
le_a.setReadOnly(True)
# 可以通过文本输入，但不能超过给定长度
le_a.setText("dhajkhf")

copy_btn.clicked.connect(copy_text)

# le_b设置掩码
# 总共输入5位，左边2（必须是大写字母）--- 右边2（必须是一个数字）
le_b.setInputMask(">AA-9A;#")

window.show()
sys.exit(app.exec_())
