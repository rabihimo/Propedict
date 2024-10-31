# prompt: give me a code with the predictive price of the top five companies S&P500 with graph

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the top 5 S&P 500 companies (replace with your desired tickers)
tickers = ['AAPL', 'MSFT', 'AMZN', 'GOOG', 'TSLA']

# Download historical data
data = yf.download(tickers, period="5y")  # Adjust the period as needed

# Extract adjusted closing prices
adj_close = data['Adj Close']

# Calculate percentage change
returns = adj_close.pct_change()

# Calculate rolling mean and standard deviation
rolling_mean = returns.rolling(window=20).mean()  # Adjust the window as needed
rolling_std = returns.rolling(window=20).std()

# Plot the results
plt.figure(figsize=(14, 7))
for ticker in tickers:
  plt.plot(adj_close.index, adj_close[ticker], label=ticker)

plt.xlabel('Date')
plt.ylabel('Adjusted Closing Price')
plt.title('Adjusted Closing Price of Top 5 S&P 500 Companies')
plt.legend()
plt.grid(True)
plt.show()

# Predictive modeling (simple example using linear regression) - requires further refinement
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# Example for AAPL (repeat for other tickers)
X = np.arange(len(adj_close['AAPL'])).reshape(-1, 1)  # Use index as predictor
y = adj_close['AAPL'].values.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# Plot the predictions against actual values
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, label='Actual Prices')
plt.plot(X_test, predictions, color='red', label='Predicted Prices')

plt.xlabel('Time Index')
plt.ylabel('Adjusted Close Price')
plt.title('Linear Regression Prediction for AAPL')
plt.legend()
plt.show()

print("Note: This is a very basic linear regression example. For more accurate predictions, consider using more sophisticated models, adding more features, and handling time series data appropriately.")
