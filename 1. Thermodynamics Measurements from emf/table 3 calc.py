import math

E0cell = float(input("What is the total E0cell value?\n"))
n = int(input("What is the value of n?\n"))
T = float(input("Enter temperature in Kelvin\n"))
row_list = []

def calc():
    Zn = float(input("Enter Zn concentration\n"))
    Cu = float(input("Enter  Cu concentration\n"))
    Ecell_exp = float(input("Enter experimental Ecell value\n"))

    Ecell_calculated = E0cell - (8.314*T/(n*96500))*math.log(Zn/Cu)
    error_percent = (Ecell_exp - Ecell_calculated)/Ecell_calculated*100
    Gibbs = -n*96500*Ecell_exp
    val_list = [Ecell_calculated, error_percent, Gibbs/1000]
    row_list.append(val_list)
    print("[Ecell (calculated), error percent, Delta G]")
    for i in row_list:
        print(i)

while True:
    resp = input("To calculate, type c \nTo view list of values calculated so far, press v")
    if resp == 'c':
        calc()
    if resp == 'v':
        print("[Ecell (calculated), error percent, Delta G]")
        for i in row_list:
            print(i)
    if resp == 'exit':
        break