import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# ❤️ IL MIO AMORE ESPONENZIALE PER PIPPI ❤️
# ==========================================

# Dati del grafico
tempo = np.linspace(0, 10, 120)
intensita = np.linspace(0, 10, 120)
T, I = np.meshgrid(tempo, intensita)

# Crescita esponenziale dell'amore
Z = np.exp(0.35 * T) * (1 + 0.12 * I)

# Normalizzazione per rendere il grafico più leggibile
Z = Z / Z.max() * 100

# Creazione della figura 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection="3d")

superficie = ax.plot_surface(
    T, I, Z,
    cmap="plasma",
    edgecolor="none",
    alpha=0.92,
    antialiased=True
)

# Titolo e assi
ax.set_title(
    "❤️ L'AMORE ESPONENZIALE PER PIPPI ❤️\nUna crescita senza limite",
    fontsize=16,
    fontweight="bold",
    pad=22
)
ax.set_xlabel("Tempo insieme →", labelpad=12)
ax.set_ylabel("Tenerezza e complicità →", labelpad=12)
ax.set_zlabel("Intensità dell'amore (%)", labelpad=12)

# Barra dei colori
cbar = fig.colorbar(superficie, ax=ax, shrink=0.65, pad=0.12)
cbar.set_label("Livello di amore per Pippi")

# Vista e stile
ax.view_init(elev=28, azim=-135)
ax.text(5, 5, 105, "PIPPI ❤️", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.show()
