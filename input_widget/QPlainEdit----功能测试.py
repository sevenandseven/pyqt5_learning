from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPlainEdit的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pte = QPlainTextEdit(self)
        pte.resize(300, 300)
        pte.move(100, 100)
        self.pte = pte
        #self.占位提示符()
        self.格式设置()
        self.pte.setCenterOnScroll(True)
        self.光标操作()

    def 自动换行(self):
        # 获取默认换行模式
        print(self.pte.lineWrapMode())
        # 不设置换行，
        self.pte.setLineWrapMode(QPlainTextEdit.NoWrap)

    def 格式设置(self):
        tcf = QTextCharFormat()
        tcf.setFontUnderline(True)
        tcf.setUnderlineColor(QColor(100, 200, 10))
        self.pte.setCurrentCharFormat(tcf)

    def 只读设置(self):
        self.pte.setReadOnly(True)
        self.pte.isReadOnly()

    def 占位提示符(self):
        # 请输入占位文本
        self.pte.setPlaceholderText("请输入你的个人信息")
        print(self.pte.placeholderText())

    def 覆盖模式(self):
        print(self.te.overwriteMode())
        self.pte.setOverwriteMode(True)
        print(self.pte.overwriteMode())

    def 块的操作(self):
        # 打印普通文本编辑器中现有的块的个数
        # 文本编辑器中有一个默认的文本框
        print(self.pte.blockCount())
        # 设置最大块的个数,完全删除了之前的内容
        self.pte.setMaximumBlockCount(3)

    def 文本操作(self):
        # 会替换原来的文本
        self.pte.setPlainText("itlike.com")
        self.pte.insertPlainText("itlike")
        self.pte.appendPlainText("<a href='https://www.itlike.com'>撩课</a>")
        # 不支持表格等富文本,2行3列
        table_str = "<table border=2>" \
                    "<tr><td>1</td><td>2</td><td>3</td></tr>" \
                    "<tr><td>4</td><td>5</td><td>6</td></tr>" \
                    "<table>"
        # 获取整个文本框中的文本
        print(self.pte.toPlainText())

    def Tab控制(self):
        self.pte.setTabChangesFocus(True)

    def 放大缩小(self):
        # 放大,存放一个小于0的数是缩小功能
        self.te.zoomIn(10)
        # 缩小
        self.te.zoomOut(10)

    def 滚动保证光标可见(self):
        # 尽可能保证光标所在的哪一行
        # 光标所在的哪一行滚动到中间位置
        #self.pte.centerCursor()
        self.pte.ensureCursorVisible()
        self.pte.setFocus()

    def 光标操作(self):
        tc = self.pte.textCursor()
        # 无任何效果，因为普通文本编辑器不支持富文本编辑
        # tc.insertImage(r"D:\Desktop\OIP-C.jpg")
        # tc.insertTable(5, 6)
        # 光标跳转到指定位置，就近选择文本
        tc = self.pte.cursorForPosition(QPoint(100, 60))
        print(tc)
        tc.insertText("itlike")
        # self.pte.setCursorWidth(20)
        # self.pte.setFocus()
        # 移动到文档的末尾,要一个选中效果
        self.pte.moveCursor(QTextCursor.End, QTextCursor.KeepAnchor)

    def 信号的操作(self):
        # self.pte.textChanged.connect(lambda: print("内容发生了改变"))
        # self.pte.cursorPositionChanged.connect(lambda: print("光标位置发生改变"))
        # self.pte.blockCountChanged.connect(lambda bc: print("块的个数发生改变", bc))

        # self.pte.selectionChanged.connect(lambda: print("选中的内容发生了改变",
        #                                                 self.pte.textCursor().selectedText()))
        # 他会像外界传递一个参数,输入内容，文本从未修改变为修改
        # self.pte.modificationChanged.connect(lambda val: print("修改状态发生了改变",val))
        # 获取文本文档对象
        # doc = self.pte.document()
        # # 修改设置编辑状态，改变编辑状态
        # # 通过这种方法提示文件是否需要带*
        # doc.setModified(False)

        self.pte.updateRequest.connect(lambda rect, dy: print("内容区域更新", rect, dy))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
