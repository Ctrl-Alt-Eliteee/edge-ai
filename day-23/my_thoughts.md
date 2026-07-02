Q1

Your manager says:

Increase max_depth to 100 for higher accuracy.

How would you respond?

So, maximum, making the maximum depth equal to 100 and then running the code. And you think that it will give me higher accuracy. Okay, well, the answer is, of course, it will do overfitting. Now, I'm not just saying that because of overfitting. Because if I do maximum depth is equal to 100%, that means the tree becomes too big. It will become too much complex, it will create too much complications, too much confusion to understand the things. Maximum depth equal to 100 is too vast for an ML engineer or anyone to understand the things because it will create too much complications. And not always the training accuracy higher means the good model. No. What if the model has training accuracy 100% and the testing accuracy 50%, 60%, 70%? That also means the model is overfitting. We want a model that fits into the criteria of good generalization. Neither overfitting nor underfitting. Now, good generalization means even though the model doesn't have accuracy 100%, it may have accuracy 96%, 94%, 95%. But the testing accuracy should also be 92%, 93% or anything. The percent gap between the training and testing accuracy should be minimum. That means that we have the perfect good generalization model. And that's why engineers don't optimize only for training accuracy because for them, along with the training accuracy, testing accuracy also matters. It is not important that how much the model memorizes. The model should learn and observe from the patterns of the training dataset. Memorizing is different thing, and learning and observing from the training dataset is really very different thing.




Q2

If collecting more data costs ₹5 lakh but changing a hyperparameter is free, which would you try first?

Why?

I would for sure try by changing hyperparameters not because it is free but it saves time. 
as collecting more data and then run the model again, then train dataset and all this shit, it will take my time more, so it will waste my time, it will take too much cost, and I think it is not practically as good as option A. And the model improvement can be done so much good by hhyperparameters.




Q3

Can a model have excellent training accuracy and still be a poor model?

Explain.

yes though model has excellent training accuracy it can be a poor model that is what overfitting is . 

And not always the training accuracy higher means the good model. No. What if the model has training accuracy 100% and the testing accuracy 50%, 60%, 70%? That also means the model is overfitting. We want a model that fits into the criteria of good generalization. Neither overfitting nor underfitting. Now, good generalization means even though the model doesn't have accuracy 100%, it may have accuracy 96%, 94%, 95%. But the testing accuracy should also be 92%, 93% or anything. The percent gap between the training and testing accuracy should be minimum and the training and testing accuracies should be maximum That means that we have the perfect good generalization model. And that's why engineers don't optimize only for training accuracy because for them, along with the training accuracy, testing accuracy also matters. It is not important that how much the model memorizes. The model should learn and observe from the patterns of the training dataset. Memorizing is different thing, and learning and observing from the training dataset is really very different thing.




Q4

If two models have similar test accuracy, which other things would you compare before deployment?

i will compare precision recall f1 score  before deploying beacuse what if model has good testing accuracy but poor recall and precision i don't want my model to raise too many false alarms or to say a faulty motor that it is healthy that means wrong prediction. 