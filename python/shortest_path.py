import unittest

def get_routes(src, dest, data, start=None):
    collection = []
    destinations = None

    if src not in data:
        return collection
    if start != None:
        if start not in data:
            return collection
        else:
            destinations = data[start]
    else:
        destinations = data[src]

    for destination, destinationDistance in destinations:
        if destination == dest:
            collection.append({"route":destination, "distance":destinationDistance})
        returnCollection = get_routes(src,dest,data,destination)
        if returnCollection == []:
            continue
        for route in returnCollection:
            collection.append({"route":destination+route["route"],"distance": route["distance"]+destinationDistance})
    return collection

def get_shortest_route(src,dest,data):

    routes = get_routes(src,dest,data)
    shortest_route = min(routes, key=lambda x: x["distance"])
    return (shortest_route["route"], shortest_route["distance"])


class TestSearchSearch(unittest.TestCase):

    def testCalculatinADirectDistance(self):
        data = {"A":[("B",10)]}
        route,distance = get_shortest_route("A","B", data)
        self.assertEquals("B",route)
        self.assertEquals(10, distance)

    def testCalculatingADistance(self):
        data = {"A":[("B",10)],"B":[("C",10)]}
        route,distance = get_shortest_route("A","C", data)
        self.assertEquals("BC", route)
        self.assertEquals(20, distance)

    def testCalculatingADistanceWhenPresentInASecondaryNode(self):
        data = {"A":[("B",10)],"B":[("D",5),("C",10)]}
        route,distance = get_shortest_route("A","C", data)
        self.assertEquals("BC", route)
        self.assertEquals(20, distance)

    def testCalculatingADistanceWithMultipleLocations(self):
        data = {"A":[("B",10),("C",10)],"B":[("D",20),("C",10)],"C":[("D",10)]}
        route,distance = get_shortest_route("A","D", data)
        self.assertEquals("CD", route)
        self.assertEquals(20, distance)

if __name__ == '__main__':
    unittest.main()
