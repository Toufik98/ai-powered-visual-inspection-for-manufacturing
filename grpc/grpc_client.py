"""
This program is used to implement a gRPC client that sends rgb images to the server.
"""

# import the grpc package
import grpc
# import the protobufs package
from rgb_image_pb2 import RGB_image

# import needed modules
import numpy as np
import cv2
import time
import os
import sys
import glob

# Define the client class
class Client():
    def __init__(self):
        # Create a channel to the server
        self.channel = grpc.insecure_channel('localhost:50051')
        # Create a stub (client)
        self.stub = grpc.rpc_channel_ready_future(self.channel)
        # Create a list to store the rgb images
        self.rgb_images = []
        # Create a list to store the rgb images
        self.rgb_images_count = 0
    
    def send_rgb_image(self, rgb_image):
        # Create a rgb image object
        rgb_image_object = RGB_image()
        # Assign the rgb image object the rgb image
        rgb_image_object.images.append(rgb_image)
        # Send the rgb image object to the server
        self.stub.result().send(rgb_image_object)
    
    def receive_rgb_images(self):
        # Create a rgb image object
        rgb_image_object = RGB_image()
        # Receive the rgb image object from the server
        rgb_image_object = self.stub.result().recv_message()
        # Assign the rgb image object to the rgb images list
        self.rgb_images = rgb_image_object.images
        # Assign the rgb images count to the rgb images count
        self.rgb_images_count = len(self.rgb_images)
    
    def close_channel(self):
        # Close the channel
        self.channel.close()

    def get_rgb_images(self):
        return self.rgb_images
    
    def get_rgb_images_count(self):
        return self.rgb_images_count


    