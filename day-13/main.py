from sklearn.linear_model import LogisticRegression

x = [[30],[40],[90],[100]]
y=[0,0,1,1]

model=LogisticRegression()

model.fit(x,y)

prediction=model.predict([[95]])

print("Prediction:",prediction[0])