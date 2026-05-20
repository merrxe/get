import time
import matplotlib.pyplot as plt
from r2r_adc import R2R_ADC

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    
    plt.title("Зависимость напряжения от времени", fontsize=16, fontweight="bold")
    plt.xlabel("Время, с", fontsize=12)
    plt.ylabel("Напряжение, В", fontsize=12)
    
    plt.xlim(0, max(time) + 1)
    plt.ylim(0, max_voltage)
    
    plt.grid(True, alpha=0.3, linestyle="--")
    
    plt.tight_layout()
    plt.show()

voltage_values = []
time_values = []
duration = 3.0

try:
    adc = R2R_ADC(3.3, compare_time=0.0001, verbose=False)
    
    start_time = time.time()
    
    while (time.time() - start_time) < duration:
        voltage = adc.get_sar_voltage()
        voltage_values.append(voltage)
        time_values.append(time.time() - start_time)
    
    plot_voltage_vs_time(time_values, voltage_values, 3.3)
    
finally:
    adc.deinit()
