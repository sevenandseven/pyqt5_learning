from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("父子关系的学习")
window.resize(500, 500)

label1 = QLabel(window)
label1.setText("标签1")
label2 = QLabel(window)
label2.setText("标签2")
label2.move(50, 50)

# 查看某一个控件的父控件
print(label2.parentWidget())
label3 = QLabel(window)
label3.setText("标签3")
label3.move(100, 100)

# 查看（55，55）位置是否有子控件
print(window.childAt(55, 55))

# 查看所有控件组成的边界矩形
print(window.childrenRect())
window.show()
sys.exit(app.exec_())