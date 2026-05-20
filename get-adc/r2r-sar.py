import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    
    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
    
    def number_to_dac(self, number):
        binary = [int(bit) for bit in bin(number)[2:].zfill(8)]
        for i in range(8):
            GPIO.output(self.bits_gpio[i], binary[i])
    
    def sequential_counting_adc(self):
        for number in range(256):
            self.number_to_dac(number)
            time.sleep(self.compare_time)
            
            if GPIO.input(self.comp_gpio) == GPIO.HIGH:
                return number
        return 255
    
    def get_sc_voltage(self):
        value = self.sequential_counting_adc()
        voltage = (value / 256) * self.dynamic_range
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
