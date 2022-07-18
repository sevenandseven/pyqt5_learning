from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog----信号的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton(self)
        btn.move(200, 200)
        btn.setText("选择文件")

        def test():
            fd = QFileDialog(self, "选择一个文件", "./", "All(*.*);;Images(*.jpg *.png);; python文件(*.py)")
            fd.show()
            #fd.setFileMode(QFileDialog.Directory)
            # 系统从内部向外界发射信号时，是由他决定，与槽函数的顺序无关
            # fd.currentChanged.connect(lambda path: print("当前路径字符串发生改变时", path))
            # fd.currentUrlChanged.connect(lambda url: print("当前路径URL发生改变时", url))
            # 打开选中文件夹时发射的信号
            # fd.directoryEntered.connect(lambda path: print("当前目录字符串进入时", path))
            # fd.directoryUrlEntered.connect(lambda url: print("当前目录URL进入时", url))
            # fd.filterSelected.connect(lambda filter: print("当前名称过滤字符串被选中时", filter))

            fd.setFileMode(QFileDialog.ExistingFiles)
            fd.fileSelected.connect(lambda val: print("单个文件被选中---字符串", val))
            fd.filesSelected.connect(lambda val: print("多个文件被选中---列表[字符串]", val))
            fd.urlSelected.connect(lambda val: print("单个文件被选中---url", val))
            fd.urlsSelected.connect(lambda val: print("多个文件被选中---url", val))

        btn.clicked.connect(test)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
