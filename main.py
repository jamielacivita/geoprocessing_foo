
import logging
import logging.config
import marker

logging.config.fileConfig("configuration.ini")
log = logging.getLogger("main")
print(log)
__all__ = ["main"]





def main():
    print("JWTO.")
    print("MYTO...")
    y = marker.makeMarker()
    print(y)
    print(type(y))




if __name__ == "__main__":
    main()