import serial

gyro = []
linear = []
with serial.Serial('/dev/cu.usbmodem92050701', 115200, timeout=1) as ser:
    while True:
        x = str(ser.readline().strip())
        x = x[2:-1]   
        type, values = x.split(" - ")       # read one byte
        print(type)
        fake,x,hoe,y,slut,z = values.split(" ")
        
        print(values.split(": "))
        to_add = (x,y,z)
        if type == "Linear Acceration":
            linear.append(to_add)
            print(linear)
        elif type == "Gyro":
            gyro.append(to_add)
            print(gyro)