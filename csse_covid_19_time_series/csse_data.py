# %%
import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima_model import ARIMA, ARMA, AR
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller  
# %%
Confirmed = pd.read_csv("C:/Users/JayLa/OneDrive/Documents/GitHub/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv")
Deaths = pd.read_csv("C:/Users/JayLa/OneDrive/Documents/GitHub/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv")
Recovered = pd.read_csv("C:/Users/JayLa/OneDrive/Documents/GitHub/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv")
# %%
Confirmed["Case"] = "Confirmed"
Deaths["Case"] = "Deaths"
Recovered["Case"] = "Recovered"
# %%
All_Cases = pd.concat([Confirmed, Deaths, Recovered], axis=0)
# %%
All_Cases.to_csv("time_series_19-covid-Combined.csv", index=False)

# %%
Confirmed.T

# %%
