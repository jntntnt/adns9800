import serial
import numpy
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def getmatrix():
    ser = serial.Serial('/dev/cu.usbmodem1421')
    raw = ser.read(7000)
    #strip data before 'x'
    for c in raw:
        if c != 'x':
            raw = raw[1:]
        else:
            break
    raw = raw[1:]
    #strip data after 'x'
    raw = raw.split('x')
    raw = raw[0]
    raw = raw[:-1]
    raw = numpy.matrix(raw)
    raw = raw.astype(float)
    for x in numpy.nditer(raw, op_flags=['readwrite']):
        x[...] = x/127
#print type(x)
    return raw

plt.ion()
plt.axis('off') # clear x- and y-axes
b = getmatrix()
pic = plt.imshow(b, cmap = cm.Greys_r)

for y in range(10000):
    b = getmatrix()
    pic.set_data(b)
    plt.draw()
