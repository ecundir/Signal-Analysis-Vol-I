import numpy as np
import matplotlib.pyplot as plt

# 1. Parámetros de la señal
bits = np.array([1, 0, 1, 1, 0, 1, 0, 0])
muestras_por_bit = 100
t = np.linspace(0, len(bits), len(bits) * muestras_por_bit)
señal_pura = np.repeat(bits, muestras_por_bit)

# 2. Generar Ruido Térmico (AWGN)
snr_db = 20  # Relación Señal-Ruido en Decibelios
potencia_señal = np.mean(señal_pura**2)
snr_lineal = 10**(snr_db / 10)
potencia_ruido = potencia_señal / snr_lineal
ruido = np.random.normal(0, np.sqrt(potencia_ruido), señal_pura.shape)

# 3. Señal Recibida (Aditiva)
señal_recibida = señal_pura + ruido

# Graficación Profesional
plt.figure(figsize=(12, 5))
plt.plot(t, señal_recibida, color='silver', label='Señal con Ruido (AWGN)')
plt.step(t, señal_pura, where='post', color='blue', linewidth=2, label='Señal Original (Bits)')

# --- Títulos de los Ejes ---
plt.title(f"Impacto del Ruido Térmico en la Transmisión (SNR = {snr_db} dB)", fontsize=14)
plt.xlabel("Tiempo (normalizado por bit)", fontsize=12)
plt.ylabel("Amplitud (Voltaje)", fontsize=12)
# ---------------------------

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper right')
plt.tight_layout() # Ajusta los márgenes para que no se corten los títulos
plt.show()