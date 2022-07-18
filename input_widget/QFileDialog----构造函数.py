from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog----构造函数的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton(self)
        btn.move(200, 200)
        btn.setText("选择文件")
        def test():
            fd = QFileDialog(self, "选择文件", "./", "All(*.*);; Images(*.jpg *.bmp);;python(*.py)")

            fd.fileSelected.connect(lambda file: print(file))
            # fd.setAcceptMode(QFileDialog.AcceptSave)
            # fd.setDefaultSuffix("txt")
            #fd.setFileMode(QFileDialog.Directory)
            #fd.setNameFilter("Img(*.jpg *.png)")
            fd.setNameFilters(["All(*.*)", "Images(*.jpg *.bmp)", "python(*.py)"])
            print("xxx")
            fd.show()
            fd.setLabelText(QFileDialog.FileName, "顺哥的文件")
            fd.setLabelText(QFileDialog.Accept, "顺哥的接受")
            fd.setLabelText(QFileDialog.Reject, "顺哥的拒绝")
            # 文件的类型，只在保存文件对话框，有个文件类型
            QFileDialog.FileType

        btn.clicked.connect(test)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
