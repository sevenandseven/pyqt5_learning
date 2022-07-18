from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 标签添加快捷方式
        name_label = QLabel("姓名(&n)：")
        age_label = QLabel("年龄(&g)：")

        name_le = QLineEdit()
        # 旋转步长调节器
        age_le = QSpinBox()
        sex_label = QLabel("性别")
        # 设置小伙伴
        name_label.setBuddy(name_le)
        age_label.setBuddy(age_le)


        # 两个单选按钮
        male_rb = QRadioButton("男")
        female_rb = QRadioButton("女")
        h_layout = QHBoxLayout()
        h_layout.addWidget(male_rb)
        h_layout.addWidget(female_rb)

        submit_btn = QPushButton("提交")

        fl = QFormLayout()
        self.setLayout(fl)
        # 打印控件的位置信息
        print(fl.getWidgetPosition(name_label))
        # fl.addRow(name_label, name_le)
        # # fl.addRow("姓名(&n)", name_le)
        # # fl.addRow("年龄(&g)", age_le)
        # fl.addRow(sex_label, h_layout)
        # fl.addRow(age_label, age_le)
        # fl.addRow(submit_btn)
        #
        # fl.insertRow(1, submit_btn)

        # # 打印当前行的总行数
        # print(fl.rowCount())
        # # 获取年龄后对应的步长调节器的位置信息
        # print(fl.getWidgetPosition(age_le))
        # # 获取布局信息
        # print(fl.getLayoutPosition(h_layout))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
