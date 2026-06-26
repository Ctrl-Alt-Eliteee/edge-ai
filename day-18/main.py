from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

print("X_train Shape:", x_train.shape)
print("X_test Shape:", x_test.shape)

print("y_train Shape:", y_train.shape)
print("y_test Shape:", y_test.shape)