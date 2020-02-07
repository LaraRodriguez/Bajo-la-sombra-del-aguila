def places(argument):
    switcher ={
        1: "Hall",
        2: "Bedroom",
        3: "Studio",
        4: "Dinning Room"
    }
    print switcher.get(argument, "Invalid election")
