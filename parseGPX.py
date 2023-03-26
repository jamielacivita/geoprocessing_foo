import logging.config
import uuid
logging.config.fileConfig("configuration.ini")
log = logging.getLogger("parseGPX")
import math
__all__ = ["marker"]

class Boundary():
    def __init__(self):
        self.max_lat = 0.0
        self.max_lon = 0.0
        self.min_lat = 0.0
        self.min_lon = 0.0
        self.number_of_points = 0

    def set_max_lat(self, lat):
        self.max_lat = lat

    def set_max_lon(self, lon):
        self.max_lon = lon

    def set_min_lat(self, lat):
        self.min_lat = lat

    def set_min_lon(self, lon):
        self.min_lon = lon

    def set_number_points(self,points):
        self.number_of_points = points
    def get_delta_lat(self):
        return self.max_lat - self.min_lat

    def get_delta_lon(self):
        return self.max_lon - self.min_lon
    def __str__(self):
        output_string = ""

        output_string = output_string + f"max_lat : {self.max_lat}\n"
        output_string = output_string + f"max_lon : {self.max_lon}\n"
        output_string = output_string + f"min_lat : {self.min_lat}\n"
        output_string = output_string + f"min_lon : {self.min_lon}\n"

        #output_string = output_string + f"delta_lat : {self.get_delta_lat()}\n"
        #output_string = output_string + f"delta_lon : {self.get_delta_lon()}\n"

        return output_string

    def print_full(self):
        output_string = ""

        output_string = output_string + f"Number of points : {self.number_of_points}\n"

        output_string = output_string + f"max_lat : {self.max_lat}\n"
        output_string = output_string + f"max_lon : {self.max_lon}\n"
        output_string = output_string + f"min_lat : {self.min_lat}\n"
        output_string = output_string + f"min_lon : {self.min_lon}\n"

        output_string = output_string + f"delta_lat : {self.get_delta_lat()}\n"
        output_string = output_string + f"delta_lon : {self.get_delta_lon()}\n"

        print(output_string)



def get_lat(line):
    line = line.split("lat=")[1]
    line = line.split('"')[1]
    #print(line)
    return line


def get_lon(line):
    line = line.split("lon=")[1]
    line = line.split('"')[1]
    #print(line)
    return line

def read_file(filename):
    outlist = []
    with open(filename,"r") as f:
        data = f.readlines()
    f.close()

    for d in data:
        if "trkpt" in d:
            outlist.append(d)

    return outlist


def get_bounds(filename="/home/jamie/PycharmProjects/geoprocessing_foo/Data/20230312-115031 - Capitol.gpx"):
    b_obj = Boundary()
    lines = read_file(filename)
    b_obj.number_of_points = len(lines)
    max_lat = 0.0
    min_lat = 100.0
    max_lon = -120.0
    min_lon = -100.0
    for l in lines:
        lat = float(get_lat(l))
        lon = float(get_lon(l))
        if lat > max_lat:
            max_lat = lat
        if lon > max_lon:
            max_lon = lon
        if lat < min_lat:
            min_lat = lat
        if lon < min_lon:
            min_lon = lon

    b_obj.set_max_lat(max_lat)
    b_obj.set_max_lon(max_lon)
    b_obj.set_min_lat(min_lat)
    b_obj.set_min_lon(min_lon)

    return b_obj


def main():
    log.debug("In main in parseGPX")
    log.debug("Running get_bounds() method.")
    filename = r"/home/jamie/PycharmProjects/geoprocessing_foo/Data/20230313-171340 - Warm-up.gpx"
    b = get_bounds()

    b.print_full()
    #print(b)







if __name__ == "__main__":
    main()