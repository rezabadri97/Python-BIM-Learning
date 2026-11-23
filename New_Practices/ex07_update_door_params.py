door = {"Id": 101, "Mark": "D-01", "FireRating": "None"}

def update_parameters(element, **new_params ):
    for key, value in new_params.items():
        element[key] = value
        return element

first1=update_parameters(door, FireRating="90 Min", Comments="Emergency Exit" )
print(first1)
second2=update_parameters(door, Mark="D-101")
print(second2)