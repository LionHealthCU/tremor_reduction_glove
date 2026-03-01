import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt 

data_buffer = []
def process_accelerometer(Ax, Ay, Az, Wx, Wy, Wz):
    data_buffer.append(((Ax ** 2 + Ay ** 2 + Az ** 2) ** (1/2) , (Wx ** 2 + Wy ** 2 + Wz ** 2) ** (1/2)))

def main():
    process_accelerometer(3,4,5,6,7,8)
    process_accelerometer(3,4,5,6,7,8)
    process_accelerometer(3,4,5,6,7,8)
    print(data_buffer)
main()
