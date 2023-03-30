from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import Qt
from PySide6.QtCore import Signal, QObject

class CheckableComboBox(QComboBox):
	def __init__(self):
		super().__init__()
		self.setMaximumWidth(200)
		self.setMinimumWidth(200)
		self.setPlaceholderText('Colonne')
		self.setStyleSheet("""QComboBox {
								border: 1px solid rgb(200, 200, 200);
								}
								QComboBox QAbstractItemView {
									color: rgb(90, 90, 90);
									border: 1px solid rgb(255, 255, 255);
									border-radius: 0px;
									padding: 10px;
								}""")
		self._changed = False
		self.view().pressed.connect(self.handleItemPressed)

	def setItemChecked(self, index, checked=False):
		item = self.model().item(index, self.modelColumn())
		if checked:
			item.setCheckState(Qt.Checked)
		else:
			item.setCheckState(Qt.Unchecked)

	def handleItemPressed(self, index):
		item = self.model().itemFromIndex(index)

		if item.checkState() == Qt.Checked:
			item.setCheckState(Qt.Unchecked)
		else:
			item.setCheckState(Qt.Checked)
		self._changed = True


	def hidePopup(self):
		if not self._changed:
			super().hidePopup()
		self._changed = False

	def itemChecked(self, index):
		item = self.model().item(index, self.modelColumn())
		return item.checkState() == Qt.Checked

class Signals(QObject):
    itemCheckStateChanged = Signal(int)