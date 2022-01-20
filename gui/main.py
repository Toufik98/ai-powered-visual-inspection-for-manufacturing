"""
This program serves as the main entry point for the GUI.
It uses Pyside2 engine from QML.
"""

# Imports
import sys
import PySide2
from PySide2.QtCore import QUrl
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQuick import QQuickView




# Main
if __name__ == '__main__':
    # Create the application
    app = QGuiApplication(sys.argv)
    # Create the engine
    engine = QQmlApplicationEngine()
    # Create the view
    view = QQuickView()
    # Load the QML file
    view.setSource(QUrl('main.qml'))
    # Show the view
    view.show()
    # Execute the application
    sys.exit(app.exec_())

    
  


