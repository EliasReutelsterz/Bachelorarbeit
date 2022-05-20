#Abbildung 2.8 Funktion m(beta,h) mit beta variabel
#Dies ist der Programmcode für das Erstellen der Plots für die Funktion m(beta,h) mit variablem beta, also in 3 Dimensionen

import numpy as np
import plotly.graph_objects as go

#! mit N = 10000, h = 401, beta = 121 Rundungsfehler nahezu beseitigt aber Laufzeit etwa 60 Minuten
#Inputs
N = 10000
anzahl_h = 401
anzahl_beta = 121
h = np.linspace(-0.8, 0.8, num = anzahl_h)
beta = np.linspace(0.7, 1.3, num = anzahl_beta)

#Definitionsbereich m
m = np.linspace(-1.0, 1.0, num = N + 1)
m = np.delete(m, [0, N])

#Funktion definieren
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


#Plot
z1 = np.zeros((anzahl_h, anzahl_beta))
for i in range(len(z1)):
    for j in range(len(z1[1])):
        z1[i][j] = argmin_I_beta_von_m(h[i], beta[j])
fig = go.Figure(go.Surface(
    contours = {
        "x": {"show": True, "start": -1, "end": 1, "size": 0.04, "color":"white"},
        "y": {"show": True, "start": 0.5, "end": 1.5, "size": 0.04, "color":"white"},
        "z": {"show": True, "start": -1, "end": 1, "size": 0.05}
    },
    x = h,
    y = beta,
    z = z1.T))    
fig.update_layout(
    scene = {
        "xaxis": {"title": "h", "nticks": 4, "tickfont": {"size": 20}},
        "yaxis": {"title": "\u03B2", "nticks": 4, "tickfont": {"size": 20}},
        "zaxis": {"title": "m(\u03B2, h)","nticks": 4, "tickfont": {"size": 20}},
        'camera_eye': {"x": 0, "y": -1, "z": 0.5},
        "aspectratio": {"x": 1, "y": 1, "z": 0.2}
    },
    font = dict(size = 30)
)
fig.show()
