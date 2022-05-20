#Abbildung 2.7 Funktion m(beta,h) mit beta konstant
#Dies ist der Programmcode für das Erstellen der Plots für die Funktion m(beta,h) mit konstantem beta, also in 2 Dimensionen

import plotly.express as px
import numpy as np
import pandas as pd

#Inputs
N = 10000
h = np.linspace(-1, 1, num = 1000)
beta1 = 0.7
beta2 = 1
beta3 = 1.3

#Definitionbereich für m
m = np.linspace(-1.0, 1.0, num = N + 1)
m = np.delete(m, [0, N])

#Funktionen definieren
def f_beta_von_m_minus_hm(m_input, beta_input, h_input):
    e = -1/2 * m_input * m_input
    s = -(1-m_input)/2 * np.log((1-m_input)/2) - (1+m_input)/2 * np.log((1+m_input)/2)
    f = beta_input * e - s
    f_minus_hm = f - h_input * m_input
    return f_minus_hm

def argmin_I_beta_von_m(h_input, beta_input):
    f_vektor = [f_beta_von_m_minus_hm(m_zählvariable, beta_input, h_input) for m_zählvariable in m]
    argmin_I = np.argmin(f_vektor)*2/N - 1
    return argmin_I
argmin_I_beta_von_m = np.frompyfunc(argmin_I_beta_von_m, 2, 1)

#1. Plot mit beta1
y1 = argmin_I_beta_von_m(h, beta1)
df1 = pd.DataFrame({"h": h, "m(\u03B2,h)": y1}, columns=["h", "m(\u03B2,h)"])
fig = px.scatter(df1, x = "h", y = "m(\u03B2,h)")
fig.update_xaxes(range = [-1.2,1.2], title = "")
fig.update_yaxes(title = "", dtick=0.8)
fig.update_layout(font = dict(size = 50))
fig.update_traces(mode="lines+markers")
fig.show()

#2. Plot mit beta2
y2 = argmin_I_beta_von_m(h, beta2)
df2 = pd.DataFrame({"h": h, "m(\u03B2,h)": y2}, columns=["h", "m(\u03B2,h)"])
fig = px.scatter(df2, x = "h", y = "m(\u03B2,h)")
fig.update_xaxes(range = [-1.2,1.2], title = "")
fig.update_yaxes(title = "", dtick=0.8)
fig.update_layout(font = dict(size = 50))
fig.update_traces(mode="lines+markers")
fig.show()

#3. Plot mit beta3
y3 = argmin_I_beta_von_m(h, beta3)
df3 = pd.DataFrame({"h": h, "m(\u03B2,h)": y3}, columns=["h", "m(\u03B2,h)"])
fig = px.scatter(df3, x = "h", y = "m(\u03B2,h)")
fig.update_xaxes(range = [-1.2,1.2], title = "")
fig.update_yaxes(title = "", dtick=0.8)
fig.update_layout(font = dict(size = 50))
fig.update_traces(mode="lines+markers")
fig.show()