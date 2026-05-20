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
        voltage = adc.get_sc_voltage()
        voltage_values.append(voltage)
        time_values.append(time.time() - start_time)
    
    adc_plot.plot_voltage_vs_time(time_values, voltage_values, 3.3)
    
finally:
    adc.deinit()        voltage = (value / 256) * self.dynamic_range
        if self.verbose:
            print(f"Напряжение: {voltage:.3f}В")
        return voltage
    
    def successive_approximation_adc(self):
        result = 0
        for bit in range(7, -1, -1):
            test_value = result | (1 << bit)
            self.number_to_dac(test_value)
            time.sleep(self.compare_time)
            
            if GPIO.input(self.comp_gpio) == GPIO.HIGH:
                result = test_value
        return result
    
    def get_sar_voltage(self):
        value = self.successive_approximation_adc()
        voltage = (value / 256) * self.dynamic_range
        if self.verbose:
            print(f"Напряжение: {voltage:.3f}В")
        return voltage
