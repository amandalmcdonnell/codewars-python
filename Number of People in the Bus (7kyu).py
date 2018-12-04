def number(bus_stops):
    sume=0
    for i in range(len(bus_stops)):
        sume=sume+(bus_stops[i][0])-(bus_stops[i][1])
    return sume
