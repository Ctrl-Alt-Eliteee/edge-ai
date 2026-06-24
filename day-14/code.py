from  sklearn.metrics import classification_report

y_test= [ 1,1,0,0]
predictions =  [1,1,1,0]

print(classification_report(y_test,predictions))
