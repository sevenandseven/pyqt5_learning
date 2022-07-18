from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QInputDialog的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 顶层窗口外观标志
        # 创建一个没有边框的输入对话框
        input_d = QInputDialog(self, Qt.FramelessWindowHint)
        # 设置模式,选择什么样的控件展示item
        #input_d.setOption(QInputDialog.UseListViewForComboBoxItems)
        # 设置下拉列表
        input_d.setComboBoxItems(["1", "2", "3"])

        input_d.setLabelText("请输入你的姓名：")
        input_d.setOkButtonText("好的")
        input_d.setCancelButtonText("我想取消")
        input_d.setInputMode(QInputDialog.DoubleInput)
        input_d.setDoubleRange(-199, 199)

        input_d.setComboBoxItems(["1", "2", "3"])
        input_d.setComboBoxEditable(True)
        input_d.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
