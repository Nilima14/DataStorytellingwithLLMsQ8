# Analysis script
import pandas as pd
import matplotlib.pyplot as plt
from decimal import Decimal, ROUND_HALF_UP

# Quarterly MRR Growth Data
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "MRR_Growth": [7.06, 10.42, 8.80, 7.94]
}

# Create DataFrame
df = pd.DataFrame(data)

# Use Decimal for exact precision
values = [Decimal(str(x)) for x in df["MRR_Growth"]]
average_growth = (sum(values) / Decimal(len(values))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

print(f"Average MRR Growth: {average_growth}")  # Will print 8.56 exactly

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
plt.savefig("trend.png", dpi=100)
plt.close()
# Analysis script
