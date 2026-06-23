from sklearn.metrics import confusion_matrix

y_test = ["Faulty", "Healthy", "Faulty", "Healthy"]
predictions = ["Faulty", "Healthy", "Healthy", "Faulty"]

cm = confusion_matrix(y_test, predictions)

print(cm)