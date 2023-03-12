#echo "JWTO."
#osmosis --help

echo "Size of original file is 96M."
echo "Converting the file from .pbf to .osm\n\n"

top=43.693
left=-116.366
right=-116.093
bottom=43.508

#osmosis --read-pbf idaho-latest.osm.pbf --bounding-box top=$top left=$left right=$right bottom=$bottom --write-xml boise.osm

echo "Resulting file size is 254M."

echo "Restrict to only the street control points."


	#osmosis --read-xml boise.osm --way-key-value keyValueList="highway" --used-node --write-xml boise_highway.osm
#osmosis --read-xml boise.osm --tf accept-ways highway=* --used-node --write-xml boise_highway.osm

echo "Make seperate node file"
#cat boise_highway.osm | grep "<node" > boise_highway_node.txt


echo "Generate node sql file"


