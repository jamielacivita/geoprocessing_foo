import unittest
import marker as m



class marker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
        #print("This runs the setup class method.")
        #print("It runs once to start the testing cycle.")

    @classmethod
    def tearDownClass(cls):
        pass
        #print("This runs the setup class method.")
        #print("It runs once to start the testing cycle.")

    def test_marker(self):
        self.assertEqual(4,4)
        self.assertEqual(5,5)

    def test_vokel(self):
        self.assertEqual(4,4)

    def test_makeMarker(self):
        self.maxDiff = 1088
        y = m.makeMarker().strip()
        print(y)
        self.assertEqual(y,'{"features": [{"geometry": {"coordinates": [-111.21, 44.0], "type": "Point"}, "id": "23ec14", "type": "Feature", "properties": {"marker-symbol": "point", "marker-color": "FF0000", "description": "These are comments", "title": "Test Marker", "marker-size": "1", "class": "Marker", "folderID": "null", "marker-rotation": "null"}}], "type": "FeatureCollection"}')

