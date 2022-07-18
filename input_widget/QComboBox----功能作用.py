from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        cb = QComboBox(self)
        # 逐个添加内容，也可添加ICon
        # cb.addItem("xxx1")
        # cb.addItem("xxx2")
        # # 一次性添加几条内容,元组或者列表的形式都可以
        # cb.addItems(("1", "2", "3"))
        # # 指定位置插入内容,该索引位置添加条目
        # cb.insertItem(1, "qqq")
        # #cb.setItemIcon(2, QIcon("xxx.png"))
        # # 设置条目的图标、文本等
        # cb.setItemText(2, "社会")
        #
        # # 删除条目项
        # cb.removeItem(2)
        # cb.insertSeparator(2)
        #
        # print(QAbstractItemModel.__subclasses__())
        # cb.resize(100, 30)
        # # 创建模型
        # model = QStandardItemModel()
        # # 设置条目
        # item1 = QStandardItem("item1")
        # item2 = QStandardItem("item2")
        # item22 = QStandardItem("item22")
        # # 将一级item加入模型
        # item2.appendRow(item22)
        # model.appendRow(item1)
        # model.appendRow(item2)
        # # 将模型设置到控件中
        # cb.setModel(model)
        #
        # # 换成树状视图显示
        # cb.setView(QTreeView(cb))

        cb.addItems(["abc", "123", "456"])
        cb.addItem("src", {"name": "itlike"})
        btn = QPushButton(self)
        btn.move(100, 100)
        btn.setText("测试按钮")
        # 获取条目总数
        # btn.clicked.connect(lambda: print(cb.count()))
        # # 获取当前索引
        # btn.clicked.connect(lambda: print(cb.currentIndex()))
        # # 获取当前数据,{"name": "itlike"}，例如城市编码，作为附加数据不会被展示
        # btn.clicked.connect(lambda: print(cb.currentData()))
        # # 获取当前文本内容
        # btn.clicked.connect(lambda: print(cb.currentText()))
        # # 获取当前图标
        # btn.clicked.connect(lambda: print(cb.itemIcon(cb.currentIndex())))
        # # 获取最后一个条目的信息
        # # idx=默认值，不传递形参的情况下才会取默认值,clicked像外界传递一个布尔类型的参数，
        # btn.clicked.connect(lambda _, idx=cb.count()-1: print(cb.itemIcon(idx), cb.itemText(idx),
        #                                                    cb.itemData(idx)))
        # # 给按钮设置图标
        # btn.clicked.connect(lambda: btn.setIcon(cb.itemIcon(cb.currentIndex())))
        # 个数到达上限无法添加新的
        btn.clicked.connect(lambda: cb.addItem("it"))
        cb.setMaxCount(6)
        cb.setEditable(True)
        # 限制可见条目个数
        cb.setMaxVisibleItems(3)

        cb.setCompleter(QCompleter(["dahk", "jdao", "jiwe"]))

        # 仅用于与用户进行交互的情况,打印出文本内容
        cb.activated[str].connect(lambda val: print("条目被激活", val))

        # 当前选中索引发生改变时，打印出索引值，不同的参数导致
        cb.currentIndexChanged.connect(lambda val: print("当前索引发生改变", val))

        # 当前文本发生改变,文本框中内容是否发生改变，也会发射信号
        cb.currentTextChanged.connect(lambda val: print("当前文本发生改变", val))

        # 编辑的文本发生改变，文本框中内容是否发生改变
        cb.editTextChanged.connect(lambda val: print("当前编辑文本发生改变", val))

        # 高亮信号，光标停留在某个条目之上，就会获取高亮的信号
        cb.highlighted.connect(lambda val: print("高亮发生改变", val))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
