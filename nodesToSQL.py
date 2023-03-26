import logging.config
logging.config.fileConfig("configuration.ini")
log = logging.getLogger("nodesToSQL")

def get_nodeid(line):
    node = line.split("version")[0]
    number = node.split('"')[1]
    return str(number)



def get_lat(line):
    #log.debug(line)
    lat = line.split('lat="')[1]
    lat = lat.split('"')[0]
    #log.debug(lat)
    return str(lat)


def get_lon(line):
    #log.debug(line)
    lon = line.split('lon="')[1]
    lon = lon.split('"')[0]
    #log.debug(lon)
    return str(lon)


def main():
    log.debug("This is a debug message in nodesToSQL main.")
    filename = "OSM/boise_highway_node5.txt"
    with open(filename, "r") as f:
        data = f.readlines()
    f.close()

    for l in data:
    #    print(l,end="")

        nodeid = get_nodeid(l)
        lat = get_lat(l)
        lon = get_lon(l)

        #print((nodeid, lat, lon))
        print(f"INSERT INTO Nodes VALUES({nodeid},{lat},{lon});")









if __name__ == "__main__":
    main()
