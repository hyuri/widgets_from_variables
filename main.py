# UI Generation From Code
# By: Hyuri Pimentel
#
# For now, you have to prefix with "UI_" the name of the variables of which you want widgets to be generated for.
# See the example code "code.py" for reference.
#-------------------------------------------------------------------------------------------


import sys

from PySide2.QtWidgets import QSizePolicy,\
								QApplication,\
								QLabel,\
								QSpinBox,\
								QDoubleSpinBox,\
								QLineEdit,\
								QCheckBox,\
								QComboBox,\
								QPushButton,\
								QVBoxLayout,\
								QHBoxLayout,\
								QGridLayout,\
								QGroupBox,\
								QScrollArea,\
								QFrame,\
								QLayout,\
								QWidget,\
								QShortcut
from PySide2.QtCore import Slot,\
							Qt,\
							Signal,\
							QThread,\
							QObject
from PySide2.QtGui import QKeySequence, QFont


#-------------------------------------------------------------------------------------------
from constants import *
import assets


#-------------------------------------------------------------------------------------------
# Sample Code
import code

#-------------------------------------------------------------------------------------------


def get_widget_by_type(obj):
	if type(obj) == int:
		widget = QSpinBox()
		widget.setRange(INT_RANGE_MIN, INT_RANGE_MAX)
		widget.setSingleStep(INT_RANGE_STEP)
		widget.setValue(obj)
		widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

	elif type(obj) == float:
		widget = QDoubleSpinBox()
		widget.setRange(FLOAT_RANGE_MIN, FLOAT_RANGE_MAX)
		widget.setSingleStep(FLOAT_RANGE_STEP)
		widget.setValue(obj)
		widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

	elif type(obj) == str:
		widget = QLineEdit()
		widget.setText(obj)

	elif type(obj) == bool:
		widget = QCheckBox()
		widget.setChecked(obj)

	elif type(obj) == list:
		widget = QComboBox()
		widget.addItems(obj)
		widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

	elif type(obj) == tuple:
		widget = QFrame()

		if len(obj) <= 3:
			box = QHBoxLayout()
		else:
			box = QVBoxLayout()
		box.setMargin(0)

		for item in obj:
			value_widget = QLabel(f"{item}")
			value_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
			value_widget.setObjectName("tuple")

			box.addWidget(value_widget)

		widget.setLayout(box)

	elif type(obj) == dict:
		widget = QFrame()

		# If less than 3 items, lay it out horizontally else vertically
		# if len(obj) <= 3:
		# 	box = QHBoxLayout()
		# else:
		# 	box = QVBoxLayout()
		# box.setMargin(0)

		grid = QGridLayout()
		grid.setMargin(0)

		row = 0
		for key in obj:
			label = QLabel(f"{key.capitalize()}:")
			grid.addWidget(label, row, 0)
			
			value_widget = get_widget_by_type(obj[key])
			value_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
			grid.addWidget(value_widget, row, 1)

			try:
				value_widget.setRange(INT_RANGE_MIN, INT_RANGE_MAX)
				value_widget.setSingleStep(INT_RANGE_STEP)
				value_widget.setValue(obj[key])
			except:
				pass

			row += 1

		widget.setLayout(grid)

	# TODO: Lists inside of lists. Should probably use QTreeView
	# elif type(obj) == list:
	# 	widget = []
	# 	for l in obj:
	# 		widget.append(QComboBox())
	# 		widget[-1].addItems(obj)
	# 		widget[-1].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
	
	return widget


#-------------------------------------------------------------------------------------------
#
def grid_layout_build(variables_list):
	grid = QGridLayout()
	grid.setSpacing(16)
	grid.setMargin(8)
	# grid.setAlignment(Qt.AlignTop)

	row = 0
	for name, value in variables_list.items():
		if name.startswith("UI_"):
			name = name.replace("UI_", "").replace("_", " ").capitalize()

			grid.addWidget(QLabel(f"{name}:"), row, 0, alignment = Qt.AlignTop)
			grid.addWidget(get_widget_by_type(value), row, 1, alignment = Qt.AlignTop)
	
			row += 1

	return grid


#-------------------------------------------------------------------------------------------
#
class MainWindow(QWidget):
	def __init__(self):
		QWidget.__init__(self)


# 
class Panel(QWidget):
	header_font = QFont()
	header_font.setBold(True)
	header_font.setPointSize(10)

	def __init__(self, name, script):
		QWidget.__init__(self)

		self.name = name
		self.script = script

		self.layout = QVBoxLayout()
		self.layout.setAlignment(Qt.AlignTop)
		self.layout.setMargin(0)

		self.header = QLabel(self.name)
		self.header.setFont(self.header_font)
		self.header.setAlignment(Qt.AlignLeft)
		self.header.setObjectName("header")
		self.layout.addWidget(self.header)

		self.grid = grid_layout_build(vars(self.script))

		self.layout.addLayout(self.grid)
		self.setLayout(self.layout)


#-------------------------------------------------------------------------------------------
# Main
if __name__ == "__main__":
	app = QApplication(sys.argv)

	# Main Window
	main_window = MainWindow()
	# main_window.resize(300, 300)
	main_window.setWindowTitle("UI From Variables")

	# Vertical Box
	layout = QVBoxLayout()
	layout.setAlignment(Qt.AlignTop)
	layout.setMargin(0)
	
	# Panels
	for i in range(1):
		panel = Panel(f"Panel {i + 1}", code)
		layout.addWidget(panel)

	main_window.setLayout(layout)

	# Stylesheet
	with open(assets.stylesheets["default"], "r") as stylesheet:
		main_window.setStyleSheet(stylesheet.read())
	
	main_window.show()

	# Shortcuts
	QShortcut(QKeySequence("Ctrl+Q"), main_window, main_window.close)

	sys.exit(app.exec_())