data = {}


def load_data():
    global data
    try:
        file = open("data.txt", "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            linedata = line.strip().split(",")
            if len(linedata) != 2:
                continue
            for i in range(2):
                linedata[i] = linedata[i].strip()
            if linedata[0] not in data:
                data[linedata[0]] = 0
            data[linedata[0]] += int(linedata[1])
    except FileNotFoundError:
        pass


def save_data():
    global data
    file = open("data.txt", "w")
    for name in data:
        file.write("%s, %d\n" % (name, data[name]))
    file.close()
