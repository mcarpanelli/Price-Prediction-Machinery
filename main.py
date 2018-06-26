import pandas as pd
import numpy as np
from helper_functions import create_X, create_y_train, train_model, predict, score

train = pd.read_csv('data/Train.csv', parse_dates=['saledate'])
test = pd.read_csv('data/Test.csv', parse_dates=['saledate'])


X_train = create_X(train)
X_test = create_X(test)
y_train = create_y_train(train)

model = train_model(X_train, y_train)

submit = predict(model, test, X_test, 'model_1')

y_test = pd.read_csv('data/do_not_open/test_soln.csv')

print(score(submit, y_test)) # final score: 0.4102042700770253