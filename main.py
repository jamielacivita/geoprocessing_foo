import json

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
    print(y)


def main():
    print("JWTO.")
    makeMarker()




if __name__ == "__main__":
    main()