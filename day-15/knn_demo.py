from sklearn.neighbors import KNeighborsClassifier

x = [[30],[40],[90],[100]]
y = [0,0,1,1]  #0=Healthy 1=faulty

model=KNeighborsClassifier(n_neighbors=3)
model.fit(x,y)

prediction = model.predict([[95]])

print("Prediction:",prediction[0])