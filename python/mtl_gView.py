from PySide2 import QtCore,QtGui,QtWidgets,QtNetwork

class MTL_View(QtWidgets.QGraphicsView):

    def __init__(self,parent=QtWidgets.QWidget):
        QtWidgets.QGraphicsView.__init__(self,parent=None)
        if parent: self.setParent(parent)
    
