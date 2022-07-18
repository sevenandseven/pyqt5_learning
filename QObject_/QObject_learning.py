from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject学习")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        #self.QObject_structure_test(self)
        self.QObject_name_property()

    def QObject_structure_test(self):
        #QObject.__subclasses__()
        # 获取他的父类
        mros = QObject.mro()
        for mro in mros:
            print(mro)

    def QObject_name_property(self):
        # 测试API
        obj = QObject()
        obj.setObjectName("notice")
        print(obj.objectName)

        obj.setProperty("notice_level", "error")
        obj.setProperty("notice_level2", "warning")

        print(obj.property("notice_level"))
        print(obj.dynamicPropertyNames())
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
