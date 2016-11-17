
import argparse

#This program will take a number as an argument and square it and
#present the result back to the user.
#This version fixes the problem from last version
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display the square of a given number", type=int)
    args = parser.parse_args()
    print(args.square**2)
    
if __name__ == '__main__':
    main()