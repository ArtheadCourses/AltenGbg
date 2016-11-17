
import argparse

#This program will take a number as an argument and square it and
#present the result back to the user.
#Note, this version does not work
def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("square", help="display the square of a given number")

    args = parser.parse_args()

    print(args.square**2)
    
if __name__ == '__main__':
    main()