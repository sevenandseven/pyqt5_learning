import sys
from PyQt5.Qt import *

# 1、创建应用程序,可以传递参数给app，通过命令行输入参数
app = QApplication(sys.argv)
# 获取程序的参数，返回的是一个列表类型
# print(app.arguments())
# # 在其他函数中获得app的参数,获取全局参数
# print(qApp.arguments())

# 2、控件的操作
# 创建控件，设置控件（大小、位置、样式），事件，信号的处理
# 2.1创建控件，控件是一个容器
# 可以再次的包含其他容器,创建一个空白的控件，刚开始不会直接展示，需要调用控件的方法,展示一个空白控件
# 当我们创建一个控件之后，如果说这个控件没有父控件，则把它当作顶层控件（窗口）
# 系统会自定给窗口添加一些装饰（标题栏），窗口控件具备一些特性（设置标题、图标）
window = QWidget()
# 想要展示一个带按钮的控件，鼠标放上去可以点击
#window = QPushButton()
# 展示一个标签类的控件
#window = QLabel()

# 2.2设置控件
#window.setText("hello world!")
# 必须是顶层控件才能修改
window.setWindowTitle("QT界面")
window.resize(400, 400)

# 控件也可以作为一个容器,该控件的父控件是window
# 没有父控件就是顶层控件，顶层控件自带窗口
label = QLabel(window)
label.setText('xxx')
label.move(100, 50)
#label.setWindowTitle('xxxxxxx')
# 没有父控件必须手动显示
#label.show()


# 2.3展示控件
# 刚创建好一个控件之后，（这个控件没有什么父控件）
# 默认情况下不会被展示，只有调用show才会被展示
# 如果这个控件有父控件，哪么父控件展示时子控件也会被展示
window.show()

# 3、应用程序的执行，进入消息循环，让整个程序开始执行，并进入消息循环（无限循环）
# 检测整个程序所接收到的用户的交互信息
sys.exit(app.exec_())

# 当别人通过命令行启动程序时
# 可以设定一种功能（接受命令行传递到参数，来执行不同的业务逻辑）
# args = sys.argv
# print(args)
# if args[1] == '1':
#     print('xxx')
# else:
#     print('ooo')

# 正常退出程序
#sys.exit()