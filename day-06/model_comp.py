precision_a = 95
recall_a = 40

precision_b = 75
recall_b = 90

if recall_b > recall_a:
    print("Model B is preferred for fault detection")
else:
    print("Model A is preferred")


#as recall means detecting fault that is why higher the recall the  more good model is 
   