models = {
    "Decision Tree":0.85,
    "Logistic Regression":0.92
}

best_model=max(models,key=models.get) #A dictionary stores data  as key:value
#models.get is dictionary method

print("Best model:",best_model)

