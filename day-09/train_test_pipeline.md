from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)


Step 1:

import train-test split function from scikit-learn

Step-2:

split the dataset 

80% --> training data
20% --> testing data

Step-3:

Train the model.

The model learns patterns from:

Training Features (X_train)
Training Labels (y_train)

Step-4:

 Predict on unseen data.

Now we're checking:

Can the model generalize?

instead of:

Can the model memorize?

Step-5:

calculate y_test