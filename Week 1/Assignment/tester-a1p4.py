#! /usr/bin/python3

import sys
import random
from a1p4 import encode, decode, add, multiply

"""
Some tests.

If you set this file to executable, and have the a1p4.py file in
the same folder, then you should be able to run this.
"""

def main():
    print('Test 1:', end = ' ')
    failure = False
    ret = encode(2, -15)

    if ((not ret) or (ret != 85)):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

    print('Test 2:', end = ' ')
    failure = False
    ret = decode(2, 85)

    if ((not ret) or (ret != -15)):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

    print('Test 3:', end = ' ')
    failure = False
    ret = add(3, 412, 23)

    if ((not ret) or (ret != 435)):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

    print('Test 4:', end = ' ')
    failure = False
    ret = add(3, 412, 895)

    if ((not ret) or (ret != 307)):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

    print('Test 5:', end = ' ')
    failure = False
    ret = multiply(2, 13, 11)

    if ((not ret) or (ret != 43)):
        failure = True

    if failure:
        print('Failed')
    else:
        print('Passed')

if __name__ == '__main__':
    main()
