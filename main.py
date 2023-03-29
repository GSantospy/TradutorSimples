# -*- coding: UTF-8 -*-

from googletrans import Translator
import sys
from ui_interface import *
from PySide2 import QtCore, QtGui, QtWidgets

tradutor = Translator()
idiomas_suportados = ['pt', 'en', 'es']

class TradutorPy(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.setWindowTitle('Tradutor Simples')
		self.setWindowIcon(QIcon('icon.png'))

		self.ui.btn_traduzir.clicked.connect(self.Traduzir)
		self.ui.btn_trocar_lang.clicked.connect(self.TrocarLang)
		self.ui.btn_copiar_traduzido.clicked.connect(self.CopiarTraduzido)


	def Traduzir(self):
		lang = self.ui.cb_detectar
		langTraduzir = self.ui.cb_traduzido
		texto = self.ui.pte_traduzir.toPlainText()
		textoPTraduzir = self.ui.pte_traduzido

		if not texto.strip():
			self.popUpVazio()
			return

		idioma = tradutor.detect(texto).lang
		if idioma not in idiomas_suportados:
			self.NaoSuportado()
			return

		traduzirEn = tradutor.translate(texto, dest="en").text
		traduzirPt = tradutor.translate(texto, dest="pt").text
		traduzirEs = tradutor.translate(texto, dest="es").text

						# TRADUZINDO DO PORTUGUÊS
		if lang.currentIndex() == 0 and langTraduzir.currentIndex() == 0:
			textoPTraduzir.setPlainText(traduzirEn)

		elif lang.currentIndex() == 0 and langTraduzir.currentIndex() == 1:
			self.PopUpSelecioneOI()

		elif lang.currentIndex() == 0 and langTraduzir.currentIndex() == 2:
			textoPTraduzir.setPlainText(traduzirEs)



						# TRADUZINDO DO INGLÊS
		elif lang.currentIndex() == 1 and langTraduzir.currentIndex() == 0:
			self.PopUpSelecioneOI()

		elif lang.currentIndex() == 1 and langTraduzir.currentIndex() == 1:
			textoPTraduzir.setPlainText(traduzirPt)

		elif lang.currentIndex() == 1 and langTraduzir.currentIndex() == 2:
			textoPTraduzir.setPlainText(traduzirEs)



						# TRADUZINDO DO ESPANHOL
		elif lang.currentIndex() == 2 and langTraduzir.currentIndex() == 0:
			textoPTraduzir.setPlainText(traduzirEn)

		elif lang.currentIndex() == 2 and langTraduzir.currentIndex() == 1:
			textoPTraduzir.setPlainText(traduzirPt)

		elif lang.currentIndex() == 2 and langTraduzir.currentIndex() == 2:
			self.PopUpSelecioneOI()


	def TrocarLang(self):
		index1 = self.ui.cb_detectar.currentIndex()
		index2 = self.ui.cb_traduzido.currentIndex()

		# se o index1 for igual a Português e index2 for igual a inglês, então troca de lugar.
		if index1 == 0 and index2 == 0:
			self.ui.cb_detectar.setCurrentIndex(1)
			self.ui.cb_traduzido.setCurrentIndex(1)

		elif index1 == 0 and index2 == 2:
			self.ui.cb_detectar.setCurrentIndex(2)
			self.ui.cb_traduzido.setCurrentIndex(1)

		elif index1 == 1 and index2 == 1:
			self.ui.cb_detectar.setCurrentIndex(0)
			self.ui.cb_traduzido.setCurrentIndex(0)

		elif index1 == 1 and index2 == 2:
			self.ui.cb_detectar.setCurrentIndex(2)
			self.ui.cb_traduzido.setCurrentIndex(0)

		elif index1 == 2 and index2 == 0:
			self.ui.cb_detectar.setCurrentIndex(1)
			self.ui.cb_traduzido.setCurrentIndex(2)

		elif index1 == 2 and index2 == 1:
			self.ui.cb_detectar.setCurrentIndex(0)
			self.ui.cb_traduzido.setCurrentIndex(2)


	def CopiarTraduzido(self):
		textotraduzido = self.ui.pte_traduzido.toPlainText()
		if not textotraduzido.strip():
			self.popUpVazio()
			return
		clipboard = QApplication.clipboard()
		clipboard.setText(textotraduzido, mode=QClipboard.Clipboard)
		msg = QMessageBox()
		msg.setWindowTitle('Tradutor Simples')
		msg.setText('Tradução copiada para a área de transferência!')
		msg.setWindowIcon(QIcon('icon.png'))
		x = msg.exec_()

	def PopUpSelecioneOI(self):
		msg = QMessageBox()
		msg.setWindowTitle('Tradutor Simples')
		msg.setText('Selecione um idioma diferente!')
		msg.setWindowIcon(QIcon('icon.png'))
		x = msg.exec_()

	def popUpVazio(self):
		msg = QMessageBox()
		msg.setWindowTitle('Tradutor Simples')
		msg.setText('Não há nada digitado!')
		msg.setWindowIcon(QIcon('icon.png'))
		x = msg.exec_()

	def NaoSuportado(self):
		msg = QMessageBox()
		msg.setWindowTitle('Tradutor Simples')
		msg.setText('Idioma não suportado!')
		msg.setWindowIcon(QIcon('icon.png'))
		x = msg.exec_()




if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = TradutorPy()
	window.show()
	sys.exit(app.exec_())