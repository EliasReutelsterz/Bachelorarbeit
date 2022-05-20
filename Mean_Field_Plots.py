#Abbildung 2.3 Mean-Field Gleichung Schnittpunkte h = 0, Mean-Field Gleichung Schnittpunkte mit h = 0.05
#Dies ist der Programmcode für das Erstellen der Plots für die Komponenten der Mean-Field Gleichung

import plotly.graph_objects as go
import numpy as np

#Inputs
beta1 = 0.7
beta2 = 1
beta3 = 1.3
h = 0.05
N = 100000

#Definitionsbereich
x = np.linspace(-1, 1, num = N)

#1. Plot mit beta3 und h = 0
fig = go.Figure()
fig.update_layout(font = dict(size = 50), legend=dict(yanchor="top",y=0.99,xanchor="left",x=0.01, bgcolor="LightSteelBlue"))
fig.update_layout(legend = {'itemsizing': 'constant'})
fig.add_trace(go.Scatter(x = x, y = x, mode = "lines+markers", name = "m"))
fig.add_trace(go.Scatter(x = x, y = np.tanh(x * beta1), mode = "lines+markers", name = "tanh(m\u03B2)"))
fig.show()

#2. Plot mit beta2 und h = 0
fig = go.Figure()
fig.update_layout(font = dict(size = 50), legend=dict(yanchor="top",y=0.99,xanchor="left",x=0.01, bgcolor="LightSteelBlue"))
fig.update_layout(legend = {'itemsizing': 'constant'})
fig.add_trace(go.Scatter(x = x, y = x, mode = "lines+markers", name = "m"))
fig.add_trace(go.Scatter(x = x, y = np.tanh(x * beta2), mode = "lines+markers", name = "tanh(m\u03B2)"))
fig.show()

#3. Plot mit beta3 und h = 0
fig = go.Figure()
fig.update_layout(font = dict(size = 50), legend=dict(yanchor="top",y=0.99,xanchor="left",x=0.01, bgcolor="LightSteelBlue"))
fig.update_layout(legend = {'itemsizing': 'constant'})
fig.add_trace(go.Scatter(x = x, y = x, mode = "lines+markers", name = "m"))
fig.add_trace(go.Scatter(x = x, y = np.tanh(x * beta3), mode = "lines+markers", name = "tanh(m\u03B2)"))
fig.show()

#4. Plot mit beta1 und h beliebig
fig = go.Figure()
fig.update_layout(font = dict(size = 50), legend=dict(yanchor="top",y=0.99,xanchor="left",x=0.01, bgcolor="LightSteelBlue"))
fig.update_layout(legend = {'itemsizing': 'constant'})
fig.add_trace(go.Scatter(x = x, y = x, mode = "lines+markers", name = "m"))
fig.add_trace(go.Scatter(x = x, y = np.tanh(x * beta1 + h), mode = "lines+markers", name = "tanh(m\u03B2 + h)"))
fig.show()

#5. Plot mit beta2 und h beliebig
fig = go.Figure()
fig.update_layout(font = dict(size = 50), legend=dict(yanchor="top",y=0.99,xanchor="left",x=0.01, bgcolor="LightSteelBlue"))
fig.update_layout(legend = {'itemsizing': 'constant'})
fig.add_trace(go.Scatter(x = x, y = x, mode = "lines+markers", name = "m"))
fig.add_trace(go.Scatter(x = x, y = np.tanh(x * beta2 + h), mode = "lines+markers", name = "tanh(m\u03B2 + h)"))
fig.show()

#6. Plot mit beta3 und h beliebig
fig = go.Figure()
fig.update_layout(font = dict(size = 50), legend=dict(yanchor="top",y=0.99,xanchor="left",x=0.01, bgcolor="LightSteelBlue"))
fig.update_layout(legend = {'itemsizing': 'constant'})
fig.add_trace(go.Scatter(x = x, y = x, mode = "lines+markers", name = "m"))
fig.add_trace(go.Scatter(x = x, y = np.tanh(x * beta3 + h), mode = "lines+markers", name = "tanh(m\u03B2 + h)"))
fig.show()