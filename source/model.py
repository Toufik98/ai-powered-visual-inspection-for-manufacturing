"""
This program aims to implement CNN model using keras and tensorflow to classify images of power boards to two classes:
1. Defectuous power board
2. Normal power board
"""

# Import libraries
from __future__ import print_function

import tensorflow as tf
import cv2
import numpy as np
from tensorflow.keras.layers import Input, Dense, Dropout, Activation, Concatenate, BatchNormalization, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Conv2D, GlobalAveragePooling2D, AveragePooling2D, ZeroPadding2D, MaxPooling2D
from tensorflow.keras.regularizers import l2

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.callbacks import LearningRateScheduler
import matplotlib.pyplot as plt
import argparse
import pandas as pd
import os

# Define the CNN model
def CNN_model(input_shape, num_classes):
    """
    This function defines the CNN model
    """
    # Define the input layer
    input_layer = Input(shape=input_shape)
    # Define the first convolutional layer
    x = Conv2D(filters=32, kernel_size=(3,3), padding='same', activation='relu', kernel_regularizer=l2(0.01))(input_layer)
    x = BatchNormalization()(x)
    x = MaxPooling2D(pool_size=(2,2))(x)
    x = Dropout(0.25)(x)
    # Define the second convolutional layer
    x = Conv2D(filters=64, kernel_size=(3,3), padding='same', activation='relu', kernel_regularizer=l2(0.01))(x)
    x = BatchNormalization()(x)
    x = MaxPooling2D(pool_size=(2,2))(x)
    x = Dropout(0.25)(x)
    # Define the third convolutional layer
    x = Conv2D(filters=128, kernel_size=(3,3), padding='same', activation='relu', kernel_regularizer=l2(0.01))(x)
    x = BatchNormalization()(x)
    x = MaxPooling2D(pool_size=(2,2))(x)
    x = Dropout(0.25)(x)
    # Define the fourth convolutional layer
    x = Conv2D(filters=256, kernel_size=(3,3), padding='same', activation='relu', kernel_regularizer=l2(0.01))(x)
    x = BatchNormalization()(x)
    x = MaxPooling2D(pool_size=(2,2))(x)
    x = Dropout(0.25)(x)
    # Define the fifth convolutional layer
    x = Conv2D(filters=512, kernel_size=(3,3), padding='same', activation='relu', kernel_regularizer=l2(0.01))(x)
    x = BatchNormalization()(x)
    x = MaxPooling2D(pool_size=(2,2))(x)
    x = Dropout(0.25)(x)
    # Define the sixth convolutional layer
    x = Conv2D(filters=1024, kernel_size=(3,3), padding='same', activation='relu', kernel_regularizer=l2(0.01))(x)
    x = BatchNormalization()(x)
    x = MaxPooling2D(pool_size=(2,2))(x)
    x = Dropout(0.25)(x)
    # Define the flatten layer
    x = Flatten()(x)
    # Define the fully connected layer
    x = Dense(units=1024, activation='relu', kernel_regularizer=l2(0.01))(x)
    x = BatchNormalization()(x)
    x = Dropout(0.5)(x)
    # Define the output layer
    output_layer = Dense(units=num_classes, activation='softmax')(x)
    # Define the model
    model = Model(inputs=input_layer, outputs=output_layer)
    # Compile the model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # Return the model
    return model


# Define the function to train the model
def train_model(model, train_generator, validation_generator, num_classes, epochs, batch_size):
    """
    This function trains the model
    """
    # Train the model
    model.fit_generator(train_generator, steps_per_epoch=train_generator.samples//batch_size, epochs=epochs, validation_data=validation_generator, validation_steps=validation_generator.samples//batch_size)
    # Save the model
    model.save('model.h5')
    # Return the model
    return model

# Define the function to test the model
def test_model(model, test_generator, num_classes, batch_size):
    """
    This function tests the model
    """
    # Test the model
    test_loss, test_acc = model.evaluate_generator(test_generator, steps=test_generator.samples//batch_size)
    # Print the test loss and test accuracy
    print('Test loss:', test_loss)
    print('Test accuracy:', test_acc)
    # Return the test loss and test accuracy
    return test_loss, test_acc

# Define the function to predict the labels
def predict_labels(model, test_generator, num_classes, batch_size):
    """
    This function predicts the labels
    """
    # Predict the labels
    predicted_labels = model.predict_generator(test_generator, steps=test_generator.samples//batch_size)
    # Return the predicted labels
    return predicted_labels



# Define the function to plot the training history
def plot_training_history(history):
    """
    This function plots the training history
    """
    # Plot the training and validation loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    # Set the legend
    plt.legend(['Train', 'Validation'], loc='upper right')
    # Show the figure
    plt.show()
    # Plot the training and validation accuracy
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    # Set the legend
    plt.legend(['Train', 'Validation'], loc='lower right')
    # Show the figure
    plt.show()
    # Return the figure
    return plt

def get_data(data_dir, batch_size):
    """
    This function loads the data
    """
    # Get current working directory
    cwd = os.getcwd()
    # Read dataframes
    test_df = pd.read_csv(cwd+data_dir+'\\'+'Y_Benchmarks.csv')

    # Train datagen
    train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
    # Load the training, validation, and testing data
    train_generator = train_datagen.flow_from_directory(data_dir + '/x_train', target_size=(1000, 1000), batch_size=batch_size, class_mode='binary', subset='training')
    validation_generator = train_datagen.flow_from_directory(data_dir + '/x_train',
                                                                                    target_size=(1000, 1000),
                                                                                    batch_size=batch_size,
                                                                                    class_mode='binary',
                                                                                    subset='validation')

    test_generator = ImageDataGenerator(rescale=1./255).flow_from_dataframe(dataframe=test_df, directory=data_dir + '/x_test', x_col='images', y_col='Labels', target_size=(1000, 1000), batch_size=batch_size, class_mode='binary')

    return train_generator, validation_generator, test_generator


def main():
    #parse the command line arguments
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--data_dir', type=str,default="..\\data",help='path to the data directory')
    argparser.add_argument('--batch_size', type=int, default= 64,help='batch size')
    argparser.add_argument('--epochs', type=int,default=50, help='number of epochs')
    argparser.add_argument('--learning_rate', type=float, help='learning rate')
    argparser.add_argument('--dropout', type=float, help='dropout rate')

    args = argparser.parse_args()
    #get the data
    train_generator, validation_generator, test_generator = get_data(args.data_dir, args.batch_size)

    input_shape = (train_generator.image_shape[1], train_generator.image_shape[2], train_generator.image_shape[3])
    num_classes = train_generator.num_classes
    model = CNN_model(input_shape, num_classes)
    model.summary()
    # Train the model
    trained_model = train_model(model, train_generator, validation_generator, num_classes, args.epochs, args.batch_size)
    # Test the model
    test_loss, test_acc = test_model(trained_model, test_generator, num_classes, args.batch_size)

    #print the test loss and test accuracy
    print('Test loss:', test_loss)
    print('Test accuracy:', test_acc)

if __name__ == '__main__':
    main()

