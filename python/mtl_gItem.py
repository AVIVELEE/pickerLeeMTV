from turtle import bgcolor
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys,os,imp
sys.path.append("C:/Users/%s/Documents/GitHub/pickerLeeMTV/python"%os.environ["USER"])
import mtl_gGlobal as mtl

class mtl_GraphicsItem(QGraphicsItem):
    
    # def __init__(self,parent=None):
    #     super(mtl_GraphicsItem,self).__init__()
    IDnumber=-1
    iPng="C:/Users/LeePhan/Documents/GitHub/pickerLeeMTV/icon/simple_geo/ceo.png"
    iName=""
    iColor=Qt.blue
    iRect=QRect(-40, -40, 40, 40)
    textSize=12
    textColor=Qt.white
    isHighLight=False
    down=1
    isOpacDown=False
    iBgrColor=QColor()  
    def __init__(self, parent = None,iName=None,img=None,ID=None):
        QGraphicsItem.__init__(self,parent)
        if iName: self.iName=iName
        if ID: self.IDnumber=ID
        self.setFlag(QGraphicsItem.ItemIsMovable,True)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setAcceptHoverEvents(True)
        self.setZValue(1)
        self.acceptedMouseButtons()
        if img:
            self.iPng=img
            self.setTransformOriginPoint(QPointF(self.iRect.center()))
            #self.iRect=QImage(img).rect()
        #print("log : %s"%QFile(self.iPng).exists())

    def paint(self, painter=QPainter, options=None, widget=None):
        if not QFile.exists(self.iPng):
            painter.drawRect(self.iRect)
            painter.fillRect(self.iRect,self.iColor)
            painter.setPen(self.textColor)
            painter.setFont(QFont("Arial", self.textSize, QFont.Bold))
            #painter.setRenderHint(QPainter.HighQualityAntialiasing,True)
            painter.drawText(self.iRect,Qt.AlignCenter,"ABC")
        else:
            painter.drawPixmap(self.iRect,QPixmap.fromImage(QImage(self.iPng),Qt.AutoColor))
        # painter.setPen(self.textColor)
        # painter.setFont(QFont("Arial", self.textSize, QFont.Bold))
        self.onSelected(painter)
        if self.isOpacDown:
            self.down-=0.02
            #self.setOpacity(self.down)
            QTimer.singleShot(200, lambda: self.setOpacity(self.down))
        if self.down <=0:
            self.scene.removeItem(self)
        
        if self.iBgrColor:
            painter.fillRect(self.iRect,self.iBgrColor)
        #return QGraphicsItem.paint(self,painter,options,widget)

    def hoverEnterEvent(self,event):
        self.isHighLight=True
        print("Hover...")
        return QGraphicsItem.hoverEnterEvent(self,event)
    def hoverLeaveEvent(self,event):
        self.isHighLight=False
        print("Hover Leave..")
        return QGraphicsItem.hoverLeaveEvent(self,event)
    def boundingRect(self):
        # if self.iPng:
        #     self.iRect=QRect(0,0,550,656)
        #     return self.iRect
        return self.iRect

    def onSelected(self,Painter=QPainter):
        if self.isSelected():
            mask=QPen(Qt.white)
            mask.setWidth(2)
            Painter.setPen(mask)
            Painter.drawRect(self.iRect)
        

