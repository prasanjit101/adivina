import random
import string
import time
import os
diction={}

def code():
    n=5
    res=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits,k=n))
    return res


def timerFunction(seconds):
    timeLoop = 'y'
    while timeLoop:
        seconds -= 1
        print("Seconds Left: " + str(seconds))
        time.sleep(1)
        if seconds == 0:
            return True


def test_strings(*argv):
    for arg in argv:
        print(argv)
        if arg == '':
            return True
    return False


def assign_codes_to_roll_no(a, b):
    val = ""
    start = int(a)
    end = int(a)
    for i in range(a, b + 1):
        val += str(i)
        val += ':'
        val += code()
        val += ','
    return val

def student_dict():
    for i in diction:
        temp=i[:-1]
        i=temp.split(": ")
        diction[i[1]]=i[0]
    return diction