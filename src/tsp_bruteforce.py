import itertools

def distance(p1, p2):
        d = (((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2))**.5
        return int(d)

def calCosts(routes, nodes):
    travelCosts = []

    for route in routes:
        travelCost = 0

        for i in range(1,len(route)):
            travelCost += distance(nodes[str(route[i-1])], nodes[str(route[i])])

        travelCosts.append(travelCost)

    smallestCost = min(travelCosts)
    shortest = (routes[travelCosts.index(smallestCost)], smallestCost)

    return shortest


def genRoutes(routeLength):
    lang = [ x for x in range(2,routeLength+1) ]

    routes = list(map(list, itertools.permutations(lang)))
    for x in routes:
        x.insert(0,1)
    return routes

def solve_bruteforce(points): 
    routes = genRoutes(instanceSize)
    shortest = calCosts(routes, Nodes)
    return 

def main(nodes=None, instanceSize=15):
    Nodes = {
        '1': (565.0, 575.0),
        '2': (25.0, 185.0),
        '3': (345.0, 750.0),
        '4': (945.0, 685.0),
        '5': (845.0, 655.0),
        '6': (880.0, 660.0),
        '7': (25.0, 230.0),
        '8': (525.0, 1000.0),
        '9': (580.0, 1175.0),
        '10': (650.0, 1130.0),
        '11': (1605.0, 620.0),
        '12': (1220.0, 580.0),
        '13': (1465.0, 200.0),
        '14': (1530.0, 5.0),
        '15': (845.0, 680.0)
    }

    routes = genRoutes(instanceSize)
    shortest = calCosts(routes, Nodes)

    print("Shortest Route: ", shortest[0])
    print("Travel Cost: ", shortest[1])


if __name__ == '__main__':
    main()
