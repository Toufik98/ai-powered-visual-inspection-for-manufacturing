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
    def Predict(self, request, context):
        """
        Input RGB image
        """
        print("Received image:")
        print(request)

        # decode the image and display it
        image = np.frombuffer(zlib.decompress(base64.b64decode(request.image)), dtype=np.uint8).reshape((100, 100, 3))

        # display the image
        cv2.imshow("Image", image)
        cv2.waitKey(0)

        # create a valid response
        response = rgb_image_pb2.Predicted_label()
        response.label = "false"
        response.name = "image1"

        return response




# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# add the calculator service to the server
rgb_image_pb2_grpc.add_Predict_labelServicer_to_server(RgbImageServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')

# start the server
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        print('.')
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

