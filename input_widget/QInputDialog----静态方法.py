from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QInputDialog----静态方法的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 有返回值，说明他是阻塞式的方法,快速获取一个整型数据
        result = QInputDialog.getInt(self, "xxx1", "xxx2", value=88, step=12)

        # 快速获取一个double型数据
        result = QInputDialog.getDouble(self, "xx2", "jxks", 888.88, decimals=3)
        # 获取文本（字符串数据）
        result = QInputDialog.getText(self, "ewi", "text")
        QInputDialog.getMultiLineText(self, "da", "dks", "default")
        # 获取下拉列表中某一个条目
        result = QInputDialog.getItem(self, "xxd", "dsd", ["1", "2", "3"], 2, True)

        # 如果没有提供步长调节，可以通过该对象设置，看是否有相关方法，遍历所有组件，找到对应的步长调节器
        # 元组[最终结果，True or False]
        print(result)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
