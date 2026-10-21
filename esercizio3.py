
import numpy as np
import matplotlib.pyplot as plt

# ❤️ Quanto amo Pippi? ❤️

giorni = np.linspace(0, 10, 100)
amore = np.exp(giorni / 2)

plt.figure(figsize=(10, 6))

plt.plot(giorni, amore, color="deeppink", linewidth=3)

plt.title("Il mio amore per Pippi ❤️", fontsize=18)
plt.xlabel("Tempo passato insieme")
plt.ylabel("Livello del mio amore")

plt.grid(True, linestyle="--", alpha=0.4)

plt.text(
    4, 100,
    "Pippi, il mio amore per te cresce esponenzialmente! ❤️",
    fontsize=11,
    color="deeppink"
)

plt.tight_layout()
plt.show()
