from sklearn.model_selection import train_test_split

x = [[30], [40], [90], [100]]
y = ["Healthy", "Healthy", "Faulty", "Faulty"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

print("x_train:", x_train)
print("x_test:", x_test)
print("y_train:", y_train)
print("y_test:", y_test)