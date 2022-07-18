from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout---功能简介的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color:cyan")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color:yellow")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color:red")
        label4 = QLabel("标签4")
        label4.setStyleSheet("background-color:orange")

        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color:pink")
        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color:blue")
        label7 = QLabel("标签7")
        label7.setStyleSheet("background-color:cyan")

        v_layout = QVBoxLayout()
        v_layout.addWidget(label5)
        v_layout.addWidget(label6)
        v_layout.addWidget(label7)

        gl = QGridLayout()
        self.setLayout(gl)
        gl.addWidget(label1, 0, 0)
        gl.addWidget(label2, 0, 1)
        gl.addWidget(label3, 0, 2)
        # 合并单元格,起始的行，起始的列，跨越的行（占据多少行），跨越的列
        gl.addWidget(label4, 1, 0, 1, 2)
        gl.addLayout(v_layout, 4, 3)

        # 获取位置、获取条目(位置，占据的行列数)
        # print(gl.getItemPosition(1))
        # 获取信息
        #print(gl.itemAtPosition(0, 1).widget().text())
        # # 列宽和行高（限制最小的列宽和行高）
        # gl.setColumnMinimumWidth(0, 100)
        # gl.setRowMinimumHeight(0, 100)

        # 拉伸系数：控制该按照怎样的比例分配额外的多余空间
        # gl.setColumnStretch(0, 2)
        # gl.setColumnStretch(1, 1)
        # gl.setRowStretch(4, 1)

        # 间距控制
        # 打印间距gl.horizontalSpacing()
        print(gl.spacing())

        # 设置水平方向的间距
        gl.setHorizontalSpacing(60)
        gl.setVerticalSpacing(50)
        # 同时设置
        gl.setSpacing(60)

        # 信息获取
        print(gl.rowCount())
        print(gl.columnCount())
        # 第0行第1列占据的尺寸
        print(gl.cellRect(0, 1))
        # 即使方向发生了变化，但他的位置还是参照原点角
        print(gl.itemAtPosition(0, 1).widget().text())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()
    gl = window.layout()
    # 版本问题，需要在父控件显示完成之后才可以
    print(gl.cellRect(0, 1))

    sys.exit(app.exec_())
