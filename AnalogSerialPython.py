import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import serial
import time

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
sig = None

# Initialize communication with serial port
arduino=serial.Serial('/dev/ttyUSB0',9600, timeout = 3.0)
print('conectado')


# This function is called periodically from FuncAnimation
def animate(i, xs, ys, sig):

    # Read sample from serial port
    arduino.write('s')
    while arduino.inWaiting() > 0:
        #sig = int(arduino.readline().strip())
        sig = float(arduino.readline().strip())
        print(sig)

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(sig)


    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Leyendo puerto serial')
    plt.ylabel('Amplitud')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, sig), interval=100)
plt.show()