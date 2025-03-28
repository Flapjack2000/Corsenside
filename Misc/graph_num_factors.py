"""
Graph the Number of Factors of a Range of Integers
"""
import math
import time
import matplotlib.pyplot as plt

def graph_factors_in_range(x_min, x_max):

    # make sure the min is a positive integer, default to (1)
    if x_min < 2 or x_min % 1:
        x_min = 1

    # make sure the max is a positive integer, default to (100,000)
    if x_max < x_min or x_max % 1:
        x_max = 1

    # make window readable
    if x_max <= 100:
        y_max: int = 13
    elif x_max <= 1000:
        y_max: int = 35
    elif x_max<= 10000:
        y_max: int = 70
    elif x_max <= 100000:
        y_max: int = 140
    elif x_max <= 1000000:
        y_max: int = 260
    else:
        y_max: int = int(math.log10(x_max))

    # compute num factors/coords
    x_coords = [i for i in range(x_min, x_max + 1)]
    y_coords = [len(factor(i)) for i in x_coords]

    # plot integers and their numbers of factors
    plt.plot(x_coords, y_coords)

    # plots every time a new biggest number of factors is found
    new_record = 1
    for index, y in enumerate(y_coords):
        if y > new_record:
            plt.plot([x_coords[index]], [y], 'ro')
            plt.annotate(text=f'{str(x_coords[index])}, {str(y)}',
                         xy=(x_coords[index], y))
            new_record = y

    # Graph labels
    plt.title('Integers and their number of factors')
    plt.axis((x_min, x_max, 0, y_max))
    plt.ylabel("# of Factors")
    plt.xlabel("Integers")
    plt.show()

def factor(n: int) -> list:
    # Check for factors under sqrt(n)
    factors = [i for i in range(1, int(math.sqrt(n)) + 1) if n / i % 1 == 0]

    # If (i) is a factor, then (n/i) must also be a factor
    # Don't add duplicates from perfect squares
    factors.extend([int(n / f) for f in factors if (n / f % 1 == 0) and (n / f not in factors)])

    return sorted(factors)

if __name__ == '__main__':
    print("This program graphs the number of factors of each integer between 1 and an inputted upper bound.\n"
          "Simultaneously, it marks the point every time a new record number of factors is found.\n"
          "Entering powers of 10 will look the nicest. Enter -1 to quit.")

    while True:
        upper_bound = int(input("Enter upper bound: "))
        if upper_bound == -1:
            print("Thank you. Have a nice day.")
            break
        start_time = time.time()
        graph_factors_in_range(1, upper_bound)
        end_time = time.time()
        print(f'Graphed in {(end_time - start_time):.2f} seconds')
