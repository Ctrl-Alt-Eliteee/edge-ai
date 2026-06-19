precision = 0.8
recall = 0.8

f1 =  2 * (precision * recall) / (precision + recall)

print("Precision :",precision*  100,"%")
print("Recall :",recall *100,"%")
print("F1 Score:",round(f1 * 100,2),"%")
