# AI Powered visual inspection for manufacturing
This repository contains all needed materials to our project of building a visual inspection system for manufacturing.

## Directory structure
This project is divided into several subdirectories :
* `database` : contains all the database files and the database management system
* `grpc` : contains all the gRPC files and the gRPC server and client which are used to make the application available to the outside world
* `models` : contains all the pre-trained models which will be used to make the visual inspection and prediction
* `preprocessing` : contains all the files which are used to preprocess the data, implement the machine learning algorithms models and train the models
* `source` : contains the principal files of the project, predict.py that will be used to load the models and make the prediction, main.py that will the main file of the project

## Installation
To be able to use the project, you need to do the following :
* Install the Python 3.8.x or higher version
* Install the needed packages with `pip install -r requirements.txt`
* Install qt5-default with `sudo apt-get install qt5-default`
## Usage
Execute the main file of the project with `python3 main.py`


