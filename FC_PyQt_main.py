from PyQt5 import QtWidgets
import sys
from Fight_Club_design import Ui_Form

app = QtWidgets.QApplication(sys.argv)

w = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(w)
w.show()
app.setStyle('Fusion')

sys.exit(app.exec_())
