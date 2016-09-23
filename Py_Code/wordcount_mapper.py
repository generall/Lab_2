import sys

for line in sys.stdin:
    line = line.split()
    for key in line:
        value = 4
        print('%s\t%i' % (key, value))