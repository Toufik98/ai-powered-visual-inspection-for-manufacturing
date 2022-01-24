"""
This program aims to implement Q methods to send signals to QML files and receive slots from it.
It will also use grpc client to send data to server
"""

# Importing libraries
import sys
import os
import time
import threading
import queue
import logging
import logging.config
import signal
import json
import grpc
import numpy as np
import cv2
import argparse

# Change directory to the directory of this file
cwd = os.getcwd()
sys.path.append(cwd + '/../grpc/')
import rgb_image_pb2
import rgb_image_pb2_grpc

import PySide2 as Qt
from PySide2.QtCore import QObject, Signal, Slot, QTimer, QThread, QMutex, QMutexLocker
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine



# Define a class to connect to QML
class QmlConnector(QObject):
    """
    This class is used to connect to QML and send signals to it.
    """
    def __init__(self, parent=None):
        super(QmlConnector, self).__init__(parent)

        # Create a channel to connect to server
        #self.channel = grpc.insecure_channel('localhost:50051')

        # Create a stub to send data to server
        #self.stub = rgb_image_pb2_grpc.RgbImageStub(self.channel)

        # Create a slot to receive data from qml
        self.qml_slot = Signal(str)




    @Slot(str)
    def load_image(self, path):
        """
        :param data:
        :return:
        """
        # Clean up the path 
        path = path.replace('file://', '')
        # Read image from path
        image = cv2.imread(path)
        if image is None:
            print("Image not found")
            return
        #Get the image name
        image_name = path.split('/')[-1]

        # Display image
        print("Image name: ", image_name)
        print("Image shape: ", image.shape)
        print("Image type: ", image.dtype)

        # Display image
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def main():
    """
    Main function
    """
    # Create a QApplication
    app = QGuiApplication(sys.argv)

    # Create a QQmlApplicationEngine
    engine = QQmlApplicationEngine()

    # Create a QmlConnector
    qml_connector = QmlConnector()

    # Connect to QML
    engine.rootContext().setContextProperty("QmlConnector", qml_connector)

    # Load QML file
    engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

    # Execute the QApplication
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())	

if __name__ == '__main__':
    main()