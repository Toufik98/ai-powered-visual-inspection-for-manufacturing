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
        root = None

        self.image = None
        self.nm = None
        self.h = None
        self.w = None

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
        label = response.label
        name = response.name

        print("The label is: " + label)
        print("The name is: " + name)
    
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

   

    # Create a root window
    client.root = Tk()

    # Create a button to select an image
    b = Button(client.root, text = "Select image", command = lambda: client.select_image())

    # Create a label to display the image
    l = Label(client.root, text = "Image")

    # Create a button to send the image to the server
    b1 = Button(client.root, text = "Send image", command = lambda: client.send_image(client.image, client.nm, client.h, client.w))

   

    # Display the button
    b.pack()


    # Display the button
    b1.pack()


    #  # Display the image
    l.pack()

    # Start the main loop
    client.root.mainloop()








    

  
if __name__ == "__main__":
    main()

    
    
