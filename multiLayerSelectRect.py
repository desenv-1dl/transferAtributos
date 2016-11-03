# -*- coding: utf-8 -*-
from qgis.gui import *
from qgis.core import *
from PyQt4.Qt import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QShortcut, QKeySequence

class MultiLayerSelectRect(QgsMapTool):
    finishedSelection = QtCore.pyqtSignal(list)
    def __init__(self, canvas, iface):
        super(MultiLayerSelectRect, self).__init__(canvas)
        self.canvas = canvas
        self.iface = iface
        self.rubberBand = None
        self.listLayer = []
        self.initVariable()
           
    def initVariable(self):
        if self.rubberBand:
            self.rubberBand.reset(True)
            self.rubberBand = None
        self.startPoint = None
        self.endPoint = None
        self.qntPoint = 0
        self.listLayer = []
        self.rect = None
        
    def showCircle(self, startPoint, endPoint):
        rect = [[startPoint.x(), startPoint.y()], [endPoint.x(), startPoint.y()], [endPoint.x(), endPoint.y()], [startPoint.x(), endPoint.y()]]
        self.rubberBand.reset(QGis.Polygon)
        for point in rect:
            self.rubberBand.addPoint(QgsPoint(point[0], point[1]))
  
    def canvasPressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if not self.startPoint:
                self.startPoint = QgsPoint(event.mapPoint())
                self.rubberBand = self.getRubberBand()
                
    def getMax(self):
        x = max(self.startPoint.x(), self.endPoint.x())
        y = max(self.startPoint.y(), self.endPoint.y())
        return QgsPoint(x, y)
    
    def getMin(self):
        x = min(self.startPoint.x(), self.endPoint.x())
        y = min(self.startPoint.y(), self.endPoint.y())
        return QgsPoint(x, y)
    
    def canvasReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if  self.startPoint and self.endPoint:            
                pmin = self.getMin()
                pmax = self.getMax()
                rect = QgsRectangle(pmin.x(), pmin.y(), pmax.x(), pmax.y())
                layers = self.canvas.layers()
                for layer in layers:
                    if (layer.type() == QgsMapLayer.RasterLayer) or (layer.name()[-1].isdigit()):
                        continue
                    else:
                        lRect = self.canvas.mapSettings().mapToLayerCoordinates(layer, rect)               
                        layer.select(lRect, False)
                        if layer.selectedFeatureCount() > 0:
                            self.listLayer.append(layer.name())
                self.finishedSelection.emit(self.listLayer)
                self.initVariable()
            else:
                self.initVariable()
                        
    def canvasMoveEvent(self, event):
        if self.startPoint:
            self.endPoint = QgsPoint(event.mapPoint())
            self.showCircle(self.startPoint, self.endPoint)
            
    def getRubberBand(self):
        rubberBand = QgsRubberBand(self.canvas, True)
        rubberBand.setFillColor(QColor(255, 0, 0, 40))
        rubberBand.setBorderColor(QColor(255, 0, 0, 200))
        rubberBand.setWidth(2)
        return rubberBand
    
    def removeSelecoes(self):
        for i in range(len(self.canvas.layers())):
            try:
                self.canvas.layers()[i].removeSelection()
            except:
                pass