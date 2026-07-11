What is Cross Validation?

Instead of testing once...

We test multiple times.

The dataset is divided into several parts.

Each part gets a chance to become the test set.


Why isn't one train-test split enough?

Imagine I have thousand model samples. And there are 800 samples of training and 200 samples of testing. And the accuracy comes out to be 97%, for example. But what if that dataset is tested on only 200 samples? What if that 200 samples were unusually easy or unusually very difficult? That means that only that particular one train-test split data cannot determine the ability of the true model. It cannot determine the true ability of my model, right? So that's why what I have to do is I have to divide the dataset into four or five parts. And then I have to take another, like, cross-validation samples.