import numpy
import pandas
import matplotlib.pyplot as plot
from sklearn import metrics
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import RepeatedKFold

dataset = pandas.read_csv('salaryData.csv')

x = dataset['YearsExperience'].values
y = dataset['Salary'].values
X = x.reshape(len(x),1)
Y = y.reshape(len(y),1)

kf = RepeatedKFold(n_splits=2, n_repeats=1, random_state=200) 
kf.get_n_splits(X)

for train_index, test_index in kf.split(X):
    xTrain, xTest = X[train_index], X[test_index]
    yTrain, yTest = Y[train_index], Y[test_index]
    
    regressor = DecisionTreeRegressor()
    regressor.fit(xTrain, yTrain)
    
    regr = AdaBoostRegressor()
    regr.fit(X, y)
    
    yPrediction = regressor.predict(xTest)
    yPred = regr.predict(xTest)
    
    df = pandas.DataFrame({'Actual': yTest.flatten(), 'Predicted(Decision Tree)': yPrediction.flatten(),'Predicted(Adaptive Boosting)': yPred.flatten()})
    print(df)
    
    df1 = df
    df1.plot(kind='bar')
    plot.show()
    
    plot.scatter(xTest, yTest,  color='blue')
    plot.plot(xTest, yPrediction, color='orange', linewidth=2)
    plot.plot(xTest, yPred, color='green', linewidth=2)
    
    plot.show()

    print('Mean Absolute Error (Decision Tree):', metrics.mean_absolute_error(yTest, yPrediction))  
    print('Mean Absolute Error (Adaptive Boosting):', metrics.mean_absolute_error(yTest, yPred))
    print('Mean Squared Error (Decision Tree):', metrics.mean_squared_error(yTest, yPrediction))  
    print('Mean Squared Error (Adaptive Boosting):', metrics.mean_squared_error(yTest, yPred))
   

