#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 12:03:06 2022

Dataset from Kaggle
https://www.kaggle.com/datasets/loovmj/tokyo-weather-data

@author: akshaypopat
"""

import pandas as pd

data = pd.read_csv("~/Documents/Data Science/tokyo_climate/tokyo_data.csv")

data["y/m/d"].isnull().sum()
data["high(C)"].isnull().sum()
data["low(C)"].isnull().sum()
data["daylight_hours(hours)"].isnull().sum()

import datetime

data["Date"] = data["y/m/d"].apply(lambda x: datetime.datetime(int(x.split("/")[0]), int(x.split("/")[1]), int(x.split("/")[2])))

data.to_csv("~/Documents/Data Science/tokyo_climate/data_clean.csv", index=False)