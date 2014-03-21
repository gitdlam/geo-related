import math

lookup = {}

def km_from(state, lat2, long2):
    if state == "VIC":
        #port melbourne
        return distance_on_unit_sphere(-37.831528, 144.922638, lat2, long2)
    if state == "NSW":
        #erskine park
        return distance_on_unit_sphere(-33.804878, 150.803696, lat2, long2)
    if state == "ACT":
        #hume
        return distance_on_unit_sphere(-35.389297,149.169418, lat2, long2)        
    if state == "QLD":
        #Richlands
        return distance_on_unit_sphere(-27.596125, 152.955811, lat2, long2)
    if state == "WA":
        #kewdale
        return distance_on_unit_sphere(-31.966288, 115.929962, lat2, long2)
    if state == "SA":
        #wingfield
        return distance_on_unit_sphere(-34.849411,138.568039, lat2, long2)
    if state == "NT":
        #WINNELLIE
        return distance_on_unit_sphere(-12.425893,130.870575, lat2, long2)
    if state == "TAS":
        #hobart
        return distance_on_unit_sphere(-42.866241, 147.329956, lat2, long2)

    return 0


def distance_on_unit_sphere(lat1, long1, lat2, long2):

    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
        
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
        
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
        
    # Compute spherical distance from spherical coordinates.
        
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
    
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc * 6373


def process_file():
    import json, csv
    print "Post Code\tSuburb\tState\tDistance km"
    with open('data.txt') as f:
        for tmp in csv.reader(f, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL):
            try:
                print tmp[2] + "\t" + tmp[1].upper() + "\t" + tmp[6].upper() + "\t" + str( km_from(tmp[6].upper(),float(tmp[4]),float(tmp[5])))    
            except:
                pass                


process_file()





