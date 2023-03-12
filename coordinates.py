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

if __name__ == "__main__":
    print(getcoordinate_list(10))

