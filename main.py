import pandas as pd
import numpy as np
<<<<<<< HEAD
from helper_functions import create_X, create_y_train, train_model, predict, score, normalize_X
from sklearn.linear_model import LinearRegression
from sklearn.linear_model.ridge import Ridge
from sklearn.linear_model import Lasso
=======
from helper_functions import create_X, create_y_train, train_model, predict, score
>>>>>>> 0e453a6a82a8c1a46c61f3419a174391e7c7affd

train = pd.read_csv('data/Train.csv', parse_dates=['saledate'])
test = pd.read_csv('data/Test.csv', parse_dates=['saledate'])


X_train = create_X(train)
X_test = create_X(test)
y_train = create_y_train(train)

<<<<<<< HEAD
X_train_normalized, X_test_normalized = normalize_X(X_train, X_test)

model_linear = train_model(X_train, y_train, LinearRegression())
model_ridge = train_model(X_train_normalized, y_train, Ridge())
model_lasso = train_model(X_train_normalized, y_train, Lasso(alpha=0.00005, max_iter=120000))

submit_linear = predict(model_linear, test, X_test, 'model_lin')
submit_ridge = predict(model_ridge, test, X_test_normalized, 'model_rid')
submit_lasso = predict(model_lasso, test, X_test_normalized, 'model_las')

y_test = pd.read_csv('data/do_not_open/test_soln.csv')

print('Linear: ', score(submit_linear, y_test), '; Ridge: ', score(submit_ridge, y_test), '; Lasso: ', score(submit_lasso, y_test))
# Linear:  0.40826129534246886 ; Ridge:  0.40822991882415727 ; Lasso:  0.40834486305959367
# Pick Ridge
=======
model = train_model(X_train, y_train)

submit = predict(model, test, X_test, 'model_1')

y_test = pd.read_csv('data/do_not_open/test_soln.csv')

print(score(submit, y_test)) # final score: 0.4102042700770253
>>>>>>> 0e453a6a82a8c1a46c61f3419a174391e7c7affd
