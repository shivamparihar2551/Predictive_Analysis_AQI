import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report

from sklearn.tree import DecisionTreeClassifier, plot_tree


df = pd.read_csv("C:/Users/LENOVO/OneDrive/Desktop/semester 4/Python Toolbox/Air-Quality-Analysis-Python/data/AQI Dataset for project.csv")


print(df.head(100))
print(df.describe())
print(df.info())
print(df.isna().sum()) 


df = df.dropna()
print(df.isna().sum())
