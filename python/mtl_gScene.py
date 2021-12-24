import decimal
import sys
from PySide2 import QtCore,QtGui,QtWidgets,QtNetwork
from decimal import Decimal

import PySide2

#custom qt graphcisview
class MTL_Scene(QtWidgets.QGraphicsScene):
    isLock=False
    def __init__(self,parent=QtWidgets.QWidget,name=None):
        QtWidgets.QGraphicsScene.__init__(self)
        self.setObjectName(name)
        self.setParent(parent)
        self.mouseGrabberItem()
        aut=QtGui.QImage("C:/Users/LeePhan/Documents/GitHub/PhanLee-Picker/icon/author1")
        self.setForegroundBrush(aut)
        self.move=0
        self.press="click.."
        self.gScenePos=0.0
        self.gCursor=0.0
        self.gView=self.parent()
        self.isMidle=False
        self.isEnter="cccc.."
        #self.setDr()
        print("# METALEE : %s #"%self.isEnter)
        #lock scene
        
        print("# METALEE : Scene is Created. #")

    #mouse move event 
    def mouseMoveEvent(self,event):
        self.move+=1
        self.gCursor=event.pos()
        self.gScenePos=event.scenePos()
        #print("# METALEE : %d , 2log ->  %d #"%(decimal.Decimal(10),decimal.Decimal(5)))

        if self.gScenePos and self.isMidle and not self.isLock:
            try:
                nRect=self.__deltaDrag()
                self.setSceneRect(nRect)
            except OverflowError as er:
                print((nRect))
        #QtWidgets.QGraphicsScene(self).mouseMoveEvent(event)

    #mouse press event
    def mousePressEvent(self,event=QtGui.QMouseEvent):
        if event.button()==QtCore.Qt.LeftButton:
            
            pass #print("# METALEE : left clicked %s #"%self.press)
        elif event.button()==QtCore.Qt.RightButton:
            pass #print("# METALEE : right clicked %s #"%self.press)
        elif event.button()==QtCore.Qt.MidButton:
            self.gScenePos=event.scenePos()
            self.gView.viewport().setCursor(QtCore.Qt.ClosedHandCursor)
            self.isMidle=True
        #elif event.button() == QtCore.Qt.RightButton:
            
        #on midle clicked 
        

    #mouse release event
    def mouseReleaseEvent(self,event):
        if event.button()==QtCore.Qt.LeftButton:
            self.gView.setDragMode(QtWidgets.QGraphicsView.NoDrag)
            pass #print("# METALEE : left release #")
        elif event.button() == QtCore.Qt.RightButton:
            pass #print("# METALEE : right release #")
        elif event.button() == QtCore.Qt.MidButton:
            self.gView.viewport().setCursor(QtCore.Qt.ArrowCursor)
            self.isMidle=False

    #wheelEvent E
    def wheelEvent(self,event):
        if MTL_Scene.isLock: return
        deltaScale,result=self.__deltaScale(event)
        if deltaScale: self.gView.scale(deltaScale,deltaScale)
        if result: self.gView.translate(result.x(),result.y())
        self.gView.update()

    #calulate zoom in / zoom out scene
    def __deltaScale(self,event):
        result=QtCore.QPointF()
        deltaScale=1.0
        temp=self.gView.transform().m11()
        if event.delta() > 0:
            if temp > 5 and deltaScale > .85: deltaScale+=0.0
            else: deltaScale+=0.15
        else: deltaScale +=-0.15
        #self.setSceneRect(deltaScale)
        self.gScenePos=event.scenePos()
        result=self.gScenePos-self.gCursor
        return deltaScale,result
        #return super(MTL_Scene,self).wheelEvent(event)
    # def wheelEvent (event)
    # midle mouse drag
    def __deltaDrag(self):
        delta=self.gScenePos-self.gCursor
        # newX=self.gView.horizontalScrollBar().value()
        # newY=self.gView.verticalScrollBar().value()
        # nX=newX + delta.x()
        # nY=newY + delta.y()
        trans=self.gView.transform()
        deltaX=delta.x()/trans.m11()
        deltaY=delta.y()/trans.m22()
        rect=QtCore.QRectF()
        rect.setX(-deltaX)
        rect.setY(-deltaY)
        # self.gView.horizontalScrollBar().setValue(long(nX))
        # self.gView.verticalScrollBar().setValue(long(nY))
        return rect
        print("# METALEE : %d, %d #"%(deltaX,deltaY),self.sceneRect())
        # if newX !=0: self.gView.horizontalScrollBar().setValue(nX)
        # if newY !=0: self.gView.verticalScrollBar().setValue(nY)
        # if self.isActive(): print("# METALEE : is active #")
    