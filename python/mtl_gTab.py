from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class MTL_View(QGraphicsView):
    def __init__(self,parent,name):
        #self.setScene(self._scene)
        QGraphicsView.__init__(self,parent,name)
        aut=QImage("C:/Users/LeePhan/Documents/GitHub/pickerLeeMTV/icon/author1")
        self._scene=QGraphicsScene()
        self.setScene(self._scene)
        self._scene.setBackgroundBrush(aut)
        self.installEventFilter(self)

    def eventFilter(self,source,e):
        #event 
        if e.type()==QEvent.Leave:
            print("leave...")
        elif e.type()==QEvent.Enter:
            print("enter...")
        elif e.type()==QEvent.GraphicsSceneMouseMove:
            self.gCursor=e.pos()
            self.gScenePos=e.scenePos()
            if self.gScenePos and self.isMidle and not self.isLock:
                rX,rY=self.__deltaDrag()
                rect=QRect()
                rect.setX(round(rX,2))
                rect.setY(round(rY,2))
                maxsizeX=QMainWindow(self.activeWindow()).width()/2
                maxsizeY=QMainWindow(self.activeWindow()).height()/2
                if rect.size().width() < maxsizeX and rect.size().height() < maxsizeY:
                    self.setSceneRect(rect)
            pass#print("move... %d "%self.move)
        elif e.type()==QEvent.GraphicsSceneMousePress:
            if e.button()==Qt.LeftButton:
                print("left click.")
            if e.button()==Qt.RightButton:
                print("right click.")
            if e.button()==Qt.MidButton:
                self.gView.viewport().setCursor(Qt.ClosedHandCursor)
                self.isMidle=True
                print("midle click.")

            #print("click..")
        elif e.type()==QEvent.GraphicsSceneMouseRelease:
            if e.button()==Qt.LeftButton:
                print("left release.")
            if e.button()==Qt.RightButton:
                print("right release.")
            if e.button()==Qt.MidButton:
                self.gView.viewport().setCursor(Qt.ArrowCursor)
                self.isMidle=False
                print("midle release.")


class mtl_gTab(QWidget):
    def __init__(*args, **kwargs):
        super().__init__(**kwargs)