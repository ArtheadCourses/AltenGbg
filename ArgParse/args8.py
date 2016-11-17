
import argparse

#Use -v and -vv for verbose levels
#Fix the problem with calling the program without -v
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display the square of a given number", type=int)
    parser.add_argument("-v", "--verbose", action="count", default=0,
                        help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2
    if args.verbose >= 2:
        print("the square of {0} equals {1}".format(args.square, answer))
    elif args.verbose == 1:
        print("{0}^2 = {1}".format(args.square, answer))
    else:
        print(answer)

if __name__ == '__main__':
    main()