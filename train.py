import tensorflow as tf
import numpy as np # for numerical operations and linear algebra
import matplotlib.pyplot as plt
import pandas as pd

image_dir = "C:\Users\austi\Downloads\datasetImages_warp256"
csv_path = "C:\Users\austi\Downloads\Dataset.csv"

batch_size = 32
epochs = 50

csv_dataframe = pd.read_csv(csv_path, delimiter=',')
print(csv_dataframe.head())

