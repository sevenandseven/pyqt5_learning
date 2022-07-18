from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        #name_label = QLabel("姓名(&n)：")
        age_label = QLabel("年龄(&g)：")

        name_le = QLineEdit()
        # 旋转步长调节器
        age_le = QSpinBox()
        sex_label = QLabel("性别")
        # 设置小伙伴
        #name_label.setBuddy(name_le)
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

        fl.addRow("姓名(&n):", name_le)
        #fl.addRow(name_label, name_le)
        fl.addRow(sex_label, h_layout)
        fl.addRow(age_label, age_le)
        fl.addRow(submit_btn)

        # 判断控件是否被销毁
        age_le.destroyed.connect(lambda: print("年龄步长被释放"))
        age_label.destroyed.connect(lambda: print("年龄标签被释放"))
        # 移除某一行，删除控件
        #fl.removeRow(2)

        # 移除某一行，不删除控件,他仍然在父控件身上，有的控件有布局，有的控件没有局部，布局混乱
        #fl.takeRow(2)
        # 所以需要删除控件(或者隐藏)解决这个问题
        # age_le.hide()
        # age_label.hide()

        # print(fl.takeRow(2).labelItem.widget())
        # print(fl.takeRow(2).fieldItem.widget())

        #单独移除某一个控件，而不是某一行
        # fl.removeWidget(age_label)
        # # 彻底删除控件
        # fl.setParent(None)
        # 获取标签对象
        fl.labelForField(name_le).setText("ddd")

        # 行包装策略
        fl.setRowWrapPolicy(QFormLayout.WrapLongRows)
        fl.setRowWrapPolicy(QFormLayout.WrapAllRows)

        # 打印整个表单的对齐方式
        print(fl.formAlignment() == Qt.AlignRight | Qt.AlignTop)
        # 设置表单的对齐方式
        fl.setFormAlignment(Qt.AlignLeft | Qt.AlignBottom)
        # 标签对齐(参照最长的列宽对齐的)
        fl.setLabelAlignment(Qt.AlignRight)

        # 行跟行之间间距设大一点
        fl.setVerticalSpacing(60)
        # 设置水平方向的间距
        fl.setHorizontalSpacing(60)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
