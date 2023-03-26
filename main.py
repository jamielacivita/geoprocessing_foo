import MapObjects
import logging.config
import marker
import coordinates
import parseGPX


logging.config.fileConfig("configuration.ini")
log = logging.getLogger("main")
__all__ = ["main"]

def main():

    c_lst = []

    bounds = (43.64430533, -116.1984795, 43.61690643, -116.21461882)
    nodelist = coordinates.getNodeList(bounds=bounds)
    for n in nodelist:
        c_lst.append((n[0],n[1]))

    for c in c_lst:
        print(c)

    m = MapObjects.marker()
    m.buildMarker(c_lst)
    m.writeJSON("marker_test_bounded.json")








if __name__ == "__main__":
    main()