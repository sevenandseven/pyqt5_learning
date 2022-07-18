from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.move(100, 100)
window.setFixedSize(600, 600)
#window.resize(600, 600)

label = QLabel(window)
label.setText("社会")
label.move(100, 100)
label.setStyleSheet("background-color:cyan")

def changedCao():
    new_content = label.text() + "社会"
    label.setText(new_content)
    label.adjustSize()
    #label.resize(label.width() + 100, label.height())

btn = QPushButton(window)
btn.setText("增加内容")
btn.move(100, 300)
btn.clicked.connect(changedCao)
window.show()

sys.exit(app.exec_())