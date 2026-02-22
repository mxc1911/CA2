# target (y) >> track_popularity
# numaric features: artist_followers, album_total_tracks

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/hhatq/CA2/data/filtered_data_Statistics.csv")

# Remove useless columns
df = df.drop(columns=["Unnamed: 7", "Unnamed: 8"], errors="ignore")

# Remove summary rows (where track_popularity is NaN)
df = df[df["track_popularity"].notna()]

#select features 
features = ["artist_followers", "album_total_tracks"]
target = "track_popularity"

X = df[features]
y = df[target]

#train/test split (not full data)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#feature scaling
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#linear regression
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

#make predicts
y_pred = model.predict(X_test)


#evaluate R² Score (how good)
from sklearn.metrics import r2_score
print("R2:", r2_score(y_test, y_pred))

#evaluate RMSE (error size)
from sklearn.metrics import mean_squared_error
import numpy as np

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("RMSE:", rmse)

#viualise results

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Popularity")
plt.ylabel("Predicted Popularity")
plt.title("Actual vs Predicted")
plt.show()