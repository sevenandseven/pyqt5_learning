from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QT学习")
        self.resize(500, 500)
        #self.QObject_name_property()
        #self.QObject对象父子关系()
        #self.manage_memory()
        #self.QObject_类型判断()
        self.QObject_类型判断案例()

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

    def QObject_信号与槽(self):
        self.obj = QObject()
        # 将obj对象里的信号与槽进行连接

        # def destory_cao(obj):
        #     print("对象被释放了", obj)
        #
        # # 当对象被释放就会发出destory信号,就会触发自定义槽函数
        # # destory信号可以像外界携带一个被释放的信号
        # self.obj.destroyed.connect(destory_cao)
        # del self.obj
        # name是最新发生改变的名字
        def obj_name_cao(name):
            print("对象名称发生了改变", name)

        def obj_name_cao2(name):
            print("对象名称发生了改变2", name)

        self.obj.objectNameChanged.connect(obj_name_cao)
        self.obj.objectNameChanged.connect(obj_name_cao2)

        # 错误例子，输入是一个字符串，而不是QT的信号类型
        # 当前信号连接的槽的个数
        #print(self.obj.receivers("objectNameChanged"))
        print(self.obj.receivers(self.obj.objectNameChanged))


        self.obj.setObjectName("xxx")
        # 取消信号与槽的连接，信号仍然会被触发发生，但信号与槽之间的关系被断开
        #self.obj.objectNameChanged.disconnect()

        # 获取信号是否被阻止，输出为false，表示并未被临时暂停
        print(self.obj.signalsBlocked())
        # 另外一种方法,代码表示临时阻断信号与槽的连接
        self.obj.blockSignals(True)
        # 输出为true，确实被临时暂停
        print(self.obj.signalsBlocked())

        self.obj.setObjectName("iiii")

        # 再次建立信号与槽的连接
        #self.obj.objectNameChanged.connect(obj_name_cao)

        # 恢复信号与槽的连接
        self.obj.blockSignals(False)
        print(self.obj.signalsBlocked())
        self.obj.setObjectName("dhiwab")

    def QObject_类型判断(self):
        Obj = QObject()

        w = QWidget()

        btn = QPushButton()

        label = QLabel()
        # 将四个对象放入列表
        objs = [Obj, w, btn, label]
        # 判定是否是控件类型
        for o in objs:
            # 判断是否是父类,那些是继承QWidegt类别
            print(o.inherits("QWidget"))
            #print(o.isWidgetType())

    def QObject_类型判断案例(self):
        label1 = QLabel(self)
        label1.setText("社会人")
        label1.move(100, 100)

        label2 = QLabel(self)
        label2.setText("头疼")
        label2.move(150, 150)
        btn = QPushButton(self)
        btn.setText("点我")
        btn.move(200, 200)

        # for widget in self.findChildren(QLabel):
        #     print(widget)

        for widget in self.children():
            # 会打印3个是，因为他们都是直接间接继承QWidget属于控件类别
            if widget.isWidgetType():
                print("是")

            # 方法2
            if widget.inherits("QLabel"):
                #print("是")
                widget.setStyleSheet("background-color:cyan;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())