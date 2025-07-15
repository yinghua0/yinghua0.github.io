"""
Merit Order Dispatch Demo
Author: Your Name
Description:
  Simple Python script to stack generator bids, meet demand,
  and find market clearing price.
"""

import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Example bid data: each generator's capacity and bid price
data = {
    'Generator': ['Gen A', 'Gen B', 'Gen C', 'Gen D'],
    'Capacity_MW': [50, 100, 75, 80],
    'Bid_Price_per_MWh': [20, 25, 30, 40]
}

df = pd.DataFrame(data)

# 2️⃣ Sort by bid price (merit order)
df_sorted = df.sort_values(by='Bid_Price_per_MWh').reset_index(drop=True)

# 3️⃣ Calculate cumulative capacity
df_sorted['Cumulative_Capacity'] = df_sorted['Capacity_MW'].cumsum()

# 4️⃣ Set demand
demand = 180  # MW

# 5️⃣ Find marginal generator (sets market price)
marginal_row = df_sorted[df_sorted['Cumulative_Capacity'] >= demand].iloc[0]
market_clearing_price = marginal_row['Bid_Price_per_MWh']

print("=== Merit Order Dispatch ===")
print(df_sorted)
print(f"\nDemand: {demand} MW")
print(f"Market Clearing Price: ${market_clearing_price} per MWh")

# 6️⃣ Plot supply stack
plt.step(
    [0] + df_sorted['Cumulative_Capacity'].tolist(),
    [0] + df_sorted['Bid_Price_per_MWh'].tolist(),
    where='post',
    label='Supply Stack'
)
plt.axvline(x=demand, color='red', linestyle='--', label='Demand')
plt.axhline(y=market_clearing_price, color='green', linestyle='--', label='Clearing Price')

plt.xlabel('Cumulative Capacity (MW)')
plt.ylabel('Bid Price ($/MWh)')
plt.title('Merit Order Dispatch Example')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
