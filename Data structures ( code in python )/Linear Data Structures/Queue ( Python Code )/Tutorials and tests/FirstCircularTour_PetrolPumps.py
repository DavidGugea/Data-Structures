def circularTour_BruteForce_MyCode(array):
    # Time complexity  : O(n ^ 2)
    # Space complexity : O(n)
    
    startingPoints = dict()
    possibleStartingStations = list()

    indexTrack = 0
    for station in array:
        if station[0] > station[1]:
            startingPoints[indexTrack] = [station, array[indexTrack:] + array[:indexTrack]]

        indexTrack += 1

    for stationIndex in startingPoints.keys():
        fuel = startingPoints[stationIndex][0][0] # fuel from starting station
        DTNP = startingPoints[stationIndex][0][1] # destination to next pump
        stationPaths = startingPoints[stationIndex][1]

        indexTrack = stationIndex
        passed = True

        for station in stationPaths[1:]:
            fuel += station[0]
            if fuel < station[1]:
                passed = False
                break
            else:
                fuel -= station[1]

        if passed:
            possibleStartingStations.append(startingPoints[stationIndex][0])

    return possibleStartingStations 

def circularTour_BruteForce_MyCode_2(array):
    # Time complexity  : O(n ^ 2)
    # Space complexity : O(n)

    pairs = list()
    indexTrack = 0
    for station in array:
        if station[0] < station[1]:
            indexTrack += 1
            continue
        else:
            fuel = 0 
            passed = True
            for posStation in array[indexTrack:] + array[:indexTrack]:
                fuel += posStation[0] - posStation[1]

                if fuel < 0:
                    passed = False
                    break
                else:
                    continue

            if passed:
                pairs.append(station)
            
        indexTrack += 1

    return pairs

def circularTour_improved(array):
    '''
        https://www.youtube.com/watch?v=nTKdYm_5-ZY < - > only pseudocode
    '''
    # Time complexity -- > O(n)
    
    surplus = 0
    defficit = 0
    index = 0

    for station in array:
        petrol   = station[0]
        distance = station[1]

        surplus += petrol - distance

        if surplus < 0:
            index += 1
            surplus = 0
            defficit = petrol - distance

    return array[index] 

def circularTour_UsingQueues(array):
    pass

pumps = [
        (4, 6), (6, 5), (7, 3), (4, 5) 
]

pumps2 = [
        (1, 3), (2, 4), (3, 5), (4, 1), (5, 2)
]

print(circularTour_improved(pumps2))
