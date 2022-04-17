import maya.cmds as cmds
import maya.OpenMayaUI as mui
import os,sys
from PySide2 import QtCore,QtGui,QtWidgets
from shiboken2 import wrapInstance
sys.path.append("C:/Users/%s/Documents/GitHub/pickerLeeMTV/python"%os.environ["USER"])
import imp

if "mtl_gTab" in sys.modules:
    imp.reload(sys.modules['mtl_gTab'])
    print("modules : mtl_gTab reloaded.")
if "Ui_MayaController" in sys.modules:
    imp.reload(sys.modules['Ui_MayaController'])
    print("modules : Ui_MayaController reloaded.")
if "mtl_gItem" in sys.modules:
    imp.reload(sys.modules['mtl_gItem'])
    print("modules : mtl_gItem reloaded.")
if "mtl_gGlobal" in sys.modules:
    imp.reload(sys.modules['mtl_gGlobal'])
    print("modules : mtl_gGlobal reloaded.")

from mtl_gGlobal import *
from mtl_gItem import mtl_GraphicsItem
from mtl_gTab import MTL_View
# from mtl_gScene import MTL_Scene
# from mtl_gView import MTL_View
MTL=mtlGlobal()

class Ui_info(object):
    ws="WS_METALEEPICKER_EDITOR"
    wstitle="METALEE's PICKER"
    user=os.environ["USER"]
    filepath="C:/Users/%s/Documents/GitHub/pickerLeeMTV/src/METALEEPICKER.ui"%user
    def __init__(self):
        pass

class Ui_MayaController(Ui_info):
    def __init__(self):
        super(Ui_MayaController,self).__init__()
        inf=Ui_info
        
        #print(inf.filepath)
        if self.__PluginsIsLoaded():
            self.uiCreatePICKER(inf.ws,inf.wstitle,self.Ui_PathFile())
        else : 
            cmds.loadPlugin("C:/Users/%s/Documents/GitHub/pickerLeeMTV/plug-ins/METALEEPICKER"%self.user)
            self.uiCreatePICKER(inf.ws,inf.wstitle,self.Ui_PathFile())
            return cmds.error("# METALEE : METALEEPICKER Plugin is'nt loaeded #")
        
    #convert maya to Object
    # def mWindowToQObject(self,MayaControl=str,QType=QtCore.QObject):
    #     if not MayaControl: return cmds.error("no control name")
    #     control_widget = mui.MQtUtil.findControl(MayaControl)
    #     control_wrap = wrapInstance(int(control_widget), QType)
    #     return control_wrap

    #create maya workspaceControl window
    def workspaceCreate(self,wSpaceName=str,windowtitle=str):
        if cmds.workspaceControl(wSpaceName,ex=True):
            cmds.deleteUI(wSpaceName)
        main_control = cmds.workspaceControl(wSpaceName,fl=False,label=windowtitle)
        control_widget = mui.MQtUtil.findControl(main_control)
        control_wrap = wrapInstance(int(control_widget), QtWidgets.QWidget)
        if control_wrap:
            return control_wrap

    #add qt to maya window 
    def addQWindowToMayaWindow(self,addWindow=QtWidgets.QWidget,ToWindow=QtWidgets.QWidget):
        if not addWindow : return cmds.error("# METALEE : addWindow not found %s #"%addWindow)
        if not ToWindow : return cmds.error("# METALEE : ToWindow not found %s #"%ToWindow)
        addWindow.setParent(ToWindow)
        ToWindow.layout().addWidget(addWindow)

    #add widget to toolbar
    def CreateWidgetAddToolbar(self,toolBarName=str,customWidget=QtWidgets.QWidgetAction):
        if not toolBarName: cmds.error("# METALEE : toolbar name can't not be empty %s #"%toolBarName)
        if not customWidget: cmds.error("# METALEE : custom widget is not found %s #"%customWidget)
        _toolbar=self.toQtWidget(toolBarName,QtWidgets.QToolBar)
        if not _toolbar: return cmds.error("# METALEE : toolbar's not found %s #"%toolBarName)
        _toolbar.addAction(customWidget)

    #get ui maya control return Qwidget
    def __getMayaControl(self,objectName=str):
        if not objectName: return cmds.error("# METALEE : ' %s ' is not found #"%objectName)
        control=mui.MQtUtil_findControl(objectName)
        if control: return control
        else : return cmds.error("# METALEE : control %s not found #"%objectName)

    #open qt designer return qwidget
    def __MayaOpenUiFile(self,filepath=str):
        if not filepath: return cmds.error("# METALEE : file's not found %s #"%filepath)
        if not os.path.isfile(filepath): cmds.error("# METALEE : file %s does not exits #"%filepath)
        if not filepath.endswith(".ui"): return cmds.error("# METALEE : does not ui file # ")
        filepath.replace("\\","/")
        windowName=cmds.loadUI(uiFile=filepath)
        cmds.showWindow(windowName)
        return MTL.mWindowToQObject(windowName,QtWidgets.QWidget)

    #create Ws PICKER
    def uiCreatePICKER(self,wsName=str,wsTitle=str,uifilePath=str):
        if not wsName or not wsTitle or not uifilePath: return cmds.error("# METALEE : error input string #")
        qWdow=self.__MayaOpenUiFile(uifilePath)
        mWidget=self.workspaceCreate(wsName,wsTitle)
        self.addQWindowToMayaWindow(qWdow,mWidget)

    def Ui_PathFile(self):
        if cmds.pluginInfo("METALEEPICKER",q=True,l=True):
            path=cmds.pluginInfo("METALEEPICKER",q=True,p=True)
            path=str(path).replace("plug-ins/METALEEPICKER.mll","src/METALEEPICKER.ui")
            #print(path)

            return path
        else: 
            print(path)
            return cmds.error("# METALEE : plug-ins METALEEPICKER isn't loaded. #")

    def __PluginsIsLoaded(self):
        return cmds.pluginInfo("METALEEPICKER",q=True,l=True)



mCTRL=Ui_MayaController()
mCTRL.Ui_PathFile()
mTab=MTL.mWindowToQObject("mainTab",QtWidgets.QWidget)
gView=MTL_View(mTab,"abc")
hLayout=mTab.findChild(QtWidgets.QHBoxLayout,"leeGraphics")
hLayout.addWidget(gView)

MTL.info("bbb")

# aScene=QtWidgets.QGraphicsScene()
# aut=QtGui.QImage("C:/Users/LeePhan/Documents/GitHub/pickerLeeMTV/icon/author1")
# aScene.setBackgroundBrush(aut)
# gView.setScene(aScene)
# print("# METALEE : %s #"%gView.objectName())

#mController.uiCreatePICKER("WS_METALEEPICKER_EDITOR","METALEE's PICKER","C:/Users/LeePhan/Documents/GitHub/PhanLee-Picker/src/METALEEPICKER.ui")
# bar=toQtWidget("mainToolBar",QtWidgets.QToolBar)
# abc=QtWidgets.QWidgetAction(bar)
# wid=QtWidgets.QWidget()
# act=QtWidgets.QSpinBox(wid)
# abc.setDefaultWidget(act)
# bar.addAction(abc)

# qtWindow=getMayaWindowtoQWidget(METALEE)
# mainWidget=workspaceCreate("taoday","METALEE's PICKER")
# print(qtWindow.objectName(),mainWidget.objectName())
# #mui.MQtUtil_addWidgetToMayaLayout(qtWindow,mainWidget.objectName()[0])
# #QtWidgets.QWidget(qtWindow).setParent(mainWidget)
# #mainWidget.layout().addWidget(qtWindow)
# addQWindowToMayaWindow(qtWindow,mainWidget)