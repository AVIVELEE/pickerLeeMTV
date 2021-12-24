#include <QtWidgets/QApplication>
#include <maya/MFnPlugin.h>
#include <maya/MGlobal.h>


MStatus initializePlugin(MObject obj) {
	MFnPlugin plugin(obj, "Autodesk", "1.0", "Any");
	MString Cmdinfo= "print(\"initialize METALEE'S PICKER in " + MString(QApplication::applicationDisplayName().toStdString().c_str())  + "\\n\")";
	MGlobal::executeCommandOnIdle(Cmdinfo);
	return MS::kSuccess;
}

MStatus uninitializePlugin(MObject obj) {

	MGlobal::displayInfo("deregister.");
	return MS::kSuccess;
}

