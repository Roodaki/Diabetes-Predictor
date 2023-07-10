from model import LogisticRegression
from IO import *


# Read the training and testing data
X_train, X_test, y_train, y_test = read_csv_dataset('samples.csv', 'Outcome')

logistic_regression = LogisticRegression()

# Train the logistic regression model
logistic_regression.train(X_train, y_train)

# Make predictions on the testing data
accuracy, predictions = logistic_regression.predict(X_test, y_test)

# Print accuracy and predictions
print("Accuracy:", accuracy)
print("Predictions:", predictions)


app = QApplication(sys.argv)

window = DiabetesPredictionWindow()
window_width = window.frameGeometry().width()
window_height = window.frameGeometry().height()
screen = app.primaryScreen().availableGeometry()
x = (screen.width() - window_width) // 2
y = (screen.height() - window_height) // 2
window.setGeometry(x, y, window_width, window_height)

window.show()
sys.exit(app.exec_())

