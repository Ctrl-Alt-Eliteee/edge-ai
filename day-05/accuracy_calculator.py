tp = 20
tn = 70
fp = 5
fn =  5


correct_predictions = tp + tn
total_predictions = tp + tn + fp + fn

accuracy = (correct_predictions / total_predictions) * 100

print("Correct Predictions:", correct_predictions)
print("Total Predictions:", total_predictions)
print("Accuracy:", accuracy, "%")