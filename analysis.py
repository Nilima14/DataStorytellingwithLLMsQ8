import matplotlib.pyplot as plt

# Quarterly MRR Growth Data
quarters = ["Q1", "Q2", "Q3", "Q4"]
mrr_growth = [7.06, 10.42, 8.8, 7.94]
industry_target = 15
average = sum(mrr_growth) / len(mrr_growth)

print("Average MRR Growth:", round(average, 2))  # should print 8.56

# Plot trend
plt.figure(figsize=(6,4))
plt.plot(quarters, mrr_growth, marker="o", label="Company MRR Growth")
plt.axhline(y=industry_target, color="r", linestyle="--", label="Industry Target (15)")
plt.title("Quarterly MRR Growth vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("MRR Growth (%)")
plt.legend()
plt.tight_layout()
plt.savefig("trend.png")
