
import pandas as pd
from sklearn.metrics import accuracy_score # For Checking Accuracy
from sklearn.model_selection import train_test_split # Splitting Data For Train Test
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB # For Multinomial Naive Bayes Model
from sklearn.model_selection import cross_val_score # For Cross Validation
from sklearn.preprocessing import MinMaxScaler

train = pd.read_csv("train.csv")
test = pd.read_csv('test.csv')

del train['id']
del train['f_27']
del test['f_27']
trainDTar = train.drop(columns=['target'])
scaler = MinMaxScaler()
print(scaler.fit(trainDTar))
newtrain = scaler.transform(trainDTar)
MinMaxScaler()
lstCol = list(trainDTar.columns)

newtrainDF = pd.DataFrame(newtrain, columns=lstCol)

X = newtrainDF
y = train['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
from sklearn.naive_bayes import MultinomialNB 
mnb_clf = MultinomialNB()
res = mnb_clf.fit(X_train, y_train)
mnbPred = mnb_clf.predict(X_test)
mnbAcc = metrics.accuracy_score(y_test, mnbPred)
print (mnbAcc*100)

nav_clf = MultinomialNB()
nav_scores = cross_val_score(nav_clf, X_train, y_train, cv=6)
print('Naive Bayes Scores: ',nav_scores)
nav_mean = nav_scores.mean()
print('Naive Bayes Mean Score: ',nav_mean)
sumbulCSV = test[['id']]
prd = test.drop(columns=['id'])
testPRD = mnb_clf.predict(prd)


print(testPRD)

sumbulCSV.to_csv('Mustafa.csv', index=False)


