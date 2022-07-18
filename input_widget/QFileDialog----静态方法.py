from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog----静态方法的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 获取一个打开的文件名称,"./表示当前文件夹"
        # 过滤掉不需要的文件格式,一个过滤器,".png",**表示所有文件,想写多个需要用;;分割
        #result = QFileDialog.getOpenFileName(self, "选择一个py文件", ",/",
        #                                     "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)")
        # 一个元素，绝对路径和过滤字符串
        #print(result)

        # # 同时获取多个文件
        # result = QFileDialog.getOpenFileNames(self, "选择多个文件",",/",
        #                                      "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)" )
        # # 返回一个元组，元组的第一个元素是一个列表，列表中共有所选的多个文件路径，后边就是过滤器
        # print(result)

        # result = QFileDialog.getOpenFileUrl(self, "选择一个文件", "./",
        #                                     "All(*.*);;Images(*.png *.jpg);;python(*.py)")
        # # 元组的第一个元素变成了QUrl对象,本地文件所对应的协议：file//
        # print(result)

        # 保存文件
        # result = QFileDialog.getSaveFileName(self, "保存文件", "./", "All(*.*);;Images(*.png *.jpg);;python文件(*.py)")
        # # 已经获得保存文件的路径，可以直接将所要保存的文件的内容直接写入该文件
        # print(result)

        # # 获取文件夹
        # result = QFileDialog.getExistingDirectory(self, "选择一个文件夹", "./")
        # # 输出结果就是一个单独的路径字符串，
        # print(result)

        # 目录需要是一个QUrl对象才可以
        result = QFileDialog.getExistingDirectory(self, "选择一个文件夹", QUrl("./"))
        print(result)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
