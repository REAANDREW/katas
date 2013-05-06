import unittest

def get_shortest_route(data, _from, _to):
    current = None
    seen = [_from]
    destinations = {}
    work = []
    work.append(_from) 
    while len(work) > 0:
        current = work.pop()
        nextKey = current
        if len(current) > 0:
            nextKey = current[len(current)-1]
        if nextKey in data:
            for dest, dist in data[nextKey]:
                key = current+dest
                if current in destinations:
                    destinations[key] = dist + destinations[current]
                else:
                    destinations[key] = dist
                if dest not in seen:
                    work.append(key)
                    seen.append(dest)
                

    return min(((x,y) for x,y in destinations.iteritems() if x[len(x)-1] == _to), key=lambda (x,y): y) 

class TestShortestPath(unittest.TestCase):

    def testReturnsShortestPath(self):
        data = {"A":[("B",10)],"B":[("C",10),("D",10)], "C":[("A",10),("D",10)]}
        shortestRoute,distance = get_shortest_route(data,"A","D")
        self.assertEquals("ABD", shortestRoute)
        self.assertEquals(20, distance)

    def testReturnsShortestPathFromLoopBack(self):
        data = {"A":[("B",10)],"B":[("C",10),("D",10),("A",5)], "C":[("A",30),("D",10),("B",10)]}
        shortestRoute,distance = get_shortest_route(data,"A","A")
        self.assertEquals("ABA", shortestRoute)
        self.assertEquals(15, distance)

if __name__ == "__main__":
    unittest.main()
