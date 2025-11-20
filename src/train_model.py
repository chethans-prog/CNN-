from tensorflow


import pandas as pandas
from datetime imoprt datatime 
import matplotlib.pyplot as plt
import os

os.makedirs("logs", exist_ok=True)

print(f"load minst dataset")

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

#normalizing the data
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

#reshaping the data
x_train = x_train.reshape(-1, 28, 28, 3)
x_test = x_test.reshape(-1, 28, 28, 3)

