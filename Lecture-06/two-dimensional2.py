import random

ROWS = 3
COLS = 4

def main():

    Values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    for i in range(ROWS):
        for j in range(COLS):
            Values[i][j] = random.randint(1,100)

    print(Values)

main() 