from plotly.graph_objects import Bar, Layout
from plotly import offline

from die import Die

die = Die()

results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequences = []

for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequences.append(frequency)

x_values = list(range(1,die.num_sides + 1))
data = [Bar(x = x_values, y = frequences)]

x_axis_config = {'title': 'Wynik'}
y_axis_config = {'title': 'Czestotliwość występowania'}
my_layout = Layout(title = 'Wynik rzucania kością 1000 razy', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename = 'd6.html')