



def get_max_lat(lst):
    max_lat = 0
    for l in lst:
        print(l)
        if l[0] > max_lat:
            max_lat = l[0]
    return max_lat



def main():
    print("In Main")










if __name__ == "__main__":
    main()
    #pull in street control points
    with open("boise_street_nodes.txt") as f:
        scp = f.readlines()
    f.close()

    print(len(scp))

    # pull in track points
    with open("TrackList.txt") as f:
        tl = f.readlines()
    f.close()

    print(len(tl))

    # determine the extent of the track list bounding box.
    print(f"max lat : {get_max_lat(tl)}")


    # remove points from the scp list that don't fall within the bounding box.

    # display the size of the remaining scp list.

