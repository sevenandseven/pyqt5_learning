from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 一个关于对话框
        QMessageBox.about(self, "xx1", "xx2")
        # 关于qt的对话框
        QMessageBox.aboutQt(self, "we")
        # 关于疑问对话框,设置默认按钮为QMessageBox.Discard
        result = QMessageBox.question(self, "xx1", "xx2", QMessageBox.Ok | QMessageBox.Discard, QMessageBox.Discard)
        print(result, "xxx")
        return None
        mb = QMessageBox(self)
        #mb = QMessageBox(QMessageBox.Warning, "dade1", "<h2>修改内容</h2>", QMessageBox.Ok | QMessageBox.Discard, self)
        # 无法自动弹出，需要手动弹出,不管使用什么方法调用
        # 强行设置它是否是模态
        #mb.setModal(False)
        # 同setModal()效果相同,设置为非模态
        mb.setWindowModality(Qt.NonModal)
        # 它都是一个窗口级别的模态对话框
        # 设置窗口
        mb.setWindowTitle("消息提示")
        # 设置标准图标信息
        mb.setIcon(QMessageBox.Information)
        # 设置自定义图标信息
        mb.setIconPixmap(QPixmap("xxx.png").scaled(50, 50))
        # 设置主标题内容
        mb.setText("<h3>文件内容已经被修改</h3>")
        # 设置副标题
        mb.setInformativeText("<h4>内容已修改，是否保存</h4>")
        # 设置复选框
        mb.setCheckBox(QCheckBox("下次不再提示", mb))
        # 设置详情文本
        mb.setDetailedText("修改的内容是：给每一行代码加了分号")

        # 设置标准按钮
        mb.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # 添加自定义按钮
        btn = QPushButton("dw", mb)
        mb.addButton(btn, QMessageBox.YesRole)
        # 效果同上
        btn2 = mb.addButton("xx2", QMessageBox.NoRole)
        # 移除某一个按钮
        mb.removeButton(btn)

        # 设置默认按钮，默认那个按钮获取焦点
        mb.setDefaultButton(btn2)
        # 退出按钮，点击ESC激活的按钮
        mb.setEscapeButton(btn2)

        print(btn)
        print(btn2)

        # yes按钮对应的整型数据是
        yes_btn = mb.button(QMessageBox.Yes)
        no_btn = mb.button(QMessageBox.No)

        # 根据某个按钮获取按钮的角色
        role = mb.buttonRole(btn)

        if role == QMessageBox.YesRole:
            print("1")
        elif role == QMessageBox.NoRole:
            print("2")

        def test(btn):
            print(btn)
            if btn == btn2:
                print("点击了第2个按钮")
            else:
                print("点击了第1个按钮")


            if btn == yes_btn:
                print("点击了第2个按钮")
            else:
                print("点击了第1个按钮")

        # 按钮被点击会发出信号
        mb.buttonClicked.connect(test)
        mb.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
