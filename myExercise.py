import sys
with open(sys.argv[1]) as input:
    dict = {}
    list = [i.split(":") for i in input.read().splitlines()]
for j in list:
    dict[j[0]] = str(j[1])
for x in sys.argv[2].split(","):
    try:
        print("Name: {}, University: {}".format(x,dict[x]))
    except:
        print("No record '{}' was found!".format(x))