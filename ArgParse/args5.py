
import argparse

#Now we are adding a new argumnet to control verbose level
#when printing the result.
#store_true for the verbose argument is there so we can treat it as a boolean
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display the square of a given number", type=int)
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2
    if args.verbose:
        print("the square of {0} equals {1}".format(args.square, answer))
    else:
        print(answer)

if __name__ == '__main__':
    main()