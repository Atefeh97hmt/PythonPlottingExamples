from matplotlib_venn import venn2
import matplotlib.pyplot as plt

# Example data
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

venn2([set1, set2], set_labels=('Set 1', 'Set 2'))
plt.title('Venn Diagram')
plt.show()
