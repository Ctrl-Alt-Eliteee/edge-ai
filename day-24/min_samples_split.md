Define:


it is a hyperparameter used to explain the minimum number of training samples required in a node before the decision tree is allowed to split .


Why it is a hyperparameter:


Hyperparameters don't change the dataset. They change how the model learns from the dataset.

What happens when it is too small?

The tree keeps splitting..... and splitting and splitting....


It undergoes 

overfitting


Effect on training accuracy


good training accuracy

Effect on testing accuracy

poor testing accuracy

Type of fitting

overfitting


What happens when it is too large?

The tree stopped splitting too early because min_samples_split is bigger number


Effect on the tree

tree undergoes underfitting  It became too restrictive.
Effect on training accuracy

poor training accuracy


Effect on testing accuracy

poor testing accuracy

Type of fitting

underfitting


| Small Value | Medium Value | Large Value |
| ----------- | ------------ | ----------- |
| model       |  good        |model        |
 undergoes    | generalization undergoes   |
 overfitting  |              |underfitting |
