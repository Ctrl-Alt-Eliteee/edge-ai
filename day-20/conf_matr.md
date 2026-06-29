Confusion matrix:-

A confusion matrix tells us which classes are being confused.


from sklearn.metrics import confusion_matrix



cm = confusion_matrix(y_test, predictions)

we use this to represent the confusion matrix.


Why do we need it when we already have Accuracy?


We need it  beacuse only accuracy does not tell us about precison , recall and f1 score.

that means we are not able to find how many false alarms are there how many faults are detected and f1 score balance that is why alongwith accuracy confusion matrix is also very important.



Why can two models with the same accuracy have different confusion matrices?


if the accuracy is both the models is same then we ask that which mistaked was more acceptable?

