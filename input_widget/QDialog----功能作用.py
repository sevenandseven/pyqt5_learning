from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QDialog")
window.resize(500, 500)

# 永远是顶层窗口
d = QDialog(window)
btn1 = QPushButton(d)
btn1.setText("btn1")
btn1.move(20, 20)
btn1.clicked.connect(lambda: d.accept())

btn2 = QPushButton(d)
btn2.setText("btn2")
btn2.move(60, 60)
btn2.clicked.connect(lambda: d.reject())
#btn2.clicked.connect(lambda: print(d.result()))

btn3 = QPushButton(d)
btn3.setText("btn3")
btn3.move(60, 160)
btn3.clicked.connect(lambda: d.done(8))
#btn3.clicked.connect(lambda: d.setResult(888))

d.accepted.connect(lambda: print("点击了，接受按钮"))
d.rejected.connect(lambda: print("点击了，拒绝按钮"))
d.accepted.connect(lambda val: print("点击了，完成按钮", val))

d.setWindowTitle("对话框")
d.resize(300, 300)
d.setWindowModality(Qt.WindowModal)
d.setSizeGripEnabled(True)
#d.show()
# 应用程序级别的模态对话框
# 通过不同的数值判断用户做的怎样的操作
result = d.exec()
print(result)

window.show()
sys.exit(app.exec_())
