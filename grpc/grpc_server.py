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

class RgbImageServicer(rgb_image_pb2_grpc.Predict_labelServicer):
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
        rgb_image_pb2_grpc.add_Predict_labelServicer_to_server(self, self.server)

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
        Input RGB image
        """
        print("Received image:")
        print(request)

        # decode the image and display it
        image = np.frombuffer(zlib.decompress(base64.b64decode(request.image)), dtype=np.uint8).reshape(request.height, request.width, 3)
        # display the image
        cv2.imshow("Image", image)
        cv2.waitKey(0)

        # create a valid response
        response = rgb_image_pb2.Predicted_label()
        response.label = "false"
        response.name = "image1"

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
    
