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
    y.setDefaults()
    y.writeDefaults()







if __name__ == "__main__":
    main()