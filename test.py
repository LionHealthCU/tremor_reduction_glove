import serial
import time 
import csv

start_time = time.time()

gyro = []
linear = []
with serial.Serial('/dev/cu.usbmodem92050701', 115200, timeout=1) as ser:
    while True:
        x = str(ser.readline().strip())
        x = x[2:-1]   
        try:
            type, values = x.split(" - ")       # read one byte   
            print(type)
            fake,x,hoe,y,slut,z = values.split(" ")
            
            print(values.split(": "))
            relative_time = time.time() - start_time
            to_add = (x,y,z, relative_time)
            if type == "Linear Acceration":
                linear.append(to_add)
                print(linear)
            elif type == "Gyro":
                gyro.append(to_add)
                print(gyro)
            if relative_time > 10:
                if relative_time > 10:
                    with open("data.csv", "w", newline="") as f:
                        writer = csv.writer(f)
                        writer.writerow(["sensor_type", "x", "y", "z", "time"])

                        for row in linear:
                            writer.writerow(["linear"] + list(row))

                        for row in gyro:
                            writer.writerow(["gyro"] + list(row))
                    print("Saved data to data.csv")
                    break 
        except Exception as e :
            print(e)