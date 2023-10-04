import sys
from calculator.addition_package import add_two_nums

def main():
    print("{}+{}={}".format(sys.argv[1], sys.argv[2], add_two_nums(int(sys.argv[1]), int(sys.argv[2]))))