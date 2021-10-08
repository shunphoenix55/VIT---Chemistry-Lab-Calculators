#This program generates values for Table 1 and then plots a graph with those values
#Values will have to be entered one by one

import math
from matplotlib import pyplot as plt

#These store the coordinates and the table values resp.
x_coordinates = []
y_coordinates = []
values = []

increment = float(input("Enter time interval in minutes\n"))
n = int(input("Enter number of values\n")) 
V_inf = float(input("Enter value of V at infinity\n"))   
time = 0

#for calculating values
def calculate(t, i):
    V_t = float(input(f"Enter value of V at {t} minutes\n"))
    delta_V = V_inf - V_t
    log_delta_V = math.log10(delta_V)
    if t != 0:
        k = 2.303/t*(math.log10(V_inf - values[0][2]) -  log_delta_V) #used a log property right here
    else:
        k = 0
    values.append([i, t, V_t, delta_V, log_delta_V, k])
    x_coordinates.append(t)
    y_coordinates.append(log_delta_V)

#gets values for each row
for i in range(1, n+ 1):
    calculate(time, i)
    time += increment

#prints data as table
print("[#, Vol of NaOH, V_inf - V_t,log(V_inf - V_t), k]")
for i in values:
    print(i)

#contains the coordinates for V_inf and V_0
x_slope = [x_coordinates[0], time - increment]
y_slope = [y_coordinates[0], y_coordinates[-1]]

#plots the graph
plt.plot(x_coordinates, y_coordinates, 'b-', x_slope, y_slope, 'r:')
plt.title("Plot of time Vs. log(V_infty - V_t)")
plt.show()

#calculating average rate constant
k_sum = 0
for i in values:
    k_sum += i[5]
k_avg = k_sum/len(values)
print(f"The average rate constant k is {k_avg}")



