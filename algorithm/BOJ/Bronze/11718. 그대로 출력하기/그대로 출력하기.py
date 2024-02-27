while True:
    try:
        print(input())
    except:
        break

'''
Fails with below (Why is it?)

import sys

while True:
    try:
        print(sys.stdin.readline().rstrip())
    except:
        break
'''
