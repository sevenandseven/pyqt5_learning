from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QT学习")
        self.resize(500, 500)
        self.QObject_name_property()


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
        label2.move(100,100)
        label2.setObjectName("notice")
        # 通过设置属性完成不同的样式
        label2.setProperty("notice_level", "warning")
        label2.setText("learing good")
        # 设置一个样式表，可以设置标签的样式
        #label.setStyleSheet("font-size:10pt; color:red")

        label3 = QLabel(self)
        # id选择器，id为notice才会给该标签匹配该样式
        label3.setText("普通标签")
        label3.setObjectName("notice")
        label3.setProperty("notice_level", "normal")
        label3.move(150,150)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())