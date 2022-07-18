from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("日期时间的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # dt = QDateTime(2018, 12, 12, 12, 30)
        # print(dt)
        # QDateTimeEdit(dt, self)
        # 获取当前的日期时间
        # dt = QDateTime.currentDateTime()
        # # 与世界时间间隔8小时
        # print(dt.offsetFromUtc() // 3600)
        # # 并未改变对象本身，而是新生成了一个对象
        # dt = dt.addYears(2)
        # QDateTimeEdit(dt, self)
        # time = QTime.currentTime()
        # time.start()
        #
        # # 获取从开始计时时刻到现在所经历的时间
        # btn = QPushButton(self)
        # btn.setText("测试")
        # btn.move(200, 200)
        # # 时间调整为s
        # btn.clicked.connect(lambda: print(time.elapsed() / 1000))

        # 年月日,当前时间
        #dte = QDateTimeEdit(QDate.currentDate(), self)
        # 只想展示当前时间
        #dte = QDateTimeEdit(QTime.currentTime(), self)
        # # 只想展示当前日期
        dte = QDateTimeEdit(QDate.currentDate(), self)
        dte.move(100, 100)
        # 设置格式,分、秒、毫秒
        dte.setDisplayFormat("yy-MM-dd & m: ss: zzz")
        print(dte.displayFormat())
        # 获取当前section的总个数
        print(dte.sectionCount())

        test_btn = QPushButton(self)
        test_btn.setText("测试按钮")
        test_btn.move(150, 150)
        # 当前section的索引
        #test_btn.clicked.connect(lambda: print(dte.currentSectionIndex()))
        # 设置当前索引为3
        #test_btn.clicked.connect(lambda: print(dte.setCurrentSectionIndex(3)))
        def test():
            print("xxx")
            dte.setFocus()
            #dte.setCurrentSectionIndex(3)
            # 指定枚举值获取索引，容错率更高一点
            dte.setCurrentSection(QDateTimeEdit.DaySection)
            # 或置指定部分对应的文本
            print(dte.sectionText(QDateTimeEdit.DaySection))
            # # 不能在获取焦点，它会将原来的效果重置，恢复到原来的初始位置
            # dte.setMaximumDateTime(QDateTime(2020, 8, 15, 12, 30))
            # dte.setMinimumDateTime(QDateTime.currentDateTime())
            # # 获取日期时间范围
            # dte.setDateTimeRange(QDateTime.currentDateTime().addDays(-3),
            #                      QDateTime.currentDateTime().addDays(3))
            dte.setCalendarPopup(True)
            # 获取内容
            print(dte.dateTime())
            print(dte.time())
            print(dte.date())

        test_btn.clicked.connect(test)
        # 当section完全编辑完才会发射该信号
        dte.dateTimeChanged.connect(lambda val: print(val))
        dte.dateChanged.connect(lambda val: print("日期发生改变：", val))
        dte.timeChanged.connect(lambda val: print("时间发生改变：", val))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(500, 500)
    window.show()

    sys.exit(app.exec_())
