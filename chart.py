import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Generate synthetic marketing campaign data ---
np.random.seed(42)
n = 100

# Example context: marketing spend vs. customer acquisition
data = pd.DataFrame({
    "Marketing_Spend": np.random.normal(5000, 1500, n).clip(1000, 10000),
    "New_Customers": np.random.normal(200, 50, n).clip(50, 400),
    "Channel": np.random.choice(["Social Media", "Email", "TV", "Radio"], n)
})

# --- Professional Seaborn Styling ---
sns.set_style("whitegrid")
sns.set_context("talk")

# --- Create scatterplot ---
plt.figure(figsize=(8, 8))   # 8 inches × 64 dpi = 512 pixels
scatter = sns.scatterplot(
    data=data,
    x="Marketing_Spend",
    y="New_Customers",
    hue="Channel",
    palette="deep",
    s=80,
    alpha=0.8
)

# Titles and labels
plt.title("Marketing Spend vs Customer Acquisition", fontsize=16, weight="bold")
plt.xlabel("Marketing Spend (USD)", fontsize=12)
plt.ylabel("New Customers Acquired", fontsize=12)

# --- Save plot ---
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
