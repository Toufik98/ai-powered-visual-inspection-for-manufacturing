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
import zlib
import base64

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
    label = Signal(str, arguments=['Label'])
    def __init__(self,ip_address, port):
        super(QmlConnector, self).__init__()

        # Create a channel to the server
        channel = grpc.insecure_channel(ip_address + ":" + port)

        # Create a stub (client)
        self.stub = rgb_image_pb2_grpc.Predict_serviceStub(channel)

        # Create a root window
        self.root = None

        # Data to sent to the server
        self.image = None
        self.nm = None
        self.h = None
        self.w = None
        self.depth = None

        # Data to receive from the server
        
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.height_image = 0
        self.width_image = 0
        self.depth_image = 0
        self.confidence = 0

    
        

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

        # Get the image data
        self.h = image.shape[0]
        self.w = image.shape[1]
        self.depth = image.shape[2]

        self.image = image
        self.nm = image_name
    
    @Slot()
    def send_image(self):
        """
        Send an image to the server
        """
        try :
            # encode the image
            if self.image is not None:
                image_bytes = self.image.tobytes()
                image_bytes_compressed = zlib.compress(image_bytes)
                image_bytes_encoded = base64.b64encode(image_bytes_compressed)

                # create a request object
                request = rgb_image_pb2.RGB_image(image = image_bytes_encoded, name = self.nm, height =self.h , width = self.w, depth = self.depth)

                # make the call
                print("Sending image to server...") 
                response = self.stub.Predict(request)
                if response.label != "":
                    # Send the response
                    self.label.emit(response.label)
                    self.x = response.x
                    self.y = response.y
                    self.width = response.width
                    self.height = response.height
                    self.height_image = response.height_image
                    self.width_image = response.width_image
                    self.depth_image = response.depth_image
                    self.confidence = response.confidence
                    print("Received response from server:")
        except Exception as e:
            print("Error: ", e)
        




def main():
    """
    Main function
    """
    # Create a QApplication
    app = QGuiApplication(sys.argv)

    # Create a QQmlApplicationEngine
    engine = QQmlApplicationEngine()

    # Create a QmlConnector
    qml_connector = QmlConnector(ip_address="localhost", port="50051")

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