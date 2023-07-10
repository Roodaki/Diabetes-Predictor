import pandas as pd
from sklearn.model_selection import train_test_split
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QWidget


def read_csv_dataset(filename, target_column, test_size=0.15, random_state=2):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(filename)

    # Separate features and target variable
    X = df.drop(target_column, axis=1)
    y = df[target_column]

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Convert DataFrame to lists
    X_train = X_train.values.tolist()
    X_test = X_test.values.tolist()
    y_train = y_train.tolist()
    y_test = y_test.tolist()

    # Return the training and testing sets as lists
    return X_train, X_test, y_train, y_test



class DiabetesPredictionWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Diabetes Prediction")
        self.setGeometry(100, 100, 300, 300)

        # Create input labels and fields
        self.pregnancies_label = QLabel("Pregnancies:")
        self.pregnancies_input = QLineEdit()

        self.glucose_label = QLabel("Glucose:")
        self.glucose_input = QLineEdit()

        self.blood_pressure_label = QLabel("Blood Pressure:")
        self.blood_pressure_input = QLineEdit()

        self.skin_thickness_label = QLabel("Skin Thickness:")
        self.skin_thickness_input = QLineEdit()

        self.insulin_label = QLabel("Insulin:")
        self.insulin_input = QLineEdit()

        self.bmi_label = QLabel("BMI:")
        self.bmi_input = QLineEdit()

        self.diabetes_pedigree_label = QLabel("Diabetes Pedigree:")
        self.diabetes_pedigree_input = QLineEdit()

        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()

        # Create predict button
        self.predict_button = QPushButton("Predict")
        self.predict_button.clicked.connect(self.predict)

        # Create layout and add input elements
        layout = QVBoxLayout()
        layout.addWidget(self.pregnancies_label)
        layout.addWidget(self.pregnancies_input)
        layout.addWidget(self.glucose_label)
        layout.addWidget(self.glucose_input)
        layout.addWidget(self.blood_pressure_label)
        layout.addWidget(self.blood_pressure_input)
        layout.addWidget(self.skin_thickness_label)
        layout.addWidget(self.skin_thickness_input)
        layout.addWidget(self.insulin_label)
        layout.addWidget(self.insulin_input)
        layout.addWidget(self.bmi_label)
        layout.addWidget(self.bmi_input)
        layout.addWidget(self.diabetes_pedigree_label)
        layout.addWidget(self.diabetes_pedigree_input)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)
        layout.addWidget(self.predict_button)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Apply stylesheet for visual enhancements
        self.setStyleSheet(
            """
            QLabel {
                font-size: 14px;
                color: #333;
            }

            QLineEdit {
                font-size: 14px;
                padding: 6px;
            }

            QPushButton {
                font-size: 16px;
                padding: 10px;
                background-color: #4CAF50;
                color: white;
                border: none;
            }

            QPushButton:hover {
                background-color: #45a049;
            }
            """
        )

    def predict(self):
        # Fetch input values
        pregnancies = float(self.pregnancies_input.text())
        glucose = float(self.glucose_input.text())
        blood_pressure = float(self.blood_pressure_input.text())
        skin_thickness = float(self.skin_thickness_input.text())
        insulin = float(self.insulin_input.text())
        bmi = float(self.bmi_input.text())
        diabetes_pedigree = float(self.diabetes_pedigree_input.text())
        age = float(self.age_input.text())

        # Apply your logistic regression model to predict diabetes here
        # Replace the following line with your model prediction code
        prediction = predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness,
                                      insulin, bmi, diabetes_pedigree, age)

        # Display the prediction result in a new window
        result_window = QMessageBox(self)
        result_window.setWindowTitle("PredictionResult")

        if prediction == 1:
            result_window.setText("Prediction: Person has diabetes")
        else:
            result_window.setText("Prediction: Person does not have diabetes")

        result_window.exec_()


def predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness,
                     insulin, bmi, diabetes_pedigree, age):
    # Implement your logistic regression model here
    # You can use your existing model or train a new one using a dataset
    # Replace the following return statement with your model's prediction
    return 1  # Replace this with your model's prediction

