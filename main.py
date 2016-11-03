# -*- coding: utf-8 -*-
import os

# Qt imports
import psycopg2
from PyQt4 import QtGui, uic, QtCore
from qgis.core import QgsPoint , QgsDataSourceURI, QgsVectorLayer, QgsMapLayerRegistry
from qgis.gui import QgsMessageBar, QgsMapTool
from PyQt4.QtCore import QSettings, pyqtSignal, pyqtSlot, SIGNAL, QObject, QSize
from PyQt4.QtGui import QIcon, QMessageBox, QCursor, QPixmap, QAction
from icons import icon1, icon2
from multiLayerSelect import MultiLayerSelection
from multiLayerSelectRect import MultiLayerSelectRect
from interface_copyPaste import CopyPaste

class Main:
    def __init__(self, iface):
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.tool1 = MultiLayerSelection(self.iface.mapCanvas(), self.iface)
    
    def initGui(self):
        self.action1 = QAction(QIcon(icon1), u"selecionar feições", self.iface.mainWindow())
        self.action2 = QAction(QIcon(icon2), u"Transfer-Atributos", self.iface.mainWindow())
        self.iface.digitizeToolBar().addAction(self.action1)
        self.iface.digitizeToolBar().addAction(self.action2)
        self.action1.triggered.connect(self.selectMulti)
        self.action2.triggered.connect(self.copyPaste)
        self.iface.actionToggleEditing().triggered.connect(self.closeCursor)
  
    def unload(self):
        pass
        
    def closeCursor(self, a):
        if not a:
            self.canvas.unsetMapTool(self.tool1)
            self.canvas.unsetCursor()
            self.removeSelecoes()
                          
    def selectMulti(self):
        self.iface.mapCanvas().setMapTool(self.tool1)
    
    def copyPaste(self):
        if (self.iface.activeLayer()) and (len(self.iface.activeLayer().selectedFeatures()) == 1):
            layer = self.iface.activeLayer().selectedFeatures()[0]
            dialog = QtGui.QDialog(self.iface.mainWindow())
            self.d = CopyPaste(self.iface, layer, dialog)
            self.d.show()
        else:
            self.iface.messageBar().pushMessage(u"Atenção", u"Selecione apenas uma feição",
                                                level=QgsMessageBar.INFO, duration=10)
              
    def removeSelecoes(self):
        for i in range(len(self.canvas.layers())):
            try:
                self.canvas.layers()[i].removeSelection()
            except:
                pass
        
    
       