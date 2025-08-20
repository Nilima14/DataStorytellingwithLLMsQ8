import pandas as pd
import matplotlib.pyplot as plt

# Quarterly MRR Growth Data
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "MRR_Growth": [7.06, 10.42, 8.80, 7.94]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate average
average_growth = df["MRR_Growth"].mean()
print(f"Average MRR Growth: {average_growth:.2f}")

# Industry target
industry_target = 15

# Plot trend
plt.figure(figsize=(6, 6))
plt.plot(df["Quarter"], df["MRR_Growth"], marker="o", label="Company MRR Growth")
plt.axhline(y=industry_target, color="r", linestyle="--", label="Industry Target (15)")
plt.title("Quarterly MRR Growth vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("MRR Growth")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("trend.png")  # Save chart for README
plt.show()
