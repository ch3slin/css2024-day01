# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:40:03 2024

@author: ckeanu
"""

import pandas as pd

insurance_data = pd.read_csv("insurance_data.csv", header=[4])
print(insurance_data.info())

print("/n--------------------------/n")
country_data = pd.read_csv("country_data.csv")
print(country_data.info())
print(country_data.describe())
print("/n--------------------------/n")
diab_data = pd.read_csv("diab_data.csv")
print(diab_data.info())
print(diab_data.describe())
print("/n--------------------------/n")
housing_data = pd.read_csv("housing_data.csv")
print(housing_data.info())
print(diab_data.describe())
print("/n--------------------------/n")
iris = pd.read_csv("iris.csv")
print(iris.info())
print(diab_data.describe())

age = [30,25,29,46,22]
print(age)