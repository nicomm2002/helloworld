import sys
import mne
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Aplicar filtro pasa banda
def bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    if data.shape[-1] <= 33:
        raise ValueError("La longitud del vector de entrada debe ser mayor que padlen, que es 33")
    y = filtfilt(b, a, data, axis=0)
    return y

# Parámetros del filtro
lowcut = 0.5
highcut = 150
fs = 500  # Frecuencia de muestreo

# Cargar los datos EEG y aplicar el filtro
try:
    file_path = sys.argv[1]
    raw = mne.io.read_raw_eeglab(file_path, preload=True)
    data = raw.get_data()

    # Filtrar cada canal de datos EEG
    filtered_data = np.zeros_like(data)
    for i in range(data.shape[0]):
        filtered_data[i] = bandpass_filter(data[i], lowcut, highcut, fs)

    # Crear un objeto RawArray con los datos filtrados
    filtered_raw = mne.io.RawArray(filtered_data, raw.info)

    # Guardar los datos filtrados en un archivo .fif
    filtered_raw.save('filtered_eeg.fif', overwrite=True)
    print("Datos EEG filtrados guardados en 'filtered_eeg.fif'.")

    # Guardar los datos filtrados en un archivo de texto
    np.savetxt('filtered_eeg.txt', filtered_data.T)
    print("Datos EEG filtrados guardados en 'filtered_eeg.txt'.")

    # Visualizar los datos filtrados y guardar como imagen
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_data.T)
    plt.title('EEG Data - Bandpass Filtered')
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.savefig('filtered_eeg.png')
    print("Imagen de los datos EEG filtrados guardada en 'filtered_eeg.png'.")
    plt.close()

except Exception as e:
    print(f"Error al procesar los datos EEG: {e}")
    sys.exit(1)
