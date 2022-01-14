"""
This program is used to implement a gRPC client that sends rgb images to the server.
"""

import grpc 

# import the generated classes
import rgb_image_pb2
import rgb_image_pb2_grpc

# Import libraries for data encoding and decoding
import base64
import io
import zlib
import numpy as np
import cv2
import argparse
from tkinter import *
from tkinter import filedialog

import os
import sys



# Define the client class
class RgbImageClient(object):
    """
    This class is used to implement a gRPC client that sends rgb images to the server.
    """
    def __init__(self, ip_address, port):
        """
        Initialize the client class
        """
        # create a channel to the server
        channel = grpc.insecure_channel(ip_address + ":" + port)

        # create a stub (client)
        self.stub = rgb_image_pb2_grpc.Predict_labelStub(channel)

        # Create a root window
        self.root = None

        self.image = None
        self.nm = None
        self.h = None
        self.w = None

        self.label = ""
        self.name = ""

    def send_image(self, image, nm, h, w):
        """
        Send an image to the server
        """
        # encode the image
        image_bytes = image.tobytes()
        image_bytes_compressed = zlib.compress(image_bytes)
        image_bytes_encoded = base64.b64encode(image_bytes_compressed)

        # create a request object
        request = rgb_image_pb2.RGB_image(image = image_bytes_encoded, name = nm, height =h , width = w) 

        # make the call
        print("Sending image to server...") 
        response = self.stub.Predict(request)
        print("Image sent to server...")
        # decode the response
        self.label = response.label
        self.name = response.name

        print("Received label: " + self.label)
        print("Received name: " + self.name)
    
    def select_image(self):
        """
        Select an image from the client
        """
        # Open file dialog
        self.root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

        # Read the image
        self.image = cv2.imread(self.root.filename)

        # Get the image name
        self.nm = self.root.filename.split("/")[-1]

        # Get the image height and width
        self.h = self.image.shape[0]
        self.w = self.image.shape[1]


def main():
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type = str, default="localhost", help="The ip of the gRPC server")
                
    parser.add_argument("--port", type=str, default=50051,
                        help="The port of the gRPC server. Default to 50051")
    args = parser.parse_args()

    ip_address = str(args.ip)
    port = str(args.port)
    # Create a client
    client = RgbImageClient(ip_address, port)

   

    """
    Using Pyqt5 to create a GUI
    Create a root window, place a button to select the image and place with logo to verify the well-working of the upload
    Place anothe button to send the image to the server and place with logo to verify the well-working of sending the image
    Place a label  to receive the response from the server and place with logo to verify the well-working of receiving the response
    Place a label to show the image to send to the server
    Place a status bar to show the sennding image

    Place a button with a power button to close the program
    """
    # Create a root window
    client.root = Tk()
    client.root.title("Rgb Image Client")

    # Create a label to show the response from the server
    response_label = Label(client.root, text = "Response from the server: ")
    response_label.grid(row = 1, column = 0)

    # Create a label to show the sending image
    sending_label = Label(client.root, text = "Sending image: ")
    sending_label.grid(row = 2, column = 0)

    # Create a label to show the status of the sending image
    status_label = Label(client.root, text = "Label of the image: " + client.label)
    status_label.grid(row = 3, column = 0)

    # Create a button to select the image
    select_button = Button(client.root, text = "Select image", command = client.select_image)
    select_button.grid(row = 1, column = 1)

    # Create a button to send the image to the server
    send_button = Button(client.root, text = "Send image", command = lambda: client.send_image(client.image, client.nm, client.h, client.w))
    send_button.grid(row = 2, column = 1)

    # Create a button to close the program
    close_button = Button(client.root, text = "Close", command = client.root.destroy)
    close_button.grid(row = 4, column = 1)

    # Start the main loop
    client.root.mainloop()



if __name__ == "__main__":
    main()

    
    
