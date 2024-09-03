# -*- coding: UTF-8 -*-

from googletrans import Translator
import sys
from ui_interface import *
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QPlainTextEdit, QComboBox
from PySide6.QtGui import QIcon, QClipboard

tradutor = Translator()
idiomasSuportados = ['pt', 'en', 'es']

class TradutorPy(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.setWindowTitle('Tradutor Simples')
		self.setWindowIcon(QIcon('icon.png'))

		self.ui.btn_traduzir.clicked.connect(self.Traduzir)
		self.ui.cb_traduzido.setCurrentIndex(1)
		self.ui.btn_trocar_lang.clicked.connect(self.TrocarLang)
		self.ui.btn_copiar_traduzido.clicked.connect(self.CopiarTraduzido)


	def Traduzir(self):
		langIndex = self.ui.cb_detectar.currentIndex()
		langTraduzirIndex = self.ui.cb_traduzido.currentIndex()
		texto = self.ui.pte_traduzir.toPlainText()
		textoPTraduzir = self.ui.pte_traduzido

		if not texto.strip():
			self.popUpVazio()
			return
		
		idiomaDetectado = tradutor.detect(texto).lang
		if idiomaDetectado not in idiomasSuportados:
			self.NaoSuportado()
			return
		
		traducoes = {
			'en': tradutor.translate(texto, dest='en').text,
			'pt': tradutor.translate(texto, dest='pt').text,
			'es': tradutor.translate(texto, dest='es').text 
		}

		idiomas = ['pt', 'en', 'es']
		idiomaOrigem = idiomas[langIndex]
		idiomaDestino = idiomas[langTraduzirIndex]

		if idiomaOrigem == idiomaDestino:
			self.PopUpSelecioneOI()
		else:
			try:
				if idiomaDestino in traducoes:
					textoPTraduzir.setPlainText(traducoes[idiomaDestino])
				else:
					self.PopUpSelecioneOI()
			except Exception as e:
				print(f'Erro na tradução: {e}')
				self.PopUpSelecioneOI()


	def TrocarLang(self):
		index1 = self.ui.cb_detectar.currentIndex()
		index2 = self.ui.cb_traduzido.currentIndex()

		self.ui.cb_detectar.setCurrentIndex(index2)
		self.ui.cb_traduzido.setCurrentIndex(index1)


	def CopiarTraduzido(self):
		textoTraduzido = self.ui.pte_traduzido.toPlainText().strip()
		if not textoTraduzido:
			self.popUpVazio()
			return
		
		clipboard = QApplication.clipboard()
		clipboard.setText(textoTraduzido, mode=QClipboard.Clipboard)
		self.mostrarMensagem('Tradução copiada para à área de transferência!')

	def PopUpSelecioneOI(self):
		self.mostrarMensagem('Selecione um idioma diferente!')

	def popUpVazio(self):
		self.mostrarMensagem('Não há nada digitado!')

	def NaoSuportado(self):
		self.mostrarMensagem('Idioma não suportado!')
	
	def mostrarMensagem(self, texto):
		msg = QMessageBox()
		msg.setWindowTitle('Tradutor Simples')
		msg.setText(texto)
		msg.setWindowIcon(QIcon('icon.png'))
		msg.exec()




if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = TradutorPy()
	window.show()
	sys.exit(app.exec())