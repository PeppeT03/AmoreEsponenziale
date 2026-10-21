
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ❤️ PEPPE + PIPPI — CUORE 3D VERTICALE ❤️

# Contorno matematico del cuore
t = np.linspace(0, 2 * np.pi, 240)
r = np.linspace(0, 1, 100)
T, R = np.meshgrid(t, r)

# Sagoma del cuore: punta in basso, due lobi in alto
X = 16 * np.sin(T)**3 / 17
Z = (
    13 * np.cos(T)
    - 5 * np.cos(2*T)
    - 2 * np.cos(3*T)
    - np.cos(4*T)
) / 17

# Riempimento dal centro verso il contorno
X = R * X
Z = R * Z

# Profondità bombata lungo l'asse Y
Y = 0.30 * np.sqrt(np.maximum(0, 1 - R**2))

fig = plt.figure(figsize=(10, 9), facecolor="#090411")
ax = fig.add_subplot(111, projection="3d")

def aggiorna(frame):
    ax.clear()
    ax.set_facecolor("#090411")

    # Pulsazione
    battito = 1 + 0.035 * (1 - np.cos(frame * 0.16)) / 2

    # Rotazione attorno all'asse verticale Z
    angolo = np.radians(frame * 0.5)
    Xp = battito * (X * np.cos(angolo) - Y * np.sin(angolo))
    Yp = battito * (X * np.sin(angolo) + Y * np.cos(angolo))
    Zp = battito * Z

    colori = plt.cm.RdPu(0.25 + 0.7 * R)

    # Fronte e retro del cuore
    ax.plot_surface(
        Xp, Yp, Zp,
        facecolors=colori,
        linewidth=0,
        antialiased=True,
        shade=True
    )

    ax.plot_surface(
        Xp, -Yp, Zp,
        facecolors=colori,
        linewidth=0,
        antialiased=True,
        shade=True
    )

    ax.set_title(
        "PEPPE  ♥  PIPPI",
        color="#ff9cde",
        fontsize=23,
        fontweight="bold",
        pad=25
    )

    ax.text2D(
        0.5, 0.92,
        "Il mio amore per te tende a +∞",
        transform=ax.transAxes,
        ha="center",
        color="#ffd9f2",
        fontsize=13
    )

    # Manteniamo il cuore verticale nell'inquadratura
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_zlim(-1.3, 1.3)
    ax.set_box_aspect((1, 0.7, 1))
    ax.view_init(elev=8, azim=-90)
    ax.set_axis_off()

animazione = FuncAnimation(
    fig,
    aggiorna,
    frames=720,
    interval=40,
    blit=False
)

plt.show()
