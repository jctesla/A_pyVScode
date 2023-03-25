# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load an example dataset, podriamos usar tmbn
# podríamos haberlos cargado con pandas.read_csv()
tips = sns.load_dataset("tips")

# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)