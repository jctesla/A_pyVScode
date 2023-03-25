import matplotlib.pyplot as plt
# Datos
xlbl_level = ['Java', 'Python', 'PHP', 'JScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# etiquetas X, Y
plt.xlabel("Languages")
plt.ylabel("Popularity")

x_pos = [i for i,j in enumerate(xlbl_level)]          # sustrae solo indice solo [0, 1, 2, 3, 4, 5]
plt.title("Programming Language\n" + "Worldwide, Oct 2017 vs 2016")
plt.xticks(x_pos, xlbl_level)

# Select the width of each bar and their positions
width = [0.1,0.2,0.5,1.1,0.2,0.3]
y_pos = [0,.8,1.5,3,5,6]

# Create bars
plt.bar(y_pos, popularity, width=width)
plt.xticks(y_pos, xlbl_level)

# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()