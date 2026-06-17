actual = "Faulty"
predicted = "Healthy"

if actual == "Faulty" and predicted == "Faulty":
    print("True Positive/TP")

elif actual == "Healthy" and predicted == "Healthy":
    print("True Negative/TN")

elif actual == "Healthy" and predicted == "Faulty":
    print("False Positive/FP")

else:
    print("False Negative/FN")