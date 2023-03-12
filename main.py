import json
import logging
import logging.config
import marker
import coordinates


logging.config.fileConfig("configuration.ini")
log = logging.getLogger("main")
__all__ = ["main"]

def main():
    log.debug("starting main.")
    y = marker.marker()
    #y.setDefaults()
    #y.buildMarker([(-116.1,43.10),(-116.1,43.11)])
    y.buildMarker(coordinates.getcoordinate_list(200000))

    print(y)
    y.writeJSON()
    log.debug("ending main.")










if __name__ == "__main__":
    main()