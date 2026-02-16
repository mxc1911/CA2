import json
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score 

DATA_PATH = os.path.join("..", "data", "filtered_data_Statistics.csv")
RESULTS_DIR = os.path.join("..", "site", "assets")
RESULTS_PATH = os.path.join(RESULTS_DIR, "results.json")

df = pd.read_csv("")