import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("按钮的功能测试--自动重复")
window.resize(500, 500)

push_btn = QPushButton(window)
push_btn.setText("重复测试")
push_btn.move(100, 100)

# 设置按钮自动重复
radio_Button = QRadioButton(window)
radio_Button.setText("这是一个radio")
radio_Button.move(100, 150)

check_btn = QCheckBox(window)
check_btn.setText("这是checkbox")
check_btn.move(100, 200)

push_btn.setStyleSheet("QPushButton:pressed {background-color:red;}")

# 把三个按钮都置为按下状态
# push_btn.setDown(True)
# radio_Button.setDown(True)
# check_btn.setDown(True)

# 判断按钮是否可以被选中
# 设置为被选中状态
#push_btn.isChecked(True)
print(push_btn.isCheckable())
print(radio_Button.isCheckable())
print(check_btn.isCheckable())

# 设置按钮被选中
push_btn.setChecked(True)
radio_Button.setChecked(True)
check_btn.setChecked(True)

push_btn.toggle()
push_btn.setChecked(not push_btn.isChecked())

# 测试按钮的排他性
print(push_btn.autoExclusive())

# 设置为具有排他性的按钮
push_btn.setAutoExclusive(True)

window.show()
sys.exit(app.exec_())
