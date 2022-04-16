from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class mtl_GraphicsItem(QGraphicsItem):
    
    # def __init__(self,parent=None):
    #     super(mtl_GraphicsItem,self).__init__()
    IDnumber=-1
    iPng="C:/Users/LeePhan/Documents/GitHub/pickerLeeMTV/icon/simple_geo/jointik.png"
    iName=""
    iColor=Qt.blue
    iRect=QRect(-40, -40, 40, 40)
    textSize=12
    textColor=Qt.white
    
    def __init__(self, parent = None,iName=None,img=None,ID=None):
        QGraphicsItem.__init__(self,parent)
        self.setFlag(QGraphicsItem.ItemIsMovable,True)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setAcceptHoverEvents(True)
        self.setZValue(1)
        self.acceptedMouseButtons()
        print("log : %s"%QFile(self.iPng).exists())

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

        return QGraphicsItem.paint(self,painter,options,widget)

    def boundingRect(self):
        return self.iRect