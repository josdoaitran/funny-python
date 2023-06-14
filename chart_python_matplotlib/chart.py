import matplotlib.pyplot as plt
# Dataset
country = ['England', 'Ammerican', 'France', 'Dermank', 'Italy']
gdp_per_capita = [45000, 42000, 52000, 49000, 47000]

plt.bar(country, gdp_per_capita)
plt.title('Country Vs GDP Per Capita')
plt.xlabel('Country')
plt.ylabel('GDP Per Capita')
plt.show()