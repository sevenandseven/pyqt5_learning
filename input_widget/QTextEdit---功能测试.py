from PyQt5.Qt import *

class MyTextEdit(QTextEdit):
    # 重写鼠标操作事件
    def mousePressEvent(self, me):
        print(me.pos())
        # 获取坐标点位置所对应的锚点
        link_str = self.anchorAt(me.pos())
        if len(link_str) > 0:
            # 通过某一个方法打开对应的地址
            QDesktopServices.openUrl(QUrl(link_str))

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        te = MyTextEdit("xxxxx", self)
        self.te = te
        te.move(50, 50)
        te.resize(300, 300)
        te.setStyleSheet("background-color:cyan;")
        # 调用占位文本提示的方法
        # self.占位文本的提示()
        # self.文本内容的设置()

        # 设置锚点的名字'lk'
        #te.insertHtml("xxx"*100 + "<a name='lk' href='#itlike'>撩课</a>" + "aaa"*200)
        te.insertHtml("xxx" * 30 + "<a href='http://www.itlike.com'>撩课</a>" + "aaa" * 200)

        test_btn = QPushButton(self)
        test_btn.move(10, 10)
        test_btn.setText("按钮")
        test_btn.clicked.connect(self.btn_pressed)
        # self.btn_test()

    def btn_pressed(self):
        # self.te.setText("")
        # self.te.clear()
        #self.光标插入内容()
        #self.格式设置与合并()
        #self.内容和格式的获取()
        #self.文本选中和清空()
        #self.自动格式化()
        #self.字体设置()
        self.滚动到锚点()

    def 打开超链接(self):
        # 通过给定一个点坐标，返回对应锚点的位置
        # 监听鼠标点击事件，如果类中没有对应功能的方法
        # 可以选择重写该方法
        pass


    def Tab功能测试(self):
        # tab键功能设置为切换焦点
        self.te.setTabChangesFocus(True)
        # 打印制表符的距离
        print(self.te.tabStopWidth())
        # 改变制表符的距离
        self.te.setTabStopWidth(100)

    def 只读设置(self):
        self.te.setReadOnly(True)

    def 滚动到锚点(self):
        self.te.scrollToAnchor("lk")

    def 常用编辑操作(self):
        # 复制选中文本
        # self.te.copy()
        # self.te.paste()
        # 选中所有内容
        self.te.selectAll()
        self.te.setFocus()
        # 查找方法会匹配编译器中的所有内容
        # 不加参数，从左往右匹配
        # 从右往左查找,切区分大小写，仅仅是一个单独的单词，否则就不要
        self.te.find("xx", QTextDocument.FindBackward | QTextDocument.FindCaseSensitively)

    def 字符设置(self):
        # 设置字符格式
        tcf = QTextCharFormat()
        tcf.setFontFamily("宋体")
        # 设置首字母大写
        tcf.setFontCapitalization(QFont.Capitalization)
        tcf.setForeground(QColor(100, 10, 200))
        self.te.setCurrentCharFormat(tcf)

        tcf2 = QTextCharFormat()
        tcf2.setFontOverline(True)
        # 设置为新的格式
        self.te.setCurrentCharFormat(tcf2)
        # 合并两种格式
        self.te.mergeCurrentCharFormat(tcf2)

    def 颜色设置(self):
        # 设置字体背景颜色
        self.te.setTextBackgroundColor(QColor(200, 20, 20))
        # 设置字体颜色
        self.te.textColor(QColor(10, 200, 20))

    def 字体设置(self):
        # 直接弹出选择字体对话框
        # QFontDialog().getFont()
        # # 将光标之后的字体转换为要求的格式
        # # 或者选中字体转换为要求的格式
        # self.te.setFontFamily("幼圆")
        # self.te.setFontPointSize(10)
        # # 设置字体的粗细
        # self.te.setFontWeight(QFont.Black)
        # # 字体倾斜
        # self.te.setFontItalic(True)
        # # 字体加上下划线
        # self.te.setFontUnderline(True)
        font = QFont()
        font.setStrikeOut(True)
        self.te.setCurrentFont(font)

    def 对齐方式(self):
        # 仅仅为设置当前段落的对齐方式
        self.te.setAlignment(Qt.AlignCenter)

    def 光标设置(self):
        if self.te.overwriteMode():
            self.te.setOverwriteMode(False)
            self.te.setCursorWidth(1)
        else:
            self.te.setOverwriteMode(True)
            self.te.setCursorWidth(10)

        # 获取光标矩形(x,y,宽，高)
        print(self.te.cursorRect(self.te.textCursor()))

    def 覆盖模式的设置(self):
        # 设置覆盖模式
        self.te.setOverwriteMode(True)
        # 判断当前是否属于覆盖模式
        print(self.te.overwriteMode())

    def 软换行模式(self):
        # 取消软换行模式，产生水平滚动条
        self.te.setLineWrapMode(QTextEdit.NoWrap)
        # 填充像素宽度,指定一个宽度，超过之后，不能往下走
        # 结合另一个方法同时使用
        self.te.setLineWrapMode(QTextEdit.FixedPixelWidth)
        # 数据的含义代表setLineWrapMode参数中的枚举值（像素宽、列宽等）
        self.te.setLineWrapMode(100)

        # 软换行过程中保持单词的形状，设置单词软换行的格式(保持单词的完整性)
        self.te.setWordWrapMode(QTextOption.WordWrap)

    def 自动格式化(self):
        # 自动创建一个项目列表
        self.te.setAutoFormatting(QTextEdit.AutoBulletList)

    def 开始和结束操作(self):
        tc = self.te.textCursor()

        tc.beginEditBlock()
        tc.insertText("123")
        # 插入空白文本段
        tc.insertBlock()
        tc.insertText("456")
        tc.insertBlock()
        tc.endEditBlock()

        tc.insertText("789")
        tc.insertBlock()

    def 位置相关(self):
        tc = self.te.textCursor()
        print("光标是否在段落结尾：",tc.atBlockEnd())
        print("光标是否在段落开始：", tc.atBlockStart())
        print("光标是否在文档结尾：", tc.atEnd())
        print("光标是否在文档的开始：", tc.atStart())

        print("光标在第几列：", tc.columnNumber())
        print("光标位置：", tc.position())
        print("光标在文本块中的位置：", tc.positionInBlock())

    def btn_test(self):
        # 获取文本文档
        print(self.te.document())
        # 获取文本光标对象，该方法是QTextEdit()中的方法
        print(self.te.textCursor())

    def 文本字符的删除(self):
        tc = self.te.textCursor()
        # 删除光标的后一个字符
        tc.deleteChar()
        # 删除光标的后一个字符
        tc.deletePreviousChar()
        self.te.setFocus()

    def 文本的其他操作(self):
        tc = self.te.textCursor()
        # 删除选中文本（列表中的文本内容也可以被删除）
        tc.removeSelectedText()
        print(tc.hasSelection())
        return None

        tc.clearSelection()
        self.te.textCursor(tc)
        self.te.setFocus()
        return None

        # 输出选中文本的光标选中起始位置
        print(tc.selectionStart())
        # 输出选中文本的光标选中结束位置
        print(tc.selectionEnd())

    def 文本选中内容和获取(self):
        tc = self.te.textCursor()
        print(tc.selectedText())
        # 返回一个类对象值
        print(tc.selection())
        # 返回文本内容
        print(tc.selection().toPlainText())

    def 文本选中和清空(self):
        tc = self.te.textCursor()
        # 移动选项操作：移动到行首、移动的模式：保持锚点不动
        tc.select(QTextCursor.BlockUnderCursor)
        # tc.setPosition(QTextCursor.StartOfLine, QTextCursor.KeepAnchor, 1)
        self.te.setTextCursor(tc)
        return None

        tc = self.te.textCursor()
        # 移动选项操作：移动到行首、移动的模式：保持锚点不动
        tc.setPosition(QTextCursor.Up, QTextCursor.KeepAnchor, 1)
        # tc.setPosition(QTextCursor.StartOfLine, QTextCursor.KeepAnchor, 1)
        self.te.setTextCursor(tc)
        return None

        # 从光标的初始位置选中到移动位置
        tc.setPosition(6, QTextCursor.KeepAnchor)
        # 位置信息需要反向设置回给，文本编辑器的文本光标对象
        self.te.setTextCursor(tc)
        self.te.setFocus()

    def 内容和格式的获取(self):
        tc = self.te.textCursor()
        # 输出文本光标所在的段落
        print(tc.block())
        # 输出光标所在段落的文本
        print(tc.block().text())
        # 获取段落编号(段落编号从0开始)
        print(tc.blockNumber())
        # 获取当前文本列表的个数,不存在文本列表的情况返回None
        print(tc.currentList().count())

    def 格式设置与合并(self):
        # 格式的合并
        tc = self.te.textCursor()
        tcf = QTextCharFormat()
        tcf.setFontFamily("隶书")
        tcf.setFontPointSize(30)
        tcf.setFontOverline(True)
        tcf.setFontUnderline(True)
        tc.setCharFormat(tcf)

        tcf2 = QTextCharFormat()
        # 设置一个删除线
        tcf2.setFontStrikeOut(True)
        #tc.setCharFormat(tcf2)
        # 在之前老的字符格式的基础上在合并新的格式
        tc.mergeCharFormat(tcf2)
        return None

        # 设置字符格式,需要先选中字符，才会将格式应用于字符上
        tc = self.te.textCursor()
        tcf = QTextCharFormat()
        tcf.setFontFamily("隶书")
        tcf.setFontPointSize(30)
        tcf.setFontOverline(True)
        tcf.setFontUnderline(True)
        tc.setCharFormat(tcf)
        return None

        tc = self.te.textCursor()
        # 设置整个块的格式(一个段落)
        tbf = QTextBlockFormat()
        tbf.setAlignment(Qt.AlignCenter)
        tbf.setIndent(2)
        tc.setBlockFormat(tbf)
        return None

        tc = self.te.textCursor()
        # 当前块内的所有字体格式
        tcf = QTextCharFormat()
        tcf.setFontFamily("隶书")
        tcf.setFontPointSize(30)
        tcf.setFontOverline(True)
        tcf.setFontUnderline(True)
        # 设置块内字符格式
        tc.setBlockCharFormat(tcf)

    def 光标插入内容(self):
        # 文本光标对象
        tc = self.te.textCursor()
        # 设置边框对象
        tff = QTextFrameFormat()
        # 设置边框有10个像素
        tff.setBorder(10)
        # 设置边框颜色
        tff.setBorderBrush(QColor(25, 59, 19))
        # 文本框架离右侧的间距
        tff.setRightMargin(20)
        # 获取文档对象
        doc = self.te.document()
        # 获得文档框架对象,大的文档框架、小的文本框架
        root_frame = doc.rootFrame()
        root_frame.setFrameFormat(tff)
        # 插入文本框
        tc.insertFrame(tff)
        return None

        # 设置段落级别的格式，需要借助类QTextBlockFormat类
        tbf = QTextBlockFormat()
        # 设置文本内容右对齐、右间距为100
        tbf.setAlignment(Qt.AlignRight)
        tbf.setRightMargin(100)
        # 设置字符级别的格式，QTextCharFormat
        tcf = QTextCharFormat()
        tcf.setFontFamily("隶书")
        # 设置是否倾斜
        tcf.setFontItalic(True)
        tcf.setFontPointSize(20)
        # 插入文本块，插入空的文本块，即插入换行
        tc.insertBlock(tbf, tcf)
        # 捕捉焦点
        self.te.setFocus()
        return None

        # tc.insertTable(5,3)
        # 创建格式对象,设置单元格格式
        ttf = QTextTableFormat()
        # 右对齐
        ttf.setAlignment(Qt.AlignRight)
        # 内边距设置
        ttf.setCellPadding(6)
        # 外边距
        ttf.setCellSpacing(4)
        # 设置行宽
        ttf.setColumnWidthConstraints((QTextLength(QTextLength.PercentageLength, 50),
                                       QTextLength(QTextLength.PercentageLength, 40),
                                       QTextLength(QTextLength.PercentageLength, 10)))

        # 返回值为一个文本表格对象
        table = tc.insertTable(5,3, ttf)
        # table对象还包含其他方法（追加行、插入行等功能）
        #table.appendColumns(3)

        return None
        # t1 = tc.insertList(QTextListFormat.ListCircle)
        # 方式一通过枚举类型创建列表
       # t1 = tc.insertList(QTextListFormat.ListDecimal)
       #  t2 = tc.createList(QTextListFormat.ListDecimal)

        # 方式二,通过创建对象创建列表
        tlf = QTextListFormat()
        # 设置缩进,3个Tab键
        tlf.setIndent(3)
        # 设置前缀
        tlf.setNumberPrefix("<<")
        # 设置后缀
        tlf.setNumberSuffix(">>")
        # 设置样式,显示前后缀需要列表的（左侧图标为数字）
        tlf.setStyle(QTextListFormat.ListDecimal)
        tt = tc.createList(tlf)
        return None
        # # 创建...对象（通过使用构造函数创建、或者通过类中的方法创建（类名调用方法））
        # tdf = QTextDocumentFragment.fromHtml("<h1>xxxxxsvl</h1>")
        # tc.insertFragment(tdf)
        # # 创建格式对象
        # tif = QTextImageFormat()
        # # 设置图片名称
        # tif.setName("xxx.png")
        # tif.setWidth(100)
        # tif.setHeight(100)
        # # 向左向右浮动，已被弃用
        # tc.insertImage(tif)
        # tc.insertImage(tif,QTextFrameFormat.FloatRight)
        # # 或者直接插入图片字符串（即路径）
        # tc.insertImage("xxx.png")
        return None
        # 创建文本字符格式对象
        tcf = QTextCharFormat()
        tcf.setToolTip("撩课学院网址")
        # 设置背景颜色
        # 设置字体家族
        tcf.setFontFamily("隶属")
        # 设置字体大小
        tcf.setFontPointSize(66)
        # 首先获取文本光标对象
        tc = self.te.textCursor()
        tc.insertText("itlike.com", tcf)
        # 写一个超链接,显示的两个撩课字体就是超链接
        tc.insertHtml("<a href='http://www.itlike.com'> 撩课</a>")

    def 文本内容的设置(self):
        # 设置普通文本,会清空旧的内容，然后再设置新的
        self.te.setPlainText("<h1>xxx</h1>")
        # 在旧的内容的基础上添加新的内容
        self.te.insertPlainText("<h1>xxx</h1>")
        print(self.te.toPlainText())
        # 富文本的操作
        self.te.setHtml("<h1>xxx</h1>")
        # 插入二级标题,每级标题字体大小不一样
        self.te.insertHtml("<h2>oxja</h2>")
        # 自动识别出HTML富文本标签
        self.te.setText("<h1>xxx</h1>")
        # 追加在所有文本内容之后、且会自动识别富文本
        self.te.append("<h3>fdsrex</h3>")

    def 占位文本的提示(self):
        self.te.setPlaceholderText("请输入你的个人简历")
        print(self.te.placeholderText())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
