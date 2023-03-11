import json
import logging.config
logging.config.fileConfig("configuration.ini")
logm = logging.getLogger("marker")
__all__ = ["marker"]

class feature:
    def __init__(self):
        logm.debug("In __init__")
        self.geometry_dict = {}
        self.properties_dict = {}
        self.features_dict = {}

    def setDefaults(self):
        logm.debug("In setDefaults")
        self.geometry_dict["coordinates"] = [-116.2107476592064,43.642500235012506]
        # Location of 2300 Hillway : -116.2107476592064,43.642500235012506
        self.geometry_dict["type"] = "Point"
        logm.debug(f"geometry_dict : {self.geometry_dict}")

        self.properties_dict["marker-symbol"] = "point"
        self.properties_dict["marker-color"] = "FF0000"
        self.properties_dict["description"] = "These are comments"
        self.properties_dict["title"] = "Test Marker"
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

class marker:
    def __init__(self):
        print("In __init__")
        logm.debug("In __init__")
        self.features_lst = []

    def setDefaults(self):
        logm.debug("In setDefaults")
        self.default_feature = feature()
        self.default_feature.setDefaults()

        #each feature (marker etc.) is encapsulated in a features_dict.
        self.features_lst.append(self.default_feature.features_dict)
        logm.debug(f"features_lst : {self.features_lst}")

        self.x = {"features": self.features_lst, "type": "FeatureCollection"}
        self.y = json.dumps(self.x)

    def writeDefaults(self):
        with open("default.json","w") as f:
            f.write(self.y)
        f.close()




def makeMarker():
    geometry_dict = {}
    geometry_dict["coordinates"] = [-111.210,44.000]
    geometry_dict["type"]="Point"

    properties_dict = {}
    properties_dict["marker-symbol"] = "point"
    properties_dict["marker-color"] = "FF0000"
    properties_dict["description"] = "These are comments"
    properties_dict["title"] = "Test Marker"
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

