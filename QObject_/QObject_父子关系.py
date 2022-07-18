from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QT学习")
        self.resize(500, 500)
        #self.QObject_name_property()
        #self.QObject对象父子关系()
        self.manage_memory()

    def QObject_name_property(self):
        # 读取字符串
        with open("QObject.qss", "r") as f:
            # 读取到的字符串全部应用到应用程序对象里的所有控件
            qApp.setStyleSheet(f.read())

        # 设置标签放置位置,给该对象上创建标签
        label = QLabel(self)
        label.setObjectName("notice")
        label.setText("QT_learning")

        label2 = QLabel(self)
        label2.move(100, 100)
        label2.setObjectName("notice")
        # 通过设置属性完成不同的样式
        label2.setProperty("notice_level", "warning")
        label2.setText("learing good")
        # 设置一个样式表，可以设置标签的样式
        # label.setStyleSheet("font-size:10pt; color:red")

    def QObject对象父子关系(self):
        # 创建一个对象
        obj0 = QObject()
        obj1 = QObject()
        obj2 = QObject()
        obj3 = QObject()
        obj4 = QObject()
        obj5 = QObject()

        # label = QLabel()
        # label.setParent(obj0)

        print("obj0", obj0)
        print("obj1", obj1)
        print("obj2", obj2)
        print("obj3", obj3)
        print("obj4", obj4)
        print("obj5", obj5)

        obj1.setParent(obj0)
        # 将obj2设置为obj1的父对象
        #obj1.setParent(obj2)
        obj2.setParent(obj0)
        obj2.setObjectName("2")

        obj3.setParent(obj1)
        obj3.setObjectName("3")
        obj4.setParent(obj2)
        obj5.setParent(obj2)

        # 测试一下4的父对象
       # print(obj4.parent())

        # 输出他的所有的 直接子对象，只有一级
       # print(obj2.children())

        # 指定某一个类型，或者类型元组,
        # 查找子对象中的QLable类型或者其他类型,只需找到一个就可以结束
        #print(obj0.findChild(QLabel))
        print(obj0.findChild(QObject, "3", Qt.FindDirectChildrenOnly))

    # 内存管理机制
    def manage_memory(self):
        obj1 = QObject()
        # 将obj1作为self对象的属性，
        # 相当于有指针指向obj1对像，所以不会被自动释放
        self.obj1 = obj1
        obj2 = QObject()

        obj2.setParent(obj1)

        # 监听obj2对像被释放
        obj2.destroyed.connect(lambda : print("obj2对象被释放了"))

        del self.obj1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # window = Window()
    # window.show()

    # win1 = QWidget()
    # win1.setWindowTitle("红色")
    # win1.setStyleSheet("background-color: red")
    # win1.show()
    #
    # win2 = QWidget()
    # win2.setWindowTitle("绿色")
    # win2.setStyleSheet("background-color: green")
    # #win2.setParent(win1)
    # win2.resize(100, 100)
    # win2.show()

    win_root = QWidget()
    label1 = QLabel()
    label1.setText("label1")
    label1.setParent(win_root)

    label2 = QLabel()
    label2.move(50, 50)
    label2.setText("label2")
    label2.setParent(win_root)

    label3 = QLabel()
    label3.move(80, 80)
    label3.setText("label1")
    label3.setParent(win_root)

    btn = QPushButton(win_root)
    btn.move(100, 100)
    btn.setText("btn")
    win_root.show()

    # 遍历win_root中所有的子控件
    for sub_widget in win_root.findChildren(QLabel):
        print(sub_widget)
        sub_widget.setStyleSheet("background-color:cyan;")

    sys.exit(app.exec_())