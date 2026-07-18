import matplotlib.pyplot as plt

classes = ["Healthy", "Inner", "Ball", "Outer"]
rms = [0.07376, 0.29153, 0.13923, 0.66951]

colors = ["green", "orange", "gold", "red"]

plt.figure(figsize=(8,5))

bars = plt.bar(classes, rms, color=colors)

plt.title("RMS Comparison of Bearing Conditions", fontsize=14)
plt.xlabel("Bearing Condition")
plt.ylabel("RMS")

plt.grid(axis="y", linestyle="--", alpha=0.5)

# Display values on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.01,
        f"{height:.3f}",
        ha="center",
        fontsize=10
    )

plt.savefig("rms_comparison.png", dpi=300)

plt.show()