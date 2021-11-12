import math
def process_input(input_vols:list, increment:float, n:int, V_inf: float ):
    time = 0
    values = []
    for i in range(1, n):
        # print(input_vols)
        # print(i)
        V_t = input_vols[i - 1]
        try:
            delta_V = V_inf - V_t
            log_delta_V = math.log10(delta_V)
            if time != 0:
                k = 2.303/time*(math.log10(V_inf - values[0][2]) -  log_delta_V) #used a log property right here
            else:
                k = 0
        except ValueError:
            log_delta_V = 0
            k = 0
        values.append([i, time, V_t, delta_V, log_delta_V, k])
        time += increment
    
    k_sum = 0
    for i in values:
        k_sum += i[5]
    
    if len(values) == 0:
        k_avg = 0
    else:
        k_avg = k_sum/(len(values) - 1)
    
    return values , k_avg



