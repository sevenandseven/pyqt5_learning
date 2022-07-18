from class_menu import Window
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = Window()
window.show()
sys.exit(app.exec_())
