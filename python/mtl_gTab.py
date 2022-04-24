from cmath import rect
from multiprocessing import Event
import maya.cmds as cmds
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys,os,imp
from shiboken2 import wrapInstance
import maya.OpenMayaUI as mui

sys.path.append("C:/Users/%s/Documents/GitHub/pickerLeeMTV/python"%os.environ["USER"])

if "mtl_GraphicsItem" in sys.modules:
    imp.reload(sys.modules['mtl_GraphicsItem'])
if "mtl_Global" in sys.modules:
    imp.reload(sys.modules['mtl_Global'])
if "mtl_gItem" in sys.modules:
    imp.reload(sys.modules['mtl_gItem'])
from mtl_gGlobal import mtlGlobal    
from mtl_gItem import mtl_GraphicsItem


MTL=mtlGlobal()
# def info(message):
#     print("#META LEE : %s"%message)



class MTL_View(QGraphicsView):
    gScenePos=QPoint()
    gCursor=QPoint()
    def __init__(self,parent,name):
        #self.setScene(self._scene)
        QGraphicsView.__init__(self,parent,name)
        self.rubberband=QRubberBand(QRubberBand.Rectangle,self)
        self.origin=QPoint()
        aut=QImage("C:/Users/LeePhan/Documents/GitHub/pickerLeeMTV/icon/author1")
        self._scene=MTL_Scene()
        self.setScene(self._scene)
        #self._scene.setBackgroundBrush(aut)
        self.isMidle=False
        self.isLock=False
        self.isLeft=False
        #self.setMouseTracking(False)
        #self.installEventFilter(self)
        #self.setUpdatesEnabled(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setRubberBandSelectionMode(Qt.IntersectsItemBoundingRect)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setBackgroundBrush(aut)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setRubberBandSelectionMode(Qt.IntersectsItemShape)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        #self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.ToolBarConnection()
        self.setOptimizationFlags(QGraphicsView.DontAdjustForAntialiasing
                              | QGraphicsView.DontClipPainter
                              | QGraphicsView.DontSavePainterState)

    def mouseMoveEvent(self,event=QMouseEvent):
        self.gCursor=event.pos()
        self.gScenePos=event.globalPos()
        if self.rubberband.isVisible():
            self.rubberband.setGeometry(
                QRect(self.origin, event.pos()).normalized())
        #print("# METALEE : %d , 2log ->  %d #"%(decimal.Decimal(10),decimal.Decimal(5)))
        #print("Moving...")
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
            self.origin=event.pos()
            selectedItem=self._scene.getNumberSelectedItem()
            print("LOG : %d"%len(self._scene.selectedItems()))
            if selectedItem ==0:
                self.rubberband.show()
            self.isLeft=True
            print(self._scene.getNumberItem())

            #print("xyz : %s"%self._scene.selectedItems())
            # if self._scene.selectedItems() > 0:
            #     self.setMouseTracking(True)
            print("# METALEE : left clicked #")
            pass #print("# METALEE : left clicked %s #"%self.press)
        elif event.button()==Qt.RightButton:
            #item=self.creatFresh(event)
            pass #print("# METALEE : right clicked %s #"%self.press)
        elif event.button()==Qt.MidButton:
            self.gScenePos=event.screenPos()
            self.viewport().setCursor(Qt.ClosedHandCursor)
            self.isMidle=True
        #elif event.button() == QtCore.Qt.RightButton:
        return QGraphicsView.mousePressEvent(self,event)   
        #on midle clicked 
    
    #mouse release event
    def mouseReleaseEvent(self,event=QMouseEvent):
        if event.button()==Qt.LeftButton:
            self.isLeft=False
            self.setDragMode(QGraphicsView.NoDrag)
            self.rubberband.hide()
            pass 
        elif event.button() == Qt.RightButton:
            pass #print("# METALEE : right release #")
        elif event.button() == Qt.MidButton:
            self.viewport().setCursor(Qt.ArrowCursor)
            self.isMidle=False
        return QGraphicsView.mouseReleaseEvent(self,event)   

    def wheelEvent(self,event=QWheelEvent):
        if self.isLock: return event.ignore()
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        target=self.gScenePos- self.gCursor
        deltaS=1
        #templa=self.transform().m11()
        if event.delta() > 0:
            deltaS +=0.25
        else:
            deltaS-=0.25
        self.scale(deltaS,deltaS)
        self.translate(target.x(),target.y())
        #deltaS+=event.delta() > 0 ? 0.25 : -0.25
        return QGraphicsView.wheelEvent(self,event)

    def creatFresh(self,e=QMouseEvent):
        mItem=mtl_GraphicsItem(iName="fresh",img="C:/Users/LeePhan/Documents/GitHub/pickerLeeMTV/icon/simple_geo/fresh.png",ID=10)
        mItem.setTransformOriginPoint(mItem.iRect.center())
        self._scene.addItem(mItem)
        mItem.isOpacDown=True
        mItem.setZValue(2)
        mItem.iRect=QRect(0,0,100,100)
        cent=e.pos()-QRect(0,0,100,100).center()
        mItem.setPos(self.mapToScene(cent))
        #mItem.mapFromScene(self.gCursor)
        QTimer.singleShot(1000, lambda: self._scene.removeItem(mItem))

    def ToolBarConnection(self):
        toolbar=MTL.mWindowToQObject("mainToolBar",QToolBar)
        aColor=MTL.findActionFromToolBar("metaCustomColor",toolbar)
        #QAction.priority("ABC")
        aColor.triggered.connect(MTL.ColorDialog)

    
#region MTL Graphics Scene */
class MTL_Scene(QGraphicsScene):
    
    isLock=False
    def __init__(self,parent=QWidget,name=None):
        QGraphicsScene.__init__(self)
        #self.mouseGrabberItem()
        aut=QImage("C:/Users/LeePhan/Documents/GitHub/pickerLeeMTV/icon/author1")
        self.move=0
        self.press="click.."
        self.gScenePos=0.0
        self.gCursor=0.0
        self.gView=self.parent()
        self.isMidle=False
        self.mouseGrabberItem()
        MTL.createItem(self)
        # item=mtl_GraphicsItem()
        # item.iPng="C:/Users/LeePhan/Downloads/ceo.png"
        # self.addItem(item)
        # #item.iBgrColor=Qt.cyan
        # print(item.boundingRect())
        # item.iBgrColor=Qt.cyan
        
        #print("# METALEE : Scene is Created. #")
        #self.setColorAllItem()
        #self.setForegroundBrush(aut)

    def ToolBarConnection(self):
        toolbar=MTL.mWindowToQObject("mainToolBar",QToolBar)
        aColor=MTL.findActionFromToolBar("metaCustomColor",toolbar)
        QAction.priority("ABC")
        aColor.triggered.connect(MTL.ColorDialog)

    #set all item bgr Color
    def setBGRColorAllItem(self,newColor=QColor):
        if len(self.items()) > 0:
            for n,item in enumerate(self.items()):
                mtl=mtl_GraphicsItem(item)
                if mtl: mtl.iBgrColor=newColor
        #mtl_Global.info("abc")

    def getNumberItem(self):
        return len(self.items())

    def getNumberSelectedItem(self):
        return len(self.selectedItems())

#endregion */