from PyQt5.Qt import *
from predict import main as Load_VGG
from predict_mobilenet import main as Load_MobileNet

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("海洋生物检测系统")
        self.setMinimumSize(550, 560)
        self.setMaximumSize(550, 560)
        self.width_margin = 70
        self.height_margin = 70
        self.label_margin = 20
        self.setup_ui()
    # 存放各种按钮和布局
    def setup_ui(self):
        width_margin = self.width_margin
        height_margin = self.height_margin
        btn_input = QPushButton("输入图片", self)
        # 模型按钮位置
        btn_input.move(width_margin, (self.height() - 3 * btn_input.height()) / 4)
        btn_model = QPushButton("载入模型", self)
        btn_model.move(width_margin,
                       2 * (self.height() - 3 * btn_input.height()) / 4 + btn_input.height())

        # 输入图像
        label_input2 = QLabel(self)
        label_input2.resize(240, 180)
        # 图像的坐标
        label_input2.move(2 * width_margin + btn_input.width() + 5,
                          self.height() - 2 * label_input2.height() - 2 * self.height_margin)
        label_input2.setStyleSheet("background-color:black")
        # 输入按钮
        label_input = QLabel("原始输入图", self)
        label_input.move(2 * width_margin + btn_input.width() + label_input2.width() / 2 - label_input.width() / 2,
                         self.height() - 2 * label_input2.height() - 2 * self.height_margin - 30)

        def read_img():
            img, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./",

                                                        "All Files (*);;Excel Files (*.xls)")  # 设置文件扩展名过滤,注意用双分号间隔

            pic = QPixmap(img).scaled(label_input2.width(), label_input2.height())
            label_input2.setPixmap(pic)
            # print(menu.actionEvent())
            action_vgg.triggered.connect(lambda: Load_VGG(img))
            action_mobile.triggered.connect(lambda: Load_MobileNet(img))
        def show_vgg():
            out_path = r"E:\object_detection\faster rcnn\test_result\test_result_vgg16.jpg"
            pic = QPixmap(out_path).scaled(label_output2.width(), label_output2.height())
            label_output2.setPixmap(pic)
        def show_MobileNet():
            out_path = r"E:\object_detection\faster rcnn\test_result\test_result_mobile.jpg"
            pic = QPixmap(out_path).scaled(label_output2.width(), label_output2.height())
            label_output2.setPixmap(pic)


        menu = QMenu()
        action_vgg = QAction("载入VGG模型", menu)
        action_mobile = QAction("载入MobileNet模型", menu)
        menu.addAction(action_vgg)
        menu.addSeparator()
        menu.addAction(action_mobile)
        btn_model.setMenu(menu)

        btn_output = QPushButton("检测结果", self)
        # 输出按钮
        btn_output.move(width_margin,
                        3 * (self.height() - 3 * btn_model.height())/4 + 2*btn_input.height())
        label_output2 = QLabel(self)
        label_output2.resize(240, 180)
        label_output2.move(2 * width_margin + btn_input.width() + 5,
                           self.height() - label_output2.height() - height_margin)
        label_output2.setStyleSheet("background-color:black")

        # 输出标签
        label_output = QLabel("检测结果图", self)
        label_output.move(2 * width_margin + btn_input.width() + label_output2.width() / 2 - label_output.width() / 2,
                          self.height() - label_output2.height() - height_margin - 30)
        def vgg():
            btn_output.clicked.connect(show_vgg)
        action_vgg.triggered.connect(vgg)

        def mobilenet():
            btn_output.clicked.connect(show_MobileNet)
        action_mobile.triggered.connect(mobilenet)
        # fileName2, ok2 = QFileDialog.getSaveFileName(self,"文件保存", "./","All Files (*);;Text Files (*.txt)")
        btn_input.clicked.connect(read_img)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.resize(500, 500)
    window.show()
    sys.exit(app.exec_())
