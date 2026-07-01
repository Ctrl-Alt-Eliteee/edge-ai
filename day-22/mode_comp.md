| Model | Train | Test |
| ----- | ----: | ---: |
| A     |    62 |   60 |
| B     |    98 |   96 |
| C     |   100 |   63 |


Which is Underfitting?

model A

Which is Good Fit?

model B

Which is Overfitting?

model C

Which would you deploy?

model B



| Model | Train | Test | Precision | Recall |
| ----- | ----: | ---: | --------: | -----: |
| A     |   100 |   97 |        98 |     60 |
| B     |    96 |   95 |        90 |     95 |


Which would you deploy?

I will deploy model B

Why?

Personally like this question very much because, yeah, you're trying to test me, right? Okay. So, I will definitely prefer model B. Now, you may ask that why not model A, though it has more training accuracy, more testing accuracy than model B. See, model B has more recall than model A. And recall is something that is very important. Recall means something that though the model is faulty, it is saying that it is healthy. So, in, generally in precision and recalls, what precision tells us that how many false alarms are there, and what recalls tells us is like how many faults did we get and all this stuff. So, the more the recall, the more the good model is. So, according to me, the model B is good. And though the gap between the training and testing accuracy in model A is 3%, and in model B it is 1%. So yeah, this is another reason why I will choose model B. I will deploy model B. And yeah, this is it. Like, I being an engineer, I will not always look for accuracy, accuracy, accuracy. I will look beyond accuracy, I will look towards the recall, towards the precision, towards the F1 score. Also, model A has bad F1 score and model B has good F1 score, because precision and recall both are balanced. That is what F1 score means, right? So yeah, I will go for model B.