import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
tips = sns.load_dataset("tips")

# Create a trellis plot
g = sns.FacetGrid(tips, col="time", row="smoker", margin_titles=True)
g.map(plt.scatter, "total_bill", "tip", color="#338844", edgecolor="white", s=50, lw=1)
g.set_axis_labels("Total bill (US Dollars)", "Tip")
g.set_titles(col_template="{col_name} patrons", row_template="{row_name}")
g.set(xlim=(0, 60), ylim=(0, 12), xticks=[10, 30, 50], yticks=[2, 6, 10])
g.despine(left=True, bottom=True)
plt.suptitle('Trellis Plot', size=16, weight='bold', y=1.02)
plt.show()
