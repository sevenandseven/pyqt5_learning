from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox的学习")
        self.resize(500, 500)
        self.city_dic = {
            "北京":{
                "东城":"001",
                "西城": "002",
                "朝阳": "003",
                "丰台": "004"
            },
            "上海": {
                "黄埔": "005",
                "徐汇": "006",
                "长宁": "007",
                "静安": "008",
                "松江": "009"
            },
            "广东": {
                "广州": "010",
                "深圳": "011",
                "湛江": "012",
                "佛山": "013"
            },
        }
        self.setup_ui()

    def setup_ui(self):
        # 创建两个下拉列表控件
        pro = QComboBox(self)
        city = QComboBox(self)
        self.pro = pro
        self.city = city
        pro.move(100, 100)
        city.move(200, 100)

        # 展示数据到第一个下拉选择控件当中
        #pro.addItems(self.city_dic.keys())
        # 监听省下拉列表中当前值改变发生信号,需要接受省会的名字
        pro.currentIndexChanged[str].connect(self.pro_changed)
        #self.pro_changed(pro.currentText())

        # 监听城市下拉列表里面的当前值发生改变的信号
        city.currentIndexChanged[int].connect(self.city_changed)
        #self.city_changed(city.currentIndex())

        pro.addItems(self.city_dic.keys())
    def pro_changed(self, pro_name):
        #print(pro_name)
        # 根据省的名称到字典里获得对应城市的字典
        citys = self.city_dic[pro_name]
        self.city.blockSignals(True)
        self.city.clear()
        self.city.blockSignals(False)
        #self.city.addItems(citys.keys())
        for key, val in citys.items():
            self.city.addItem(key, val)

    def city_changed(self, city_idx):
        #print(city_idx)
        print(self.city.itemData(city_idx))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
