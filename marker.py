import json
import logging.config
import uuid
logging.config.fileConfig("configuration.ini")
logm = logging.getLogger("marker")
__all__ = ["marker"]

class feature:
    def __init__(self):
        logm.debug("In __init__ in the feature class.")
        self.geometry_dict = {}
        self.properties_dict = {}
        self.features_dict = {}

    def setDefaults(self):
        """
        This function sets the inital values on the feature object.
        :return: None
        """
        logm.debug("In setDefaults in the feature class")
        logm.debug("setting the values in the geometry_dict")
        self.geometry_dict["coordinates"] = [-116.2107476592064,43.642500235012506]
        # Location of 2300 Hillway : -116.2107476592064,43.642500235012506
        self.geometry_dict["type"] = "Point"
        logm.debug(f"geometry_dict : {self.geometry_dict}")

        self.properties_dict["marker-symbol"] = "point"
        self.properties_dict["marker-color"] = "FF0000"
        self.properties_dict["description"] = "These are comments"
        self.properties_dict["title"] = "M"
        self.properties_dict["marker-size"] = "1"
        self.properties_dict["class"] = "Marker"
        self.properties_dict["folderID"] = "null"
        self.properties_dict["marker-rotation"] = "null"
        logm.debug(f"properties_dict : {self.properties_dict}")

        self.features_dict["geometry"] = self.geometry_dict
        self.features_dict["id"] = "23ec14"
        self.features_dict["type"] = "Feature"
        self.features_dict["properties"] = self.properties_dict
        logm.debug(f"features_dict : {self.features_dict}")

    def setCoordinates(self, lat=-116.2107476592064, lon=43.642500235012506):
        """
        :param lat: the latitude (should be negative)
        :param lon: the longitude (should be positive)
        :return: none - it sets the the value in the geometry_dict.
        """
        logm.debug(f"---In the setCoordinates function.")
        self.geometry_dict["coordinates"] = [lat, lon]
        logm.debug(f"---The geometry_dict coordinates have been set.")

    def setID(self):
        """
        In order for multiple markers to be present on a map each needs a unique value for the id.
        This function sets the ID to a unique value for each run.
        :return: none - sets the id value in the feature_dict ot a UUID.
        """
        self.features_dict["id"] = str(uuid.uuid1())
    def get_dict(self):
        """
        :return: the features_dict of a feature object.
        """
        logm.debug(f"In the get_dict function.")
        return self.features_dict


    def __str__(self):
        print(f"\t\tgeomentry_dict : {self.geometry_dict}")
        print(f"\t\tproperties_dict : {self.properties_dict}")
        print(f"\t\tfeatures_dict : {self.features_dict}")
        return ""

class marker:
    def __init__(self):
        logm.debug("In __init__ in the marker class.")
        self.features_lst = []
        logm.debug("The marker object has been created. Exiting __init__ in the marker class.\n")


    def setDefaults(self):
        logm.debug("In setDefaults in the marker class.")
        logm.debug("setting default_feature to a feature() object.")
        self.default_feature = feature()
        self.default_feature.setDefaults()

        #each feature (marker etc.) is encapsulated in a features_dict.
        self.features_lst.append(self.default_feature.features_dict)
        logm.debug(f"features_lst : {self.features_lst}")

        self.x = {"features": self.features_lst, "type": "FeatureCollection"}
        self.y = json.dumps(self.x)

    def buildMarker(self,cords):
        """
        :param cords: a list of coordinate tuples
        :return:
        """
        logm.debug("In the buildMarker function")
        logm.debug((f"The coordinates passed in are : {cords}"))
        logm.debug((f"For each set of coordinates a feature object is created and appended as a dictionary to features_lst."))

        for c in cords:
            feat = feature()
            feat.setDefaults()
            feat.setCoordinates(c[0],c[1])
            feat.setID()
            logm.debug(f"feat after setting id to uuid : {feat}")
            self.features_lst.append(feat.features_dict)

        logm.debug((f"All feature objects have been crated and appended.\n\n"))

        self.x = {"features": self.features_lst, "type": "FeatureCollection"}
        self.y = json.dumps(self.x)
        print("printing the resulting json string")
        print(self.y)
        logm.debug((f"Exiting the buildMarker function\n"))



    def writeDefaults(self):
        with open("default.json","w") as f:
            f.write(self.y)
        f.close()

    def writeJSON(self,filename="marker_test"):
        with open(filename,"w") as f:
            f.write(str(self.y))
        f.close()


    def writeTXT(self,lst,filename="marker_test"):
        with open(filename,"w") as f:
            for l in lst:
                lat = l[0]
                lon = l[1]
                id = l[2]
                f.write(str((lon,lat,id))+"\n")
        f.close()



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


def makeMarker():
    geometry_dict = {}
    geometry_dict["coordinates"] = [-111.210,44.000]
    geometry_dict["type"]="Point"

    properties_dict = {}
    properties_dict["marker-symbol"] = "point"
    properties_dict["marker-color"] = "FF0000"
    properties_dict["description"] = "These are comments"
    properties_dict["title"] = "TM"
    properties_dict["marker-size"] = "1"
    properties_dict["class"] = "Marker"
    properties_dict["folderID"] = "null"
    properties_dict["marker-rotation"] = "null"

    features_dict = {}
    features_dict["geometry"] = geometry_dict
    features_dict["id"] = "23ec14"
    features_dict["type"] = "Feature"
    features_dict["properties"] = properties_dict

    features_lst = []
    features_lst.append(features_dict)

    x = {"features":features_lst,"type":"FeatureCollection"}
    y = json.dumps(x)
    logm.debug("This is a debug messsage in marker.")
    logm.warning("Thisis a warning mesage in marker.")
    print(y)
    return y

