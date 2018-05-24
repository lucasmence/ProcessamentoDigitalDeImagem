#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, random
import os

import binarizacao
import filtroMedia
import filtroMediana
import filtroModa
import filtroOrdemK
import filtroPassaAltaLaplace
import filtroSobel
import filtroRoberts
import filtroPrewitt
import equalizacaoHistograma
import quantizacao

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtWidgets

reload(sys)
sys.setdefaultencoding('utf-8')

class WindowHome(QtWidgets.QMainWindow):
    
    windowCamera = None
    imageViewOriginal = None
    imageViewEdited = None
    imageViewEditedHorizontal = None
    imageViewEditedVertical = None
    mapFilter = None
    cbxFilter = None
    edtPath = None
    edtCustomValue = None
    qt = None
    imgLoaded = False
    imgGradientLoaded = False
    index = None
    indexHorizontal = None
    indexVertical = None
    lineSum = 0
    lineSumHorizontal = 0
    lineSumVertical = 0
    graphType = 0 
    graphTypeHorizontal = 0
    graphTypeVertical = 0
    graphNormalValue = 260
    graphTinyValue = 5000
       
    def paintEvent(self, e):

        self.qp = QtGui.QPainter()
        self.qp.begin(self)
        
        if (self.imgLoaded == True):
            self.imgLoaded == False
            self.index = [0.00] * 256
            self.lineSum = 0
            
            for listItem in open('histogram.txt','r').read().splitlines():
                if (listItem != '\xef\xbb\xbf80') and (listItem != '\xef\xbb\xbf79') and (listItem != '\xef\xbb\xbf81') and (listItem != '\xef\xbb\xbf122') and (listItem != '\xef\xbb\xbf245') and (listItem != '\xef\xbb\xbf231') and (listItem != '\xef\xbb\xbf141') and (listItem != '\xef\xbb\xbf90') and (listItem != '\xef\xbb\xbf37') and (listItem != '\xef\xbb\xbf127') and (listItem != '\xef\xbb\xbf66') and (listItem != '\xef\xbb\xbf132') and (listItem != '\xef\xbb\xbf0') and (listItem != '\xef\xbb\xbf82') and (listItem != '\xef\xbb\xbf548') and (listItem != '\xef\xbb\xbf246') and (listItem != '\xef\xbb\xbf184') and (listItem != '\xef\xbb\xbf97') and (listItem != '\xef\xbb\xbf42') and (listItem != '\xef\xbb\xbf60'):
                    self.lineSum = self.lineSum + 1
                    value = int(listItem)
                    self.index[value] = self.index[value] + 1
                    
            for x in xrange(0,247): 
                self.index[x] = int(self.index[x] / self.lineSum * self.graphType)
        
        if self.index != None:
            for x in xrange(0,247):
                if self.index[x] > 255:
                    self.index[x] = 255
                self.qp.drawLine(510+x,740-self.index[x],510+x,740)
        
        
        if (self.imgGradientLoaded == True):
            self.imgGradientLoaded == False
            
            self.indexHorizontal = [0.00] * 256
            self.lineSumHorizontal = 0
            
            for listItem in open('histogramHorizontal.txt','r').read().splitlines():
                if (listItem != '\xef\xbb\xbf231') and (listItem != '\xef\xbb\xbf141') and (listItem != '\xef\xbb\xbf90') and (listItem != '\xef\xbb\xbf37') and (listItem != '\xef\xbb\xbf127') and (listItem != '\xef\xbb\xbf66') and (listItem != '\xef\xbb\xbf132') and (listItem != '\xef\xbb\xbf0') and (listItem != '\xef\xbb\xbf82') and (listItem != '\xef\xbb\xbf548') and (listItem != '\xef\xbb\xbf246') and (listItem != '\xef\xbb\xbf184') and (listItem != '\xef\xbb\xbf97') and (listItem != '\xef\xbb\xbf42') and (listItem != '\xef\xbb\xbf60'):
                    self.lineSumHorizontal = self.lineSumHorizontal + 1
                    value = int(listItem)
                    self.indexHorizontal[value] = self.indexHorizontal[value] + 1
                    
            for x in xrange(0,247):
                self.indexHorizontal[x] = int(self.indexHorizontal[x] / self.lineSumHorizontal * self.graphTypeHorizontal)
            
            
            self.indexVertical = [0.00] * 256
            self.lineSumVertical = 0
            
            for listItem in open('histogramVertical.txt','r').read().splitlines():
                if (listItem != '\xef\xbb\xbf231') and (listItem != '\xef\xbb\xbf141') and (listItem != '\xef\xbb\xbf90') and (listItem != '\xef\xbb\xbf37') and (listItem != '\xef\xbb\xbf127') and (listItem != '\xef\xbb\xbf66') and (listItem != '\xef\xbb\xbf132') and (listItem != '\xef\xbb\xbf0') and (listItem != '\xef\xbb\xbf82') and (listItem != '\xef\xbb\xbf548') and (listItem != '\xef\xbb\xbf246') and (listItem != '\xef\xbb\xbf184') and (listItem != '\xef\xbb\xbf97') and (listItem != '\xef\xbb\xbf42') and (listItem != '\xef\xbb\xbf60'):
                    self.lineSumVertical = self.lineSumVertical + 1
                    value = int(listItem)
                    self.indexVertical[value] = self.indexVertical[value] + 1
                    
            for x in xrange(0,247):
                self.indexVertical[x] = int(self.indexVertical[x] / self.lineSumVertical * self.graphTypeVertical)
        
        if self.indexVertical != None:
            for x in xrange(0,247):
                if self.indexVertical[x] > 255:
                    self.indexVertical[x] = 255
                self.qp.drawLine(1065+x,740-self.indexVertical[x],1065+x,740)
                
        if self.indexHorizontal != None:
            for x in xrange(0,247):
                if self.indexHorizontal[x] > 255:
                    self.indexHorizontal[x] = 255
                self.qp.drawLine(785+x,740-self.indexHorizontal[x],785+x,740)
           
        self.qp.end()  
            
    
    def __init__(self, parent=None):
        #criando nossa janela
        
        super(WindowHome, self).__init__(parent)
        self.setWindowTitle('Processamento Digital de Imagens')
        self.resize(800,600)
        
        btnLayout = QPushButton('',self)
        btnLayout.move(0,0)
        btnLayout.setFixedWidth(1355)
        btnLayout.setFixedHeight(755)
        btnLayout.setStyleSheet('border: 1px solid red;')
          
        btnProcess = QPushButton('Processar', self)
        btnProcess.move(500,140)
        btnProcess.setFixedWidth(160)
        btnProcess.setFixedHeight(20)
        btnProcess.setStyleSheet('font-size: 15px; color: white; background-color: blue')
        
        btnExit = QPushButton('Sair', self)
        btnExit.move(20,20)
        btnExit.setFixedWidth(120)
        btnExit.setFixedHeight(40)
        btnExit.setStyleSheet('font-size: 30px; color: white; background-color: red')
        
        lblTitle = QLabel('Processamento de Imagens', self)
        lblTitle.move(220,10)
        lblTitle.setStyleSheet('font-size: 30px; color: black')
        lblTitle.adjustSize()
        
        lblInfo = QLabel('Desenvolvido por Lucas da Silva - RA: 203417 - UniSalesiano Aracatuba - SP, Marco de 2018', self)
        lblInfo.move(5,735)
        lblInfo.setStyleSheet('font-size: 12px; color: blue')
        lblInfo.adjustSize()
        
        lblPath = QLabel('Arquivo:', self)
        lblPath.move(220,50)
        lblPath.setStyleSheet('font-size: 20px; color: black')
        lblPath.adjustSize()
        
        self.edtPath = QLineEdit('TesteBoat.bmp', self)
        self.edtPath.move(220,80)
        self.edtPath.setFixedWidth(300)
        self.edtPath.setFixedHeight(20)
        self.edtPath.setStyleSheet('font-size: 10px; color: black')
        self.edtPath.adjustSize()
        
        lblCustomValue = QLabel('Valor:', self)
        lblCustomValue.move(360,175)
        lblCustomValue.setStyleSheet('font-size: 20px; color: black')
        lblCustomValue.adjustSize()
        
        self.edtCustomValue = QLineEdit('0', self)
        self.edtCustomValue.move(360,200)
        self.edtCustomValue.setFixedWidth(50)
        self.edtCustomValue.setFixedHeight(20)
        self.edtCustomValue.setStyleSheet('font-size: 10px; color: black')
        self.edtCustomValue.adjustSize()
        
        btnLoad = QPushButton('Carregar', self)
        btnLoad.move(530,80)
        btnLoad.setFixedWidth(80)
        btnLoad.setFixedHeight(20)
        btnLoad.setStyleSheet('font-size: 10px; color: black; background-color: white')
        
        lblFilter = QLabel('Filtro:', self)
        lblFilter.move(300,110)
        lblFilter.setStyleSheet('font-size: 20px; color: black')
        lblFilter.adjustSize()
        
        self.mapFilter = {
             0:'Binarizacao',
             1:'Media',
             2:'Mediana',
             3:'Moda',
             4:'Ordem-k',
             5:'Passa Alta - Laplaciano',
             6:'Operadores de Sobel',
             7:'Operadores de Roberts',
             8:'Operadores de Prewitt',
             9:'Equalizacao de Histograma',
             10:'Quantizacao'
            }
        
        self.cbxFilter = QComboBox(self)
        self.cbxFilter.move(300,140)
        self.cbxFilter.setFixedWidth(160)
        self.cbxFilter.setFixedHeight(20)
        self.cbxFilter.setStyleSheet('font-size: 10px')
        
        for key, value in self.mapFilter.items():
            self.cbxFilter.insertItem(key, value, None)
        
        lblOriginalImage = QLabel('Imagem Original:', self)
        lblOriginalImage.move(50,170)
        lblOriginalImage.setStyleSheet('font-size: 20px; color: black')
        lblOriginalImage.adjustSize()
        
        lblEditedImage = QLabel('Imagem Alterada:', self)
        lblEditedImage.move(510,170)
        lblEditedImage.setStyleSheet('font-size: 20px; color: black')
        lblEditedImage.adjustSize()
        
        lblEditedHorizontalImage = QLabel('Gradiente Vertical:', self)
        lblEditedHorizontalImage.move(785,170)
        lblEditedHorizontalImage.setStyleSheet('font-size: 20px; color: black')
        lblEditedHorizontalImage.adjustSize()
        
        lblEditedVerticalImage = QLabel('Gradiente Horizontal:', self)
        lblEditedVerticalImage.move(1065,170)
        lblEditedVerticalImage.setStyleSheet('font-size: 20px; color: black')
        lblEditedVerticalImage.adjustSize()
        
        btnLayoutOriginalImage = QPushButton('',self)
        btnLayoutOriginalImage.move(45,205)
        btnLayoutOriginalImage.setFixedWidth(260)
        btnLayoutOriginalImage.setFixedHeight(260)
        btnLayoutOriginalImage.setStyleSheet('border: 1px solid purple;')
        
        btnLayoutEditedImage = QPushButton('',self)
        btnLayoutEditedImage.move(505,205)
        btnLayoutEditedImage.setFixedWidth(260)
        btnLayoutEditedImage.setFixedHeight(260)
        btnLayoutEditedImage.setStyleSheet('border: 1px solid purple;')
        
        btnLayoutEditedHorizontalImage = QPushButton('',self)
        btnLayoutEditedHorizontalImage.move(780,205)
        btnLayoutEditedHorizontalImage.setFixedWidth(260)
        btnLayoutEditedHorizontalImage.setFixedHeight(260)
        btnLayoutEditedHorizontalImage.setStyleSheet('border: 1px solid purple;')
        
        btnLayoutEditedVerticalImage = QPushButton('',self)
        btnLayoutEditedVerticalImage.move(1060,205)
        btnLayoutEditedVerticalImage.setFixedWidth(260)
        btnLayoutEditedVerticalImage.setFixedHeight(260)
        btnLayoutEditedVerticalImage.setStyleSheet('border: 1px solid purple;')
        
        btnLayoutEditedImageHistogram = QPushButton('',self)
        btnLayoutEditedImageHistogram.move(505,480)
        btnLayoutEditedImageHistogram.setFixedWidth(260)
        btnLayoutEditedImageHistogram.setFixedHeight(260)
        btnLayoutEditedImageHistogram.setStyleSheet('border: 1px solid purple;')
        
        btnLayoutEditedHorizontalImageHistogram = QPushButton('',self)
        btnLayoutEditedHorizontalImageHistogram.move(780,480)
        btnLayoutEditedHorizontalImageHistogram.setFixedWidth(260)
        btnLayoutEditedHorizontalImageHistogram.setFixedHeight(260)
        btnLayoutEditedHorizontalImageHistogram.setStyleSheet('border: 1px solid purple;')
        
        btnLayoutEditedVerticalImageHistogram = QPushButton('',self)
        btnLayoutEditedVerticalImageHistogram.move(1060,480)
        btnLayoutEditedVerticalImageHistogram.setFixedWidth(260)
        btnLayoutEditedVerticalImageHistogram.setFixedHeight(260)
        btnLayoutEditedVerticalImageHistogram.setStyleSheet('border: 1px solid purple;')
        
        
        pixmap = QPixmap('TesteBoat.bmp').scaled(250,250, QtCore.Qt.IgnoreAspectRatio)
        self.imageViewOriginal = QLabel('',self)
        self.imageViewOriginal.move(50,210)       
        self.imageViewOriginal.setFixedWidth(250)
        self.imageViewOriginal.setFixedHeight(250)
        self.imageViewOriginal.setPixmap(pixmap)
        
        self.imageViewEdited = QLabel('',self)
        self.imageViewEdited.move(510,210)       
        self.imageViewEdited.setFixedWidth(250)
        self.imageViewEdited.setFixedHeight(250)
        self.imageViewEdited.setPixmap(pixmap)
        
        self.imageViewEditedHorizontal = QLabel('',self)
        self.imageViewEditedHorizontal.move(785,210)       
        self.imageViewEditedHorizontal.setFixedWidth(250)
        self.imageViewEditedHorizontal.setFixedHeight(250)
        #self.imageViewEditedHorizontal.setPixmap(pixmap)
        
        self.imageViewEditedVertical = QLabel('',self)
        self.imageViewEditedVertical.move(1065,210)       
        self.imageViewEditedVertical.setFixedWidth(250)
        self.imageViewEditedVertical.setFixedHeight(250)
        #self.imageViewEditedVertical.setPixmap(pixmap)
        
        

        #criando as acoes
        @pyqtSlot()
        def on_btnExitClick():
            self.close()
            
        @pyqtSlot()
        def on_btnProcessClick():
            operation = self.mapFilter.get(self.cbxFilter.currentIndex(),'None')
            sucess = False
            sucessGradient = False
                     
            if (operation == "Binarizacao"):
                binarizacao.execute(self.edtPath.text())
                self.graphType = self.graphNormalValue
                sucess = True
            elif (operation == "Media"):
                filtroMedia.execute(self.edtPath.text())
                self.graphType = self.graphTinyValue
                sucess = True
            elif (operation == "Mediana"):
                filtroMediana.execute(self.edtPath.text())
                self.graphType = self.graphTinyValue
                sucess = True
            elif (operation == "Moda"):
                filtroModa.execute(self.edtPath.text())
                self.graphType = self.graphTinyValue
                sucess = True
            elif (operation == "Ordem-k"):
                filtroOrdemK.execute(self.edtPath.text(),int(self.edtCustomValue.text()))
                self.graphType = self.graphTinyValue
                sucess = True
            elif (operation == "Passa Alta - Laplaciano"):
                filtroPassaAltaLaplace.execute(self.edtPath.text())
                self.graphType = self.graphTinyValue
                sucess = True
            elif (operation == "Operadores de Sobel"):
                filtroSobel.execute(self.edtPath.text())
                sucess = True
                sucessGradient = True
                self.graphType = self.graphTinyValue
                self.graphTypeHorizontal = self.graphTinyValue
                self.graphTypeVertical = self.graphTinyValue
            elif (operation == "Operadores de Roberts"):
                filtroRoberts.execute(self.edtPath.text())
                sucess = True
                sucessGradient = True
                self.graphType = self.graphTinyValue
                self.graphTypeHorizontal = self.graphTinyValue
                self.graphTypeVertical = self.graphTinyValue
            elif (operation == "Operadores de Prewitt"):
                filtroPrewitt.execute(self.edtPath.text())
                sucess = True
                sucessGradient = True
                self.graphType = self.graphTinyValue
                self.graphTypeHorizontal = self.graphTinyValue
                self.graphTypeVertical = self.graphTinyValue
            elif (operation == "Equalizacao de Histograma"):
                equalizacaoHistograma.execute(self.edtPath.text())
                sucess = True
                self.graphType = self.graphTinyValue
            elif (operation == "Quantizacao"):
                quantizacaoValue = int(self.edtCustomValue.text())
                if (quantizacaoValue <= 0):
                    quantizacaoValue = 128
                quantizacao.execute(self.edtPath.text(),quantizacaoValue)
                sucess = True
                self.graphType = self.graphTinyValue
            
            if (sucess == True):
                pixmapEdited = QPixmap('result.bmp').scaled(250,250, QtCore.Qt.IgnoreAspectRatio)
                self.imageViewEdited.setPixmap(pixmapEdited)
                self.imgLoaded = True
                
            if (sucessGradient == True):
                pixmapEditedHorizontal = QPixmap('resultHorizontal.bmp').scaled(250,250, QtCore.Qt.IgnoreAspectRatio)
                self.imageViewEditedHorizontal.setPixmap(pixmapEditedHorizontal)
                pixmapEditedVertical = QPixmap('resultVertical.bmp').scaled(250,250, QtCore.Qt.IgnoreAspectRatio)
                self.imageViewEditedVertical.setPixmap(pixmapEditedVertical)
                self.imgGradientLoaded = True
            else:
                pixmapHorizontalVertical = QPixmap()
                self.imageViewEditedHorizontal.setPixmap(pixmapHorizontalVertical)
                self.imageViewEditedVertical.setPixmap(pixmapHorizontalVertical)
                self.indexHorizontal = None
                self.indexVertical = None
                self.imgGradientLoaded = False
        
        @pyqtSlot()
        def on_btnLoadClick():
            pixmapNew = QPixmap(self.edtPath.text()).scaled(250,250, QtCore.Qt.IgnoreAspectRatio)
            self.imageViewOriginal.setPixmap(pixmapNew)
            self.imageViewEdited.setPixmap(pixmapNew)
                       
        #conectando os eventos aos slots
        btnExit.clicked.connect(on_btnExitClick)
        btnProcess.clicked.connect(on_btnProcessClick)
        btnLoad.clicked.connect(on_btnLoadClick)  
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = WindowHome()
    main.showFullScreen()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
