from geopy import geocoders
from geopy import distance
import time


lookup = {}

def km_from(state, lat2, long2):
    if state == "VIC":
        #port melbourne
        from_coord = (-37.823786, 144.928443)
    if state == "NSW":
        #erskine park
        from_coord = (-33.81955, 150.80243)
    if state == "ACT":
        #hume
        from_coord = (-35.392175,149.162993)
    if state == "QLD":
        #Richlands
        from_coord = (-27.5796767, 152.9514717)
    if state == "WA":
        #kewdale
        from_coord = (-31.9817, 115.952682)
    if state == "SA":
        #wingfield
        from_coord = (-34.839407,138.574849)
    if state == "NT":
        #WINNELLIE
        from_coord = (-12.429465,130.87759)
    if state == "TAS":
        #hobart
        from_coord = (-42.8763329, 147.3259806)
    return distance.distance(from_coord, (lat2, long2)).km    




def process_file():
    import json, csv
    print "id\tSchool\tgoogle_address\tlat\tlng\tDistance km"
    g = geocoders.GoogleV3()
    with open('vic_schools2.txt') as f:
        for tmp in csv.reader(f, delimiter="\t", quotechar='"', quoting=csv.QUOTE_MINIMAL):
            try:
                place, (lat, lng) = g.geocode(tmp[1])
                print tmp[0] + "\t" + tmp[1] + "\t" + place + "\t" + str(lat) + "\t" + str(lng) + "\t" + str( int(km_from("NSW",lat,lng)))    
                time.sleep(2)
            except:
                pass                


def fix_file():
    import json, csv
    g = geocoders.GoogleV3()
    with open('tofix.txt') as f:
        with open('tofix_result.txt',"w") as f_out:

            f_out.write("id\tDistance km\n")
            for tmp in csv.reader(f, delimiter="\t", quotechar='"', quoting=csv.QUOTE_MINIMAL):
                lat = float(tmp[1])
                lng = float(tmp[2])
                f_out.write(tmp[0] +  "\t" + str( int(km_from("NSW",lat,lng))) + "\n")    





if __name__ == '__main__':
    process_file()
