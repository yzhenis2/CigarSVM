# Import train_test_split function
from sklearn.model_selection import train_test_split


import xlrd
import pandas as pd
import string
import numpy as np
from string import digits
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import cross_val_score

Review = "E:/academia/fall23/ADM/midterm/WS_cigar.xls"
reviews = xlrd.open_workbook(Review)
review = reviews.sheet_by_index(0)
wine_name = review.col_values(0,1,review.nrows)
score = review.col_values(1,1, review.nrows)
features = review.row_values(0,2, review.ncols)
data = np.zeros((review.nrows-1, review.ncols-2))

for i in range(1, review.nrows-1):
    data[i] = review.row_values(i,2,review.ncols)


X_train, X_test, y_train, y_test = train_test_split(data, score, test_size = 0.3)


#Create a svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel

#Train the model using the training sets
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)



# Model Accuracy: how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# Model Precision: what percentage of positive tuples are labeled as such?
print("Precision:",metrics.precision_score(y_test, y_pred, pos_label=str(1)))

# Model Recall: what percentage of positive tuples are labelled as such?
print("Recall:",metrics.recall_score(y_test, y_pred, pos_label=str(1)))

#5-fold validation
fold_scores = cross_val_score(clf,data,score,cv=5)
print("5-fold validation scores: ", fold_scores)
