from sklearn.tree import DecisionTreeClassifier

x = [[30],[40],[90],[100]]
y = ["Healthy","Healthy","Faulty","Faulty"]

model=DecisionTreeClassifier()

model.fit(x,y)

prediction = model.predict([[95]])

print("Prediction :",prediction[0])
