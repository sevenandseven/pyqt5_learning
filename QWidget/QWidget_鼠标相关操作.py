import sys
from PyQt5.Qt import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("鼠标操作")
    window.resize(500, 500)

    # 当鼠标在window空间内部，则鼠标变为繁忙状态
    #window.setCursor(Qt.BusyCursor)
    label = QLabel(window)
    label.setText("鼠标")
    label.resize(200, 200)
    label.setStyleSheet("background-color:cyan")

    # 第一个参数是一个独一无二的枚举值，第二个参数是一个QCursor对象
    pixmap = QPixmap(r"C:\Users\22104\Desktop\OIP-C.jpg")
    # 将缩放结果返回给外界，但图像并未改变
    new_pixmap = pixmap.scaled(20,20)
    # 鼠标对象需要一个图片对象，所以需要创建一个图片对象
    # 图像对象作为cursor的参数,可以使用str作为图形的路径
    # # (-1,-1)指图片的中心位置，中心位置放在那里，那里就有作用，0，0指左上角，20，20指右下角
    cursor = QCursor(new_pixmap, 20, 20)
    label.setCursor(cursor)
    label.unsetCursor()

    # 可以获取鼠标对象，获取它的位置
    # 返回一个鼠标对象
    print(label.cursor())
    # 设置鼠标的位置,鼠标位置是相比于整个桌面窗口
    current_cursor = label.cursor()
    print(current_cursor.pos())
    print(label.cursor().pos())

    # 鼠标会直接跑到桌面左上角
    current_cursor.setPos(0,0)

    window.show()

    sys.exit(app.exec_())