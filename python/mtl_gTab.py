import imp
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys,os,imp
sys.path.append("C:/Users/%s/Documents/GitHub/pickerLeeMTV/python"%os.environ["USER"])

from mtl_gItem import mtl_GraphicsItem

class MTL_View(QGraphicsView):
    def __init__(self,parent,name):
        #self.setScene(self._scene)
        QGraphicsView.__init__(self,parent,name)
        #aut=QImage("C:/Users/LeePhan/Documents/GitHub/pickerLeeMTV/icon/author1")
        self._scene=MTL_Scene()
        self.setScene(self._scene)
        #self._scene.setBackgroundBrush(aut)
        self.isMidle=False
        self.isLock=False
        self.setMouseTracking(True)
        #self.installEventFilter(self)

    def mouseMoveEvent(self,event=QMouseEvent):
        self.gCursor=event.pos()
        self.gScenePos=event.globalPos()
        #print("# METALEE : %d , 2log ->  %d #"%(decimal.Decimal(10),decimal.Decimal(5)))
        print("Moving...")
        if self.gScenePos and self.isMidle and not self.isLock:
            try:
                #nRect=self.__deltaDrag()
                pass
                #self.setSceneRect(nRect)
            except OverflowError as er:
                pass
        return QGraphicsView.mouseMoveEvent(self,event)

    #mouse press event
    def mousePressEvent(self,event=QMouseEvent):
        if event.button()==Qt.LeftButton:
            print("# METALEE : left clicked #")
            pass #print("# METALEE : left clicked %s #"%self.press)
        elif event.button()==Qt.RightButton:
            pass #print("# METALEE : right clicked %s #"%self.press)
        elif event.button()==Qt.MidButton:
            self.gScenePos=event.screenPos()
            self.viewport().setCursor(Qt.ClosedHandCursor)
            self.isMidle=True
        #elif event.button() == QtCore.Qt.RightButton:
        return QGraphicsView.mousePressEvent(self,event)   
        #on midle clicked 
        

    #mouse release event
    def mouseReleaseEvent(self,event):
        if event.button()==Qt.LeftButton:
            self.setDragMode(QGraphicsView.NoDrag)
            print("# METALEE : left release. #")
            pass 
        elif event.button() == Qt.RightButton:
            pass #print("# METALEE : right release #")
        elif event.button() == Qt.MidButton:
            self.viewport().setCursor(Qt.ArrowCursor)
            self.isMidle=False
        return QGraphicsView.mouseReleaseEvent(self,event)   

    # def eventFilter(self,source,e):
    #     #event 
    #     if e.type()==QEvent.Leave:
    #         print("leave...")
    #     elif e.type()==QEvent.Enter:
    #         print("enter...")
    #     elif e.type()==QEvent.GraphicsSceneMouseMove:
    #         self.gCursor=e.pos()
    #         self.gScenePos=e.scenePos()
    #         if self.gScenePos and self.isMidle and not self.isLock:
    #             rX,rY=self.__deltaDrag()
    #             rect=QRect()
    #             rect.setX(round(rX,2))
    #             rect.setY(round(rY,2))
    #             maxsizeX=QMainWindow(self.activeWindow()).width()/2
    #             maxsizeY=QMainWindow(self.activeWindow()).height()/2
    #             if rect.size().width() < maxsizeX and rect.size().height() < maxsizeY:
    #                 self.setSceneRect(rect)
    #         pass#print("move... %d "%self.move)
    #     elif e.type()==QEvent.GraphicsSceneMousePress:
    #         if e.button()==Qt.LeftButton:
    #             print("left click.")
    #         if e.button()==Qt.RightButton:
    #             print("right click.")
    #         if e.button()==Qt.MidButton:
    #             self.viewport().setCursor(Qt.ClosedHandCursor)
    #             self.isMidle=True
    #             print("midle click.")

    #         #print("click..")
    #     elif e.type()==QEvent.GraphicsSceneMouseRelease:
    #         if e.button()==Qt.LeftButton:
    #             print("left release.")
    #         if e.button()==Qt.RightButton:
    #             print("right release.")
    #         if e.button()==Qt.MidButton:
    #             self.viewport().setCursor(Qt.ArrowCursor)
    #             self.isMidle=False
    #             print("midle release.")
    # def __deltaDrag(self):
    #     delta=self.gScenePos-self.gCursor
    #     # newX=self.gView.horizontalScrollBar().value()
    #     # newY=self.gView.verticalScrollBar().value()
    #     # nX=newX + delta.x()
    #     # nY=newY + delta.y()
    #     trans=self.transform()
    #     deltaX=delta.x()/trans.m11()
    #     deltaY=delta.y()/trans.m22()
    #     rect=QRectF()
    #     rect.setX(-deltaX)
    #     rect.setY(-deltaY)
    #     # self.gView.horizontalScrollBar().setValue(long(nX))
    #     # self.gView.verticalScrollBar().setValue(long(nY))
    #     return rect
    #     print("# METALEE : %d, %d #"%(deltaX,deltaY),self.sceneRect())
    #     # if newX !=0: self.gView.horizontalScrollBar().setValue(nX)
    #     # if newY !=0: self.gView.verticalScrollBar().setValue(nY)
    #     # if self.isActive(): print("# METALEE : is active #")


class MTL_Scene(QGraphicsScene):
    isLock=False
    def __init__(self,parent=QWidget,name=None):
        QGraphicsScene.__init__(self)
        self.mouseGrabberItem()
        aut=QImage("C:/Users/LeePhan/Documents/GitHub/pickerLeeMTV/icon/author1")
        self.setForegroundBrush(aut)
        self.move=0
        self.press="click.."
        self.gScenePos=0.0
        self.gCursor=0.0
        self.gView=self.parent()
        self.isMidle=False
        self.isEnter="cccc.."
        self.mouseGrabberItem()
        #self.setDr()
        print("# METALEE : %s #"%self.isEnter)
        ##self.installEventFilter(self)
        #lock scene
        item=mtl_GraphicsItem()
        self.addItem(item)
        print("# METALEE : Scene is Created. #")
    # def eventFilter(self,source,e):
    #     if e.type()==QEvent.GraphicsSceneMouseMove:
    #         print("moving..")
    #     return QGraphicsScene.eventFilter(self,source,e)            
        #event 
        # if e.type()==QEvent.Leave:
        #     print("leave...")
        # elif e.type()==QEvent.Enter:
        #     print("enter...")
        # elif e.type()==QEvent.GraphicsSceneMouseMove:
        #     self.gCursor=e.pos()
        #     self.gScenePos=e.scenePos()
        #     if self.gScenePos and self.isMidle and not self.isLock:
        #         rX,rY=self.__deltaDrag()
        #         rect=QRect()
        #         rect.setX(round(rX,2))
        #         rect.setY(round(rY,2))
        #         maxsizeX=QMainWindow(self.activeWindow()).width()/2
        #         maxsizeY=QMainWindow(self.activeWindow()).height()/2
        #         if rect.size().width() < maxsizeX and rect.size().height() < maxsizeY:
        #             self.setSceneRect(rect)
        #     pass#print("move... %d "%self.move)
        # elif e.type()==QEvent.GraphicsSceneMousePress:
        #     if e.button()==Qt.LeftButton:
        #         print("left click.")
        #     if e.button()==Qt.RightButton:
        #         print("right click.")
        #     if e.button()==Qt.MidButton:
        #         self.viewport().setCursor(Qt.ClosedHandCursor)
        #         self.isMidle=True
        #         print("midle click.")

        #     #print("click..")
        # elif e.type()==QEvent.GraphicsSceneMouseRelease:
        #     if e.button()==Qt.LeftButton:
        #         print("left release.")
        #     if e.button()==Qt.RightButton:
        #         print("right release.")
        #     if e.button()==Qt.MidButton:
        #         self.viewport().setCursor(Qt.ArrowCursor)
        #         self.isMidle=False
        #         print("midle release.")
        # return QGraphicsScene.eventFilter(self,source,e)