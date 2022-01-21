"""
This program aims to upload the mobilenet model and use it to predict the class of an image.
"""

import os
import sys
import argparse
import numpy as np
import tensorflow as tf
from PIL import Image


class Predict:
    """
    This class is used to predict the class of an image.
    """

    def __init__(self, model_path):
        """
        Initialize the Predict class.

        :param model_path: The path to the model.
        :param image_path: The path to the image.
        """
        self.model_path = model_path
        self.prediction = None
        self.model = self.load_model()

    def load_model(self):
        """
        Load the model.

        :return: The model.
        """
        model = tf.keras.models.load_model(self.model_path)
        return model

    def predict(self, model, image):
        """
        Predict the class of an image.

        :param model: The model.
        :param image: The image.
        :return: The class of the image.
        """
        image = image.resize((224, 224))
        image = np.array(image)
        image = image / 255.0
        image = image.reshape(1, 224, 224, 3)
        self.prediction = model.predict(image)

    def get_image(self, image_path):
        """
        :param image_path:
        :return:
        """
        image = Image.open(image_path)
        return image

    def image_size(self, image):
        """
        Get the size of the image.

        :param image: The image.
        :return: The size of the image.
        """
        width, height, depth = image.size

        return width, height, depth

    def get_class(self):
        """
        :param index:
        :return:
        """
        classes = {
            0: "Not Defected",
            1: "Defected"
        }
        return classes[np.argmax(self.prediction)]

    def get_confidence(self):
        """
        :param index:
        :return:
        """
        return self.prediction[0][np.argmax(self.prediction)]
