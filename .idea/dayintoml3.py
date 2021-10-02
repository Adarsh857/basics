#KNN IS CLASSIFICATION ALGORITHM
#K NEAREST NEIGHBOURS  ,based on distance formula d=√((x_2-x_1)²+(y_2-y_1)²)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Social_Network_Ads.csv");
print("Data Imported For Modeling")
df.head(3)
df.tail(3)
df.describe()
X = df.iloc[:, [2, 3]].values
y = df.iloc[:, -1].values
#print(X)
#print(y)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 20, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)


# #making a confusion matrix
# from sklearn.metrics import confusion_matrix
# from sklearn.metrics import accuracy_score
# cm = confusion_matrix(y_test, y_pred)
# print(cm)
# print('Accuracy is :')
# print(accuracy_score(y_test,y_pred))

#visualizing the training set rules
# from matplotlib.colors import ListedColormap
# X_set, y_set = X_train, y_train
# X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
#                      np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
# plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
#              alpha = 0.25, cmap = ListedColormap(('red', 'green')))
# plt.xlim(X1.min(), X1.max())
# plt.ylim(X2.min(), X2.max())
# for i, j in enumerate(np.unique(y_set)):
#     plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
#                 c = ListedColormap(('yellow', 'blue'))(i), label = j)
# plt.title('K-NN (Training set)')
# plt.xlabel('Age')
# plt.ylabel('Estimated Salary')
# plt.legend()
# plt.show()

# #SVM MODEL
# from sklearn.svm import SVC
# classifier = SVC(kernel='linear',random_state=0)
# classifier.fit(X_train,y_train)
# #predicting the test set results
# y_pred=classifier.predict(X_test)
# from sklearn.metrics import confusion_matrix     #confusion matrix
# cm=confusion_matrix(y_test,y_pred)
# print(cm)
# # graph with svm
# from matplotlib.colors import ListedColormap
# X_set, y_set = X_train, y_train
# X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
#                      np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
# plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
#              alpha = 0.25, cmap = ListedColormap(('red', 'green')))
# plt.xlim(X1.min(), X1.max())
# plt.ylim(X2.min(), X2.max())
# for i, j in enumerate(np.unique(y_set)):
#     plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
#                 c = ListedColormap(('yellow', 'blue'))(i), label = j)
# plt.title('K-NN (Training set)')
# plt.xlabel('Age')
# plt.ylabel('Estimated Salary')
# plt.legend()
# plt.show()


#training the svm model on the training set
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
classifier =SVC(kernel ='rbf',random_state=0)
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)  #predicting the test set result
from sklearn.metrics import confusion_matrix   #making the confusion matrix
cm=  confusion_matrix(y_test, y_pred)
print(cm)
print('Accuracy is :')
print(accuracy_score(y_test,y_pred))

#visualizing the training set rules
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.25, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('yellow', 'blue'))(i), label = j)
plt.title('K-NN (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()