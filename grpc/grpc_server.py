"""
This program is a gRPC server that receives rgb images from the client.
"""

# import the grpc package
import grpc
from concurrent import futures

# import the generated classes
import rgb_image_pb2_grpc 
import rgb_image_pb2
import time

import zlib 
import base64
import numpy as np
import cv2

class RgbImageServicer(rgb_image_pb2_grpc.Predict_serviceServicer):
    """
    This class is used to implement a gRPC server that receives rgb images from the client.
    """

    def __init__(self):
        """
        Initialize the server class
        """
        self.server = None
    
    def start(self, ip_address, port):
        """
        Start the server
        """
        # create a server
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        # add the service to the server
        rgb_image_pb2_grpc.add_Predict_serviceServicer_to_server(self, self.server)

        # start the server
        self.server.add_insecure_port(ip_address + ":" + port)

        # start the server
        self.server.start()
        print("Server started...")
    def stop(self):
        """
        Stop the server
        """
        self.server.stop(0)
        print("Server stopped...")
    
    def loop(self):
        """
        Loop the server
        """
        try:
            while True:
                time.sleep(60 * 60 * 24)
        except KeyboardInterrupt:
            self.stop()
    
    def Predict(self, request, context):
        """
        Method where will be doing our processing and storing the result in Database

        TODO: Add your processing here
        TODO: Add your storing here

        """
        print("Received image:")
        print("Name: " + request.name)
        print("Height: " + str(request.height))
        print("Width: " + str(request.width))

        # decode the image and display it
        image = np.frombuffer(zlib.decompress(base64.b64decode(request.image)), dtype=np.uint8).reshape(request.height, request.width, 3)

        # TODO: Delete display of the image 
        # display the image
        #cv2.imshow("Image", image)
        #cv2.waitKey(0)

        # create a valid response
        response = rgb_image_pb2.Predicted()
        response.label = "false"
        response.confidence = 0.0
        response.x = 0
        response.y = 0
        response.height_image = 0
        response.width_image = 0
        response.depth_image = 0
        response.width = 0
        response.height = 0
        response.confidence = 0.0

        # Send the response

        return response

def main():
    # create a server
    server = RgbImageServicer()

    # start the server
    server.start("localhost", "50051")

    # loop the server
    server.loop()

if __name__ == "__main__":
    main()
    
