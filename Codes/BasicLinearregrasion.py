# Import the necessary libraries
import numpy
import matplotlib.pyplot as plot
import pandas

def average(x):
    sum1=0;
    for i in x:
        sum1=sum1+i;    
    sum1=sum1/len(x)
    return sum1
def xy(x,y,avgX,avgY):
    sum3=0
    i=0
    while(i<len(x)):
        sum1=0
        sum2=0
        sum1=x[i]-avgX
        sum2=y[i]-avgY
        sum3=sum3+(sum1*sum2)
        i=i+1
        
    return sum3
def xy2(x,avgX):
    sum3=0
    i=0
    while(i<len(x)):
        sum1=0
        sum1=x[i]-avgX
        sum1=numpy.power(sum1,2)
        sum3=sum3+sum1
        i=i+1
        
    return sum3


def find(x,alpha,beta):
    i=0
    ypre=[]
#    print(ypre)
    while(i<len(x)):
        ypre.append(alpha*x[i]+beta)
        i=i+1
    
    return ypre

dataset = pandas.read_csv('salaryData.csv')

x = dataset['YearsExperience'].values
y = dataset['Salary'].values
#print(x)

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 2/3)

avgX=average(xTrain)
avgY=average(yTrain)
alpha=(xy(xTrain,yTrain,avgX,avgY)/xy2(xTrain,avgX))
beta=avgY-alpha*avgX
predictedY=find(xTest,alpha,beta)
predictedY=numpy.array(predictedY)

df = pandas.DataFrame({'Actual': yTest.flatten(), 'Predicted': predictedY.flatten()})
print(df)

df1 = df
df1.plot(kind='bar')
plot.show()

plot.scatter(xTest, yTest,  color='gray')
plot.plot(xTest, predictedY, color='red', linewidth=2)
plot.show()

MAE=0
MSE=0
i=0
while(i<len(yTest)):
    MAE=MAE+abs(yTest[i]-predictedY[i])
    MSE=MSE+numpy.power((yTest[i]-predictedY[i]),2)
    i=i+1
MAE=MAE/len(yTest)
MSE=MSE/len(yTest)
RMSE=numpy.power(MSE,1/2)

print('Mean Absolute Error:',MAE)  
print('Mean Squared Error:', MSE)  
print('Root Mean Squared Error:', RMSE)






