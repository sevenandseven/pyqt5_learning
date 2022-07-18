import sys
from PyQt5.Qt import *

# 自定义一个关于账号操作的工具类,不需要继承任何类
class AccountTool:
    # 将类属性当作枚举值使用
    ACCOUNT_ERROR = 1
    PWD_ERROE = 2
    SUCCESS = 3
    # 把账号和密码发送给服务器，等待服务器返回结果
    # 添加self的是实例方法，很多时候可以去掉self，将他变为静态方法,参数就可以对应
    # def check_login(self, account, pwd):
    @staticmethod
    def check_login(account, pwd):
        if account != "sz":
            return AccountTool.ACCOUNT_ERROR
        if pwd != "123":
            return AccountTool.PWD_ERROE
        return AccountTool.SUCCESS

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("登录案例")
        self.resize(500, 500)
        self.setMinimumSize(400, 400)
        self.setup_ui()

    def setup_ui(self):
        # 添加三个控件
        # 将局部变量保存到属性中，在所有方法中该属性都可以使用
        # 属性定义在__init__方法之外，报警告
        self.account_le = QLineEdit(self)
        self.pwd_le = QLineEdit(self)
        # 设置为密文格式
        self.pwd_le.setEchoMode(QLineEdit.Password)
        self.login_btn = QPushButton(self)
        self.login_btn.setText("登   录")
        # 连接槽函数
        self.login_btn.clicked.connect(self.login_cao)

        # 占位文本的提示
        self.account_le.setPlaceholderText("请输入账号")
        self.pwd_le.setPlaceholderText("请输入密码")

        # 清空按钮的显示
        self.pwd_le.setClearButtonEnabled(True)
        # 添加自定义行为操作(明文和密文切换)
        # 文本框对象作为他的父对象
        action = QAction(self.pwd_le)
        action.setIcon(QIcon("close.png"))

        def change():
            print("切换明文或密文")
            if self.pwd_le.echoMode() == QLineEdit.Normal:
                self.pwd_le.setEchoMode(QLineEdit.Password)
                action.setIcon(QIcon("close.png"))
            else:
                self.pwd_le.setEchoMode(QLineEdit.Normal)
                action.setIcon(QIcon("open.png"))

        # # 点击图标按钮做一些动作，则可以监听action
        # action.triggered.connect(change)
        #
        # # 图标添加在尾部
        # self.pwd_le.addAction(action, QLineEdit.TrailingPosition)
        # self.pwd_le.addAction(action, QLineEdit.LeadingPosition)
        completer = QCompleter(["sz", "shunzi", "wangzhe"], self.account_le)
        self.account_le.setCompleter(completer)

    # 定义一个槽函数，监听信号
    def login_cao(self):
        # 获取账号和密码
        account = self.account_le.text()
        pwd = self.pwd_le.text()
        state = AccountTool.check_login(account, pwd)
        if state == AccountTool.ACCOUNT_ERROR:
            print("账号错误")
            self.account_le.setText()
            self.account_le.setFocus()
            return None
        if state == AccountTool.PWD_ERROE:
            print("密码错误")
            self.pwd_le.setText("")
            self.pwd_le.setFocus()
            return None
        if state == AccountTool.SUCCESS:
            print("登录成功")

        # 推荐写法
        # if account != "sz":
        #     print("账号错误")
        #     self.account_le.setText()
        #     self.account_le.setFocus()
        #     return None
        # if pwd != "123":
        #     print("密码错误")
        #     self.pwd_le.setText("")
        #     self.pwd_le.setFocus()
        #     return None
        # print("登录成功")
        # 方法二
        # if account == "sz":
        #     if pwd == "123":
        #         print("登录成功！")
        #     else:
        #         print("密码错误！")
        #         self.pwd_le.setText("")
        #         # 获取焦点，密码错误之后可以直接在重新输入密码，不需要人工获取
        #         self.pwd_le.setFocus()
        # else:
        #     print("账号错误！")
        #     self.pwd_le.setText("")
        #     self.account_le.setText("")
        #     # 账号文本框获取焦点
        #     self.account_le.setFocus()
    # 设置控件随窗口的大小改变而改变
    def resizeEvent(self, evt):
        widget_w = 150
        widget_h = 50
        margin = 60
        self.account_le.resize(widget_w, widget_h)
        self.pwd_le.resize(widget_w, widget_h)
        self.pwd_le.resize(widget_w, widget_h)

        # 控件的横坐标
        x = (self.width() - widget_w) / 2
        # 暂时先给定一个y值
        self.account_le.move(x, self.height() / 5)
        self.pwd_le.move(x, self.account_le.y() + margin + widget_h)
        self.login_btn.move(x, self.pwd_le.y() + margin + widget_h)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.setWindowTitle("")
    window.resize(500, 500)
    window.show()
    sys.exit(app.exec_())
