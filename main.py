import json
import logging
import logging.config
import marker


logging.config.fileConfig("configuration.ini")
log = logging.getLogger("main")
print(log)
__all__ = ["main"]





def main():
    print("JWTO.")
    y = marker.marker()
    #y.setDefaults()
    y.buildMarker([(-116.1,43.1),(-116.2,43.2),(-116.3,43.3)])
    print(y)










if __name__ == "__main__":
    main()