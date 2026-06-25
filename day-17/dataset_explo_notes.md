Dataset Exploration:

The process of understanding a dataset before training  a machine learning model.

We explore a dataset to:

Understand the number of samples and features.
Check for missing or incorrect values.
Learn what each feature represents.
Understand the target labels.
Find any patterns or problems in the data.


Why shouldn't we directly do model.fit()?

if  we train  the model without exploring the data :
we may have missing or false values.
The model may perform poorly.
It becomes difficult to interpret the results.


x.shape:

It returns the dimensions of the feature dataset
(R,C)
(150,4)
150=number of samples(rows)
4=number of features(columns)


X.shape tells us the size of the dataset.