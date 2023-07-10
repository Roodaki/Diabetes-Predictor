<div align="center">
  <h1><strong>Diabet Predictor</strong></h1>
  <p><strong>The Diabetes Predictor Desktop Application is a user-friendly tool that utilizes a logistic regression model to predict the probability of a user having diabetes based on their inputted information. The application features a custom implementation of the logistic regression algorithm, an intuitive graphical user interface (GUI), and the ability to train the model on custom datasets. It aims to aid in early detection and proactive healthcare interventions for diabetes management.</strong></p>
</div>

![Screenshot (140)](https://github.com/Roodaki/Diabet-Predictor/assets/89901590/3c0eaefc-64cf-4f00-81ad-3317bcdfa14f)

## Table of Contents
- [Intruduction](#intruduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Usage Guide](#usage-guide)

## Intruduction
Diabetes is a prevalent and chronic disease that affects millions of people worldwide. Early detection and accurate prediction of diabetes can significantly improve patient outcomes and guide proactive healthcare interventions. In this project, we have developed a desktop application that utilizes a logistic regression model to predict whether a person has diabetes based on their inputted information.

The application employs a logistic regression algorithm, implemented from scratch, to analyze various patient attributes such as age, body mass index (BMI), blood pressure, and glucose levels. By training the model on a dataset containing these attributes along with corresponding labels (0 for no diabetes, 1 for diabetes), it learns to distinguish between diabetic and non-diabetic individuals. The trained model is then used to predict the probability of a user having diabetes based on their input.

## Features
- Full Implementation of Logistic Regression: The logistic regression algorithm is implemented from scratch, allowing for a comprehensive understanding of the underlying principles and complete control over the training process. This implementation ensures that the application is not reliant on external libraries for logistic regression.
- Customizable Model Training: Users can train the logistic regression model on their own dataset. By providing a properly formatted CSV file with the necessary attributes and labels, users can tailor the model to their specific requirements and datasets.
- Diabetes Prediction: Based on the inputted information, the application predicts whether the user has diabetes or not. The application provides accurate predictions and enables early detection by leveraging the logistic regression model.
- User-friendly Interface: The application provides a graphical user interface (GUI) that allows users to input their information easily. The interface is intuitive, making it simple for users to provide their details for prediction.

## Project Structure
The project follows a specific structure to organize its files and directories:
```
diabetes-prediction-app/
├── main.py
├── model.py
├── IO.py
├── samples.csv
├── README.md
└── .gitignore
```
- `main.py`: Main script file that runs the diabetes prediction application.
- `model.py`: File containing the implementation of the logistic regression model.
- `IO.py`: File containing the input/output operations and GUI code for the application.
- `samples.csv`: CSV file containing sample data for training and testing the model.
- `README.md`: Documentation file providing information about the project.
- `.gitignore`: File that specifies which files and directories should be ignored by Git version control.

## Requirements
To run the Diabetes Prediction Desktop Application, you need to have the following installed on your system:
* Python (version 3.0 or higher)
* Python libraries:
  * scikit-learn
  * PyQt
* Git command line tool (or Git GUI client) to clone the repository.

## Usage Guide
1. Open a terminal and clone this repository: `git clone https://github.com/Roodaki/Diabet-Predictor.git`
2. Prepare the Dataset: The application requires a properly formatted CSV file dataset with the necessary attributes and labels (0 for no diabetes, 1 for diabetes). Ensure that the dataset is ready for training and testing the logistic regression model.
4. Run the Application: Run the application's `main.py` script to train the logistic regression model on the provided dataset and launch the graphical user interface (GUI) where users can input their information and receive diabetes predictions based on the trained model.
5. Interact with the Application: Input the patient's information, such as age, BMI, blood pressure, and glucose levels, through the GUI. After entering the information, click on the "Predict" button to obtain the diabetes prediction result. The application will display the prediction outcome on the GUI.
