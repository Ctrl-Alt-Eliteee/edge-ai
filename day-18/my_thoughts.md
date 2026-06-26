Why shouldn't we use:

model.fit(X_test, y_test)

instead of

model.fit(X_train, y_train)


because we shouldn't train on X_test and y_test as test dataset should remain completely unseen during training.  If the model is trained on test data , it can memorize the examples which  will lead to unfair evaluation . this leads to data leakage.


Data leakage:


data leakage happens when info from test data accidently influences the training process.


Why do we compare:

y_test

with

predictions

instead of comparing with y_train?

y_test means actual answer and predictions is prediction so we compare actual answer with predicted ones.

The predicted labels are compared with the actual labels to measure the model's performance.

