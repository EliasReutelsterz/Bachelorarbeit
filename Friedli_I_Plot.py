#Abbildung 2.2 Funktion I(beta, 0, m) mit h = 0, Abbildung 2.6 Funktion I(beta, h, m) mit h = 0.05
#Dies ist der Programmcode für das Erstellen der Plots für die Funktion I

import plotly.express as px
import numpy as np
import pandas as pd

#Inputs
N = 100000
h = 0.05
beta1 = 0.7
beta2 = 1
beta3 = 1.3

#Definitionsbereich für m definieren
x = np.linspace(-1.0, 1.0, num = N + 1)
x = np.delete(x, [0, N])

#Funktion definieren
def f_beta_von_m_minus_hm(m_input, beta_input, h_input):
    e = -1/2 * m_input * m_input
    s = -(1-m_input)/2 * np.log((1-m_input)/2) - (1+m_input)/2 * np.log((1+m_input)/2)
    f = beta_input * e - s
    f_minus_hm = f - h_input * m_input
    return f_minus_hm

def I_beta_von_m(m_input, beta_input, h_input, f_minus_hm_minimum_input):
    I = f_beta_von_m_minus_hm(m_input, beta_input, h_input) - f_minus_hm_minimum_input
    return I
I_beta_von_m = np.frompyfunc(I_beta_von_m, 4, 1)


#1. Plot mit beta1 und h = 0
f_minus_hm_vektor1 = [f_beta_von_m_minus_hm(m, beta1, 0) for m in x]
f_minus_hm_minimum1 = min(f_minus_hm_vektor1)
y1 = I_beta_von_m(x, beta1, 0, f_minus_hm_minimum1)
df1 = pd.DataFrame({"m": x, "I(\u03B2,m)": y1}, columns=["m", "I(\u03B2,m)"])
fig = px.scatter(df1, x = "m", y = "I(\u03B2,m)")
fig.update_xaxes(range = [-1.2,1.2], title = "")
fig.update_yaxes(title = "", dtick=0.1)
fig.update_layout(font = dict(size = 50))
fig.update_traces(mode="markers+lines")
fig.show()

#2. Plot mit beta2 und h = 0
f_minus_hm_vektor2 = [f_beta_von_m_minus_hm(m, beta2, 0) for m in x]
f_minus_hm_minimum2 = min(f_minus_hm_vektor2)
y2 = I_beta_von_m(x, beta2, 0, f_minus_hm_minimum2)
df2 = pd.DataFrame({"m": x, "I(\u03B2,m)": y2}, columns=["m", "I(\u03B2,m)"])
fig = px.scatter(df2, x = "m", y = "I(\u03B2,m)")
fig.update_xaxes(range = [-1.2,1.2], title = "")
fig.update_yaxes(title = "", dtick=0.1)
fig.update_layout(font = dict(size = 50))
fig.update_traces(mode="markers+lines")
fig.show()

#3. Plot mit beta3 und h = 0
f_minus_hm_vektor3 = [f_beta_von_m_minus_hm(m, beta3, 0) for m in x]
f_minus_hm_minimum3 = min(f_minus_hm_vektor3)
y3 = I_beta_von_m(x, beta3, 0, f_minus_hm_minimum3)
df3 = pd.DataFrame({"m": x, "I(\u03B2,m)": y3}, columns=["m", "I(\u03B2,m)"])
fig = px.scatter(df3, x = "m", y = "I(\u03B2,m)")
fig.update_xaxes(range = [-1.2,1.2], title = "")
fig.update_yaxes(title = "", dtick=0.03)
fig.update_layout(font = dict(size = 50))
fig.update_traces(mode="markers+lines")
fig.show()

#4. Plot mit beta1 und h beliebig
f_minus_hm_vektor4 = [f_beta_von_m_minus_hm(m, beta1, h) for m in x]
f_minus_hm_minimum4 = min(f_minus_hm_vektor4)
y4 = I_beta_von_m(x, beta1, h, f_minus_hm_minimum4)
df4 = pd.DataFrame({"m": x, "I(\u03B2,m)": y4}, columns=["m", "I(\u03B2,m)"])
fig = px.scatter(df4, x = "m", y = "I(\u03B2,m)")
fig.update_xaxes(range = [-1.2,1.2], title = "")
fig.update_yaxes(title = "", dtick=0.1)
fig.update_layout(font = dict(size = 50))
fig.update_traces(mode="markers+lines")
fig.show()

#5. Plot mit beta2 und h beliebig
f_minus_hm_vektor5 = [f_beta_von_m_minus_hm(m, beta2, h) for m in x]
f_minus_hm_minimum5 = min(f_minus_hm_vektor5)
y5 = I_beta_von_m(x, beta2, h, f_minus_hm_minimum5)
df5 = pd.DataFrame({"m": x, "I(\u03B2,m)": y5}, columns=["m", "I(\u03B2,m)"])
fig = px.scatter(df5, x = "m", y = "I(\u03B2,m)")
fig.update_xaxes(range = [-1.2,1.2], title = "")
fig.update_yaxes(title = "", dtick=0.1)
fig.update_layout(font = dict(size = 50))
fig.update_traces(mode="markers+lines")
fig.show()

#6. Plot mit beta3 und h beliebig
f_minus_hm_vektor6 = [f_beta_von_m_minus_hm(m, beta3, h) for m in x]
f_minus_hm_minimum6 = min(f_minus_hm_vektor6)
y6 = I_beta_von_m(x, beta3, h, f_minus_hm_minimum6)
df6 = pd.DataFrame({"m": x, "I(\u03B2,m)": y6}, columns=["m", "I(\u03B2,m)"])
fig = px.scatter(df6, x = "m", y = "I(\u03B2,m)")
fig.update_xaxes(range = [-1.2,1.2], title = "")
fig.update_yaxes(title = "", dtick=0.05)
fig.update_layout(font = dict(size = 50))
fig.update_traces(mode="markers+lines")
fig.show()