"""
This program aims to upload the mobilenet model and use it to predict the class of an image.
"""

import os
import sys
import argparse
import numpy as np
import tensorflow as tf
import cv2


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
        self.prediction = model.predict(image)

    def get_image(self, image):
        """
        :param image_path:
        :return:
        """
        image = cv2.resize(image, (224, 224))
        image = np.array(image)
        image = image.astype('float32')
        image /= 255
        image = np.expand_dims(image, axis=0)
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


def main():
    # Get current working directory
    cwd = os.getcwd()
    # Instantiate the Predict class.
    predict = Predict(model_path=cwd+"/../models/mobilenet.hdf5")
    # Load the image.
    image = cv2.imread(cwd+"/../data/x_test/AE00008_080949_00_2_2_2001.jpg")
    # Get the image.
    image = predict.get_image(image)

    # Predict the class of the image.
    predict.predict(model=predict.model, image=image)
    # Get the class of the image.
    class_ = predict.get_class()
    # Get the confidence of the image.
    confidence = predict.get_confidence()

    # Print the class and confidence.
    print("Class: {}".format(class_))
    print("Confidence: {}".format(confidence))

if __name__ == "__main__":
    main()


