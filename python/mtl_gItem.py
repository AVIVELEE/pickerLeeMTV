from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class mtl_GraphicsItem(QGraphicsItem):
    
    # def __init__(self,parent=None):
    #     super(mtl_GraphicsItem,self).__init__()


    def __init__(self, parent = None):
        QGraphicsItem.__init__(self,parent)
        self.setFlag(QGraphicsItem.ItemIsMovable)

    def paint(self, painter, options, widget):
        rect=QRect(-30, -30, 30, 30)
        painter.drawRect(rect)
        painter.fillRect(rect,QBrush(Qt.red))
        return QGraphicsItem.paint(self,painter,options,widget)

    def boundingRect(self):
        return QRectF(self.x() - 10, self.y() - 10, 50, 50)