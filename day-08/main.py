from sklearn.tree import DecisionTreeClassifier

X = [[30], [40], [90], [100]]
y = ["Healthy", "Healthy", "Faulty", "Faulty"]

model = DecisionTreeClassifier()
model.fit(X, y)

print(model.predict([[40]]))
print(model.predict([[95]]))