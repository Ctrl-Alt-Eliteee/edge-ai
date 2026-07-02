What is a hyperparameter?

Hyperparameters

These are chosen before training.

Example:

model = DecisionTreeClassifier(max_depth=3)

Here,

max_depth = 3

is a hyperparameter.

The model hasn't trained yet.

You're telling the model:

Don't grow deeper than 3 levels


Parameters vs Hyperparameters



| Parameters              | Hyperparameters     |
| ----------------------- | ------------------- |
| Learned by model        | Chosen by engineer  |
| Learned during training | Set before training |



What is max_depth?

max_depth means to how many depth the model should go


DecisionTreeClassifier(max_depth=1)

The tree is very small.

It may not learn enough.

↓

Underfitting.



DecisionTreeClassifier(max_depth=20)

The tree grows very deep.

It may memorize the training data.

↓

Overfitting.




DecisionTreeClassifier(max_depth=4)

A balanced tree.

Learns useful patterns.

↓

Good generalization

