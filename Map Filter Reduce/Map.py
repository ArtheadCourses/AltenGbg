
def c2f(t):
    return (9.0/5) * t + 32

def f2c(t):
    return (5.0/9) * (t-32)

def main():
    temp_in_c = [16.3, 21.3, 19.7, 15.4]

    #f_temp = list(map(lambda t:(9.0/5) * t + 32, temp_in_c))
    f_temp = [(9.0/5) * t + 32 for t in temp_in_c]
    c_temp = list(map(f2c, f_temp))
    print(f_temp)
    print(c_temp)

    
if __name__ == '__main__':
    main()