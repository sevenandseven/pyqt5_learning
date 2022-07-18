import sys
from PyQt5.Qt import *

# 做成活动模块，修改方便
# 1、创建应用程序,可以传递参数给app，通过命令行输入参数
app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("QButtonGroup使用")
window.resize(500, 500)

# 创建四个单选按钮
r_male = QRadioButton("男", window)
r_female = QRadioButton("女", window)
r_male.move(100, 100)
r_female.move(100, 150)
# 男设置为默认选中按钮
r_male.setChecked(True)
# 创建按钮容器
sex_group = QButtonGroup(window)
# 设置每一个按钮的id，默认都是负数
sex_group.addButton(r_male, 1)
sex_group.addButton(r_female, 2)

r_yes = QRadioButton("是", window)
r_no = QRadioButton("否", window)
r_yes.move(300, 100)
r_no.move(300, 150)
answer_group = QButtonGroup(window)
answer_group.addButton(r_yes)
answer_group.addButton(r_no)
# 给每一个按钮设置ID
answer_group.setId(r_yes, 1)
answer_group.setId(r_no, 2)
# 获得每一个按钮的ID
print(answer_group.id(r_yes))
print(answer_group.id(r_no))
# 当输出值为-1表示未有按钮被选中
print(answer_group.checkedId())

# 删除组中的某一个按钮
sex_group.removeButton(r_male)
# 设置独占
sex_group.setExclusive(True)

# 查看按钮组中的按钮
print(sex_group.buttons())
# 获取组中某一个id的按钮
print(sex_group.button(2))
# 获取组中被选中的按钮
print(sex_group.checkedButton())

# 监听按钮组中的按钮切换信号
def test(val):
    print(val)
    print(sex_group.id(val))

sex_group.buttonToggled.connect(test)
# 传参数为int类型的信号，使用中括号,输出的val为他的id
#sex_group.buttonToggled[int].connect(test)
window.show()
sys.exit(app.exec_())
