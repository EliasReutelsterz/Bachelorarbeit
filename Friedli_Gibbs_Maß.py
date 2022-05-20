#Abbildung 2.1 Gibbs-Maß mit h = 0 und Abbildung 2.4 Gibbs-Maß mit h = 0.001
#Dies ist der Programmcode für das Erstellen der Plots des Gibbs-Maßes in Abhängigkeit der Parameter N, h und beta

import plotly.express as px
import numpy as np
import scipy.special
import pandas as pd

#Inputs
N = 1000
h = 0.001
beta1 = 0.98
beta2 = 1
beta3 = 1.02

#Funktion definieren
x = np.linspace(-1.0, 1.0, num=N+1) #Definitionsbereich für m

def mü_mN_gleich_m(m_input, beta_input, h_input, Z_input):
    #In Z benutzen wir der Übersicht wegen i als Zählvariable, da m ja bereits Input für mü ist
    mü = 1/Z_input * scipy.special.binom(N, (1+m_input)/2*N) *np.exp((1/2)*beta_input*m_input*m_input*N + h_input*m_input*N)
    return mü
mü_mN_gleich_m = np.frompyfunc(mü_mN_gleich_m, 4, 1)

#1. Plot mit beta1 und h = 0
Z1 = np.sum([scipy.special.binom(N,(1+i)/2*N) * np.exp((1/2)*beta1*i*i*N + 0 *i*N) for i in x])
y1 = mü_mN_gleich_m(x, beta1, 0, Z1)
df1 = pd.DataFrame({"m": x, "\u03bc(mN = m)": y1}, columns=["m", "\u03bc(mN = m)"])
fig = px.scatter(df1, x = "m", y = "\u03bc(mN = m)")
fig.update_xaxes(range = [-1.2,1.2], title = "")
fig.update_yaxes(title = "", dtick=0.001)
fig.update_layout(font = dict(size = 50))
fig.update_traces(mode="markers+lines")
fig.show()

#2. Plot mit beta2 und h = 0
Z2 = np.sum([scipy.special.binom(N,(1+i)/2*N) * np.exp((1/2)*beta2*i*i*N + 0 *i*N) for i in x])
y2 = mü_mN_gleich_m(x, beta2, 0, Z2)
df2 = pd.DataFrame({"m": x, "\u03bc(mN = m)": y2}, columns=["m", "\u03bc(mN = m)"])
fig = px.scatter(df2, x = "m", y = "\u03bc(mN = m)")
fig.update_xaxes(range = [-1.2,1.2], title = "")
fig.update_yaxes(title = "", dtick=0.001)
fig.update_layout(font = dict(size = 50))
fig.update_traces(mode="markers+lines")
fig.show()

#3. Plot mit beta3 und h = 0
Z3 = np.sum([scipy.special.binom(N,(1+i)/2*N) * np.exp((1/2)*beta3*i*i*N + 0 *i*N) for i in x])
y3 = mü_mN_gleich_m(x, beta3, 0, Z3)
df3 = pd.DataFrame({"m": x, "\u03bc(mN = m)": y3}, columns=["m", "\u03bc(mN = m)"])
fig = px.scatter(df3, x = "m", y = "\u03bc(mN = m)")
fig.update_xaxes(range = [-1.2,1.2], title = "")
fig.update_yaxes(title = "", dtick=0.001)
fig.update_layout(font = dict(size = 50))
fig.update_traces(mode="markers+lines")
fig.show()

#4. Plot mit beta1 und h beliebig
Z4 = np.sum([scipy.special.binom(N,(1+i)/2*N) * np.exp((1/2)*beta1*i*i*N + h *i*N) for i in x])
y1 = mü_mN_gleich_m(x, beta1, h, Z4)
df1 = pd.DataFrame({"m": x, "\u03bc(mN = m)": y1}, columns=["m", "\u03bc(mN = m)"])
fig = px.scatter(df1, x = "m", y = "\u03bc(mN = m)")
fig.update_xaxes(range = [-1.2,1.2], title = "")
fig.update_yaxes(title = "", dtick=0.001)
fig.update_layout(font = dict(size = 50))
fig.update_traces(mode="markers+lines")
fig.show()

#5. Plot mit beta2 und h beliebig
Z5 = np.sum([scipy.special.binom(N,(1+i)/2*N) * np.exp((1/2)*beta2*i*i*N + h *i*N) for i in x])
y2 = mü_mN_gleich_m(x, beta2, h, Z5)
df2 = pd.DataFrame({"m": x, "\u03bc(mN = m)": y2}, columns=["m", "\u03bc(mN = m)"])
fig = px.scatter(df2, x = "m", y = "\u03bc(mN = m)")
fig.update_xaxes(range = [-1.2,1.2], title = "")
fig.update_yaxes(title = "", dtick=0.001)
fig.update_layout(font = dict(size = 50))
fig.update_traces(mode="markers+lines")
fig.show()

#6. Plot mit beta3 und h beliebig
Z6 = np.sum([scipy.special.binom(N,(1+i)/2*N) * np.exp((1/2)*beta3*i*i*N + h *i*N) for i in x])
y3 = mü_mN_gleich_m(x, beta3, h, Z6)
df3 = pd.DataFrame({"m": x, "\u03bc(mN = m)": y3}, columns=["m", "\u03bc(mN = m)"])
fig = px.scatter(df3, x = "m", y = "\u03bc(mN = m)")
fig.update_xaxes(range = [-1.2,1.2], title = "")
fig.update_yaxes(title = "", dtick=0.001)
fig.update_layout(font = dict(size = 50))
fig.update_traces(mode="markers+lines")
fig.show()