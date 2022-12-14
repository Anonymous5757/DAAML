import pandas as pd
import matplotlib as plt
import seaborn as sns

df=pd.read_csv('Heart.csv')
print(df.head())

#print shape of data
print(df.shape)

#find null values
print(df.isnull().sum())

#find data type
print(df.dtypes)

#find out zeros
print("total zeros :",df[df==0].count())

#print mean of age

print("mean age is:-",df['Age'].mean())

newdf=df[['Age','Sex','ChestPain','RestBP','Chol']]
print(newdf)

print("---------------------------------------------------------------")
#part b
import numpy as np
actual=list(np.ones(45))+list(np.zeros(55))
print("ACTUAL->")
print(np.array(actual))

predicted=list(np.ones(40))+list(np.zeros(52))+list(np.ones(8))
print("Predited ->")
print(np.array(predicted))

import matplotlib.pyplot as plt
from sklearn import metrics

confusion_matrix=metrics.confusion_matrix(actual,predicted)
cm_display=metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix,display_labels=[0,1])
cm_display.plot()
plt.show()

from sklearn.metrics import classification_report
print(classification_report(actual, predicted))

from sklearn.metrics import accuracy_score
print(accuracy_score(actual, predicted))
