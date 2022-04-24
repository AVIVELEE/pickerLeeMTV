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
    iBgrColor=None  
    def __init__(self, parent = None,iName=None,img=None,ID=None):
        QGraphicsItem.__init__(self,parent)
        if iName: self.iName=iName
        if ID: self.IDnumber=ID
        self.setFlag(QGraphicsItem.ItemIsMovable,True)
        self.setFlag(QGraphicsItem.ItemIsSelectable,True)
        self.setAcceptHoverEvents(True)
        self.setZValue(1)
        self.acceptedMouseButtons()
        self.setCacheMode(QGraphicsItem.ItemCoordinateCache)
        self.setFlag(QGraphicsItem.ItemIsFocusable,True)
        if img:
            self.iPng=img
            self.setTransformOriginPoint(QPointF(self.iRect.center()))
            #self.iRect=QImage(img).rect()
        #print("log : %s"%QFile(self.iPng).exists())

    def paint(self, painter=QPainter, options=None, widget=None):
        self.painting(painter)
        if self.isUnderMouse():
            self.onSelected(painter)
        
    #     #QGraphicsItem.paint(painter,options,widget)
    #     #return QGraphicsItem.paint(self,painter,options,widget)

    def hoverEnterEvent(self,event):
        self.isHighLight=True
        print("Hover...")
        return QGraphicsItem.hoverEnterEvent(self,event)

    def hoverLeaveEvent(self,event):
        self.isHighLight=False
        print("Hover Leave..")
        return QGraphicsItem.hoverLeaveEvent(self,event)

    def boundingRect(self):
        if not QImage(self.iPng).isNull():
            iRect=QRect(QImage(self.iPng).rect())
            self.iRect=QRect(iRect.x(),iRect.y(),iRect.width()/10,iRect.height()/10)
        return self.iRect

    def mousePressEvent(self, event=QMouseEvent):
        if event.button()==Qt.RightButton:
            if self.isUnderMouse():
                self.itemContextMenu(event.screenPos())
        return QGraphicsItem.mousePressEvent(self,event)


    #paint when selected
    def onSelected(self,Painter=QPainter):
        if self.isSelected():
            self.setCacheMode(QGraphicsItem.DeviceCoordinateCache)
            mask=QPen(Qt.white)
            mask.setWidth(4)
            Painter.setPen(mask)
            Painter.drawRect(self.iRect)
    
    #paint runtime
    def painting(self,painter=QPainter):
        if not QFile.exists(self.iPng):
            painter.drawRect(self.iRect)
            painter.fillRect(self.iRect,self.iColor)
            painter.setPen(self.textColor)
            painter.setFont(QFont("Arial", self.textSize, QFont.Bold))
            #painter.setRenderHint(QPainter.HighQualityAntialiasing,True)
            painter.drawText(self.iRect,Qt.AlignCenter,"ABC")
        else:
            pixmap=QPixmap.fromImage(QImage(self.iPng),Qt.AutoColor)
            painter.drawPixmap(self.iRect,pixmap)
        # painter.setPen(self.textColor)
        # painter.setFont(QFont("Arial", self.textSize, QFont.Bold))
        
        if self.isUnderMouse():
            self.onSelected(painter)
        
        if self.iBgrColor:
            painter.fillRect(self.iRect,self.iBgrColor)

    def itemContextMenu(self,pos):
        menu=QMenu()
        menu.addAction("assign selection",self.mayaAssignSelection)
        menu.addAction("change image",self.onChangeImage)
        menu.exec_(pos)

    def mayaAssignSelection(self):
        print("selection assigned..")

    def onChangeImage(self):
        imgFilter="image (*.png)"
        fname,_=QFileDialog.getOpenFileName(self.parentWidget(),"image choise","c:\\\Users\\\LeePhan\\Documents\\maya\\iTools","All files (*.*);;JPEG (*.jpg *.jpeg);;TIFF (*.tif);;PNG (*.png)",imgFilter)
        if fname !="":
            self.iPng=fname
            self.iRect=QImage(self.iPng).rect()
            self.update()
