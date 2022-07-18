from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressMessage的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        #pd = QProgressDialog(self)
        # 多个参数设置
        pd = QProgressDialog("dja", "diw", 0, 100, self)
        # 设置最小显示时长为0，则任何情况都会弹出该对话框
        pd.setMinimum(0)
        # 去掉自动关闭功能
        pd.setAutoClose(False)
        # 去掉自动重置功能
        pd.setAutoReset(False)
        # 设置当前进度值为50%
        #pd.setValue(50)
        # 非模态对话框显示窗口
        pd.show()
        # 设置标签文本
        pd.setLabelText("进度展示")
        # 设置取消按钮文本
        pd.setCancelButtonText("取消")
        # 设置进度条范围
        pd.setRange(0, 100)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
