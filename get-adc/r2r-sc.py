import time
from r2r_adc import R2R_ADC
import adc_plot

voltage_values = []
time_values = []
duration = 3.0

try:
    adc = R2R_ADC(3.3, compare_time=0.0001, verbose=False)
    
    start_time = time.time()
    
    while (time.time() - start_time) < duration:
        voltage = adc.get_sar_voltage()  # используем метод ПП
        voltage_values.append(voltage)
        time_values.append(time.time() - start_time)
    
    # Строим график
    adc_plot.plot_voltage_vs_time(time_values, voltage_values, 3.3)
    
    # Строим гистограмму (если функция есть в adc_plot)
    if hasattr(adc_plot, 'plot_sampling_period_hist'):
        adc_plot.plot_sampling_period_hist(time_values)
    
finally:
    adc.deinit()
