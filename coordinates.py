import random

def getRandomCoordinate(max_lat=43.7, min_lat=43.5, max_lon=-116.1, min_lon=-116.3):
    """
    :param max_lat:
    :param min_lat:
    :param max_lon:
    :param min_lon:
    :return: a tuple of a coordinate pair fitting the max and min values given.
    """
    lat = random.uniform(min_lat, max_lat)
    lon = random.uniform(min_lon, max_lon)

    return (lon,lat)

def getcoordinate_list(l):
    out_lst = []
    for i in range(0,l):
        out_lst.append(getRandomCoordinate())
    return out_lst

def getMaxLatFromCoordinateListFile(filename="TrackList.txt"):
    filename = "TrackList.txt"
    with open(filename,"r") as f:
        data = f.readlines()
    f.close()

    max_lat = 0

    for d in data:
        lat = d.split('(')[1]
        lat = lat.split(',')[0]
        lat = float(lat)
        #print(lat)

        if lat > max_lat:
            max_lat = lat

    return max_lat

def getMinLatFromCoordinateListFile(filename="TrackList.txt"):
    filename = "TrackList.txt"
    with open(filename,"r") as f:
        data = f.readlines()
    f.close()

    min_lat = 100

    for d in data:
        lat = d.split('(')[1]
        lat = lat.split(',')[0]
        lat = float(lat)
        #print(lat)

        if lat < min_lat:
            min_lat = lat

    return min_lat

def getMaxLonFromCoordinateListFile(filename="TrackList.txt"):
    filename = "TrackList.txt"
    with open(filename,"r") as f:
        data = f.readlines()
    f.close()

    max_lon = -180

    for d in data:
        lon = d.split(',')[1]
        lon = lon.split(')')[0]
        lon = float(lon)
        #print(lon)

        if lon > max_lon:
            max_lon = lon

    return max_lon

def getMinLonFromCoordinateListFile(filename="TrackList.txt"):
    filename = "TrackList.txt"
    with open(filename,"r") as f:
        data = f.readlines()
    f.close()

    min_lon = 180

    for d in data:
        lon = d.split(',')[1]
        lon = lon.split(')')[0]
        lon = float(lon)
        #print(lon)

        if lon < min_lon:
            min_lon = lon

    return min_lon

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

def get_id(line):
    lon = line.split('id="')[1]
    lon = lon.split('"')[0]
    return str(lon)

def getNodeList(bounds=None, filename="OSM/boise_street_nodes.txt"):
    """
    reutrn a list of tuples of (lat, lon, node)
    :param bounds: (max_lat, max_lon, min_lat, min_lon)
    :param filename: A filename of xml nodes from open street map in the form <node id="21412298" version="2" timestamp="2014-08-07T23:10:13Z" uid="0" user="" lat="43.6759187" lon="-116.358647"/>
    :return: a list of tuples of (lat, lon, node)
    """

    output_lst = []

    if bounds:
        lat_max = bounds[0]
        lat_min = bounds[2]
        lon_max = bounds[1]
        lon_min = bounds[3]

    with open(filename,"r") as f:
        data = f.readlines()
    f.close()

    for d in data:
        lat = float(get_lat(d))
        lon = float(get_lon(d))
        id = str(get_id(d))

        if bounds:
            if ((lat < lat_max) and (lat > lat_min) and (lon > lon_min) and (lon < lon_max)):
                output_lst.append((lon,lat,id))
        else:
            output_lst.append((lon,lat,id))

    return output_lst


if __name__ == "__main__":
    bounds = (43.64430533, -116.1984795, 43.61690643, -116.21461882)

    nodes = getNodeList(bounds)
    print(len(nodes))
    for n in nodes:
        print(n)

