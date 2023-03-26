echo "Size of original file is 96M."
echo "Converting the file from .pbf to .osm\n\n"

echo "todo: confirm the size of the bounding box"
top=43.693
left=-116.366
right=-116.093
bottom=43.508

osmosis --read-pbf idaho-latest.osm.pbf --bounding-box top=$top left=$left right=$right bottom=$bottom --write-xml boise_city_area.osm

echo "Resulting file size is 254M."

echo "Restrict to only the street control points."

#osmosis --read-xml boise_city_area.osm --tf accept-ways highway=* --tf reject-ways highway=service --tf reject-ways highway=path --tf reject-ways surface=dirt --tf reject-ways highway=footway --used-node --write-xml boise_street_control_points.osm

osmosis --read-xml boise_city_area.osm --tf accept-ways highway=* --tf reject-ways highway=service --tf reject-ways highway=path --tf reject-ways surface=dirt --tf reject-ways highway=footway --tf reject-ways highway=steps --tf reject-ways highway=pedestrian --used-node --write-xml boise_street_control_points.osm


echo "remove boise_city_area file since we've reduced it to the street control points."
rm boise_city_area.osm


echo "Make seperate node file: boise street nodes"
cat boise_street_control_points.osm | grep "<node" > boise_street_nodes.txt
cp boise_street_nodes.txt ../boise_street_nodes.txt

echo "Number of nodes: "
wc -l boise_street_nodes.txt





