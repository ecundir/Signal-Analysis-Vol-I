#@title 🎛️ Panel de Control: Experimento de Ruido Térmico
#@markdown Desliza para ajustar la calidad de la señal (SNR en dB).
snr_db = 15 #@param {type:"slider", min:0, max:30, step:1}
mostrar_senal_pura = True #@param {type:"boolean"}

import numpy as np
import matplotlib.pyplot as plt

# Generar señal base
bits = np.array([1, 0, 1, 1, 0, 1, 0, 0])
muestras = 100
señal_pura = np.repeat(bits, muestras)
t = np.linspace(0, len(bits), len(señal_pura))

# Generar AWGN basado en el slider
potencia_señal = np.mean(señal_pura**2)
snr_lineal = 10**(snr_db / 10)
potencia_ruido = potencia_señal / snr_lineal
ruido = np.random.normal(0, np.sqrt(potencia_ruido), señal_pura.shape)
señal_recibida = señal_pura + ruido

# Visualización
plt.figure(figsize=(10, 4))
plt.plot(t, señal_recibida, color='silver', label='Señal con Ruido (AWGN)')
if mostrar_senal_pura:
    plt.step(t, señal_pura, where='post', color='blue', linewidth=2, label='Señal Original')

plt.title(f"Simulación en Tiempo Real: SNR = {snr_db} dB")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.grid(True, linestyle='--')
plt.legend()
plt.show()
