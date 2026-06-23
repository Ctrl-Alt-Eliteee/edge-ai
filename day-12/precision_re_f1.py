from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score

y_test=[1,1,0,0]
predictions=[1,1,1,0]

print("Precision:",precision_score(y_test,predictions))
print("Recall:",recall_score(y_test,predictions))
print("F1 Score:",f1_score(y_test,predictions))