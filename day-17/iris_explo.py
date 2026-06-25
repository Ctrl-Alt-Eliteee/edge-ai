from sklearn.datasets import load_iris

iris = load_iris()

print("Shape:", iris.data.shape)
print("Feature Names:", iris.feature_names)
print("Target Names:", iris.target_names)

x = iris.data
y = iris.target

print("\nFirst 5 Feature Rows:")
print(x[:5])

print("\nFirst 5 Labels:")
print(y[:5])