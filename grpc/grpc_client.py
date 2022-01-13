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


# create a channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = rgb_image_pb2_grpc.Predict_labelStub(channel)

# create a valid rgb image
rgb_image = rgb_image_pb2.RGB_image()

# Reade the image from the file
image = cv2.imread("../data/AE00008_143414_00_1_1_2001.jpg")

# Encode the image
image_bytes = image.tobytes()

# Compress the image
image_bytes_compressed = zlib.compress(image_bytes)

# Encode the image
image_bytes_encoded = base64.b64encode(image_bytes_compressed)

# Set the image
rgb_image.image = image_bytes_encoded

# Send the image to the server
response = stub.Predict(rgb_image)

# decode the response
print("Received response:")
print(response)

