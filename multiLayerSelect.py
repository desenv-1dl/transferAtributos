# -*- coding: utf-8 -*-
from qgis.gui import *
from qgis.core import *
from PyQt4.Qt import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QShortcut, QKeySequence

class MultiLayerSelection(QgsMapTool):
	finished = QtCore.pyqtSignal(list)
	def __init__(self, canvas, iface):
		self.iface=iface        
		self.canvas = canvas
		self.free = False
		self.selecaoMulti=[]
		QgsMapTool.__init__(self, self.canvas)
		
	def getSelectionsLayers(self):
		self.selecaoVariada =  list(set( self.selecaoVariada ))
		return self.selecaoVariada
	
	def setSelectionsLayers(self, name):
		self.selecaoVariada.append(name)
	
	def keyReleaseEvent(self, event):
		if event.key() == Qt.Key_Control:
		    self.free = False

	def keyPressEvent(self, event):
	    if event.key() == Qt.Key_Control:
	        self.free = True
	   
	def canvasPressEvent(self, e):
		if not self.free:
			self.removerSelecoes()
		layers = self.canvas.layers()	
		layer2 = QgsMapLayerRegistry.instance().mapLayers()	
		grupo={}
		for x in range(len(layer2)):
			grupo[layer2.keys()[x][:-17]]=layer2.get(layer2.keys()[x])    		
		p = self.toMapCoordinates(e.pos())
		w = self.canvas.mapUnitsPerPixel() * 10
		rect = QgsRectangle(p.x()-w, p.y()-w, p.x()+w, p.y()+w)
		for layer in layers:
			if (layer.type() == QgsMapLayer.RasterLayer) or (layer.name() == 'moldura'):
				continue
			else:
				lRect = self.canvas.mapSettings().mapToLayerCoordinates(layer, rect)			   
				layer.select(lRect, False)
				if (self.free) and (layer.selectedFeatureCount() >= 1):
					self.setSelectionsLayers(layer.name())
					self.iface.setActiveLayer(grupo.get(layer.name()))
					self.iface.activeLayer().startEditing()
				elif layer.selectedFeatureCount() == 1:
					self.setSelectionsLayers(layer.name())
					self.iface.setActiveLayer(grupo.get(layer.name()))
					self.iface.activeLayer().startEditing()
		selectionsLayers = self.getSelectionsLayers()
		if not self.free:
			self.hasMoreThanOneSelection(selectionsLayers)
		self.finished.emit(selectionsLayers)
			
					
	def hasMoreThanOneSelection(self, selections):
		layer2 = QgsMapLayerRegistry.instance().mapLayers()	
		grupo={}
		for x in range(len(layer2)):
			if layer2.keys()[x][:-17] in selections:
				grupo[layer2.get(layer2.keys()[x]).geometryType()]=layer2.get(layer2.keys()[x])
		print grupo				
		if 0 in grupo:
			if not (len(grupo[0].selectedFeatures()) == 1):
				grupo[0].selectedFeatures()
			if 1 in grupo:
				grupo[1].removeSelection()
			if 2 in grupo:
				grupo[2].removeSelection()	
		elif 1 in grupo:
			if not (len(grupo[1].selectedFeatures()) == 1):
				grupo[1].selectedFeatures()
			if 2 in grupo:
				grupo[2].removeSelection()						
		elif 2 in grupo:
			if not (len(grupo[2].selectedFeatures()) == 1):
				grupo[2].removeSelection()			
                       
	def deactivate(self):
		if self is not None:
			QgsMapTool.deactivate(self)

	def activate(self):
		QgsMapTool.activate(self)
	
	def removerSelecoes(self):
		for i in range(len(self.iface.mapCanvas().layers())):
			try:
				self.iface.mapCanvas().layers()[i].removeSelection()
			except:
				pass
		self.selecaoVariada=[]
	
		






