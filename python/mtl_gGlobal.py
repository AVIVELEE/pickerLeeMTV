from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
if "Maya" in QApplication.applicationName():
    import maya.cmds as cmds
    import maya.OpenMayaUI as mui
from shiboken2 import wrapInstance
from mtl_gItem import mtl_GraphicsItem

class mtlGlobal:
    def __init__(self):
        pass
    def mWindowToQObject(self,MayaControl=str,QType=QObject):
        if not MayaControl: return cmds.error("no control name")
        control_widget = mui.MQtUtil.findControl(MayaControl)
        control_wrap = wrapInstance(int(control_widget), QType)
        return control_wrap

    def ColorDialog(self):
        colorDialog=QColorDialog()
        colorDialog.setOption(QColorDialog.ShowAlphaChannel,False)
        colorDialog.exec_()
        selColor=colorDialog.selectedColor()
        return selColor

    def findActionFromToolBar(self,actName=str,ToolBar=QToolBar):
        #aColor=self.mWindowToQObject("mainToolBar",QToolBar)
        for i,o in enumerate(ToolBar.actions()):
            if actName in o.objectName():
                return o
    def info(self,message):
        print("#META LEE : %s"%message)
        print("#META LEE : updated")

    def createItem(self,mScene=QGraphicsScene):
        item=mtl_GraphicsItem()
        if mScene: 
            mScene.addItem(item)
            item.iPng="C:/Users/LeePhan/Downloads/ceo.png"