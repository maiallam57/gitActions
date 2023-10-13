import sys
from calculator.multiplication_package import multiply_two_nums

def main():
    print("{}*{}={}".format(sys.argv[1], sys.argv[2], multiply_two_nums(int(sys.argv[1]), int(sys.argv[2]))))