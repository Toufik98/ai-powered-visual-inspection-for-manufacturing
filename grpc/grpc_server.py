"""
This program is a gRPC server that receives rgb images from the client
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

# Define the server class
class Server():
    def __init__(self):
        # Create a channel to the server
        self.channel = grpc.insecure_channel('localhost:50051')
        # Create a stub (server)
        self.stub = grpc.rpc_channel_ready_future(self.channel)
        # Create a list to store the rgb images
        self.rgb_images = []
        # Create a list to store the rgb images
        self.rgb_images_count = 0
        
    def receive_rgb_images(self):
        # Create a rgb image object
        rgb_image_object = RGB_image()
        # Receive the rgb image object from the server
        rgb_image_object = self.stub.result().recv_message()
        # Assign the rgb image object to the rgb images list
        self.rgb_images = rgb_image_object.images
        # Assign the rgb images count to the rgb images count
        self.rgb_images_count = len(self.rgb_images)
        
    def get_rgb_images(self):
        return self.rgb_images
        
    def get_rgb_images_count(self):
        return self.rgb_images_count
        
    def close_channel(self):
        # Close the channel
        self.channel.close()

def main():
    # Run the server
    server = Server()

    # Create a loop to receive rgb images
    while True:
        # Receive the rgb images
        server.receive_rgb_images()
        # Get the rgb images
        rgb_images = server.get_rgb_images()
        # Get the rgb images count
        rgb_images_count = server.get_rgb_images_count()
        # Print the rgb images count
        print('rgb_images_count:', rgb_images_count)
        # Print the rgb images
        print('rgb_images:', rgb_images)
        # Close the channel
        server.close_channel()
        # Wait for 1 second
        time.sleep(1)
