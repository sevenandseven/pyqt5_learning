from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCalendarWidget---简介的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        cw = QCalendarWidget(self)
        # 设置最小日期
        cw.setMinimumDate(QDate(1999, 12,12))
        # 设置最大日期
        cw.setMaximumDate(QDate(2024, 12, 12))
        # 设置日期范围
        cw.setDateRange(QDate(1999, 12,12), QDate(2024, 12, 12))
        #cw.setDateEditEnabled(False)
        cw.setDateEditAcceptDelay(200)

        btn = QPushButton(self)
        btn.move(400, 400)
        btn.setText("测试按钮")
        # 显示月份
        btn.clicked.connect(lambda: print(cw.monthShown()))
        # 显示年份
        btn.clicked.connect(lambda: print(cw.yearShown()))
        # 显示选中的时间
        btn.clicked.connect(lambda: print(cw.selectedDate()))

        # 隐藏导航条
        #cw.setNavigationBarVisible(False)
        # 一周的第一天设置为周日
        cw.setFirstDayOfWeek(Qt.Sunday)
        # 网格显示
        cw.setGridVisible(True)

        # 设置水平头和垂直头的字体格式
        tcf = QTextCharFormat()
        tcf.setFontPointSize(16)
        tcf.setFontFamily("隶书")
        tcf.setFontUnderline(True)

        cw.setHeaderTextFormat(tcf)
        # 显示格式
        cw.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)

        # 垂直头,显示周数一行一周, 隐藏
        cw.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

        t_tcf = QTextCharFormat()
        t_tcf.setFontPointSize(20)
        # 针对特定的星期、特定的日期控制文本字符格式
        #cw.setWeekdayTextFormat(Qt.Tuesday, t_tcf)
        # 只改某一天
        #cw.setDateTextFormat(QDate(2022, 3, 8), t_tcf)

        # 控制日期无法选中,无法通过鼠标选中
        cw.setSelectionMode(QCalendarWidget.NoSelection)
        # 通过代码选中
        cw.setSelectedDate(QDate(2022, 3, 8))

        cw.activated.connect(lambda date: print(date))
        cw.clicked.connect(lambda date: print(date))
        cw.currentPageChanged.connect(lambda y,m: print(y,m))
        cw.selectionChanged.connect(lambda: print("选中的日期发生改变", cw.selectedDate()))

        # 选中
        cw.setSelectedDate(QDate(2008, 8, 8))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(700, 700)
    window.show()

    sys.exit(app.exec_())
