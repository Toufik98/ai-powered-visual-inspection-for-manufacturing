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
        response = self.stub.Predict(request)

        # decode the response
        label = response.label
        name = response.name

        print("The label is: " + label)
        print("The name is: " + name)
    
    def stop(self):
        """
        Stop the client
        """
        self.stub.stop()
        print("Client stopped...")
    


def main():
    # create a client
    client = RgbImageClient("localhost", "50051")

    # create an image
    image = cv2.imread("../data/AE00008_143414_00_1_1_2001.jpg")

    # Get the image height and width
    h, w, _ = image.shape
    print("Image height:", h)
    print("Image width:", w)
    name = "image1"
    client.send_image(image, name, h, w)

    # stop the client
    client.stop()

if __name__ == "__main__":
    main()

    
    
