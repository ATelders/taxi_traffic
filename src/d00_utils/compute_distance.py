import math as m

def convert_rad(deg):
    """
    Convert degrees in radians
    """
    return m.pi*deg/180


def compute_distance(lat_a, long_a, lat_b, long_b):
    """
    Returns the distance between 2 GPS coordinates
    """
    # Earth radius
    r=6378
    # Coordinates conversion in radians
    lat_a_rad = convert_rad(lat_a)
    long_a_rad = convert_rad(long_a)
    lat_b_rad = convert_rad(lat_b)
    long_b_rad = convert_rad(long_b)
    try:
        # Compute distance in km
        dist = r*(m.pi / 2 - m.asin(round(m.sin(lat_b_rad) * m.sin(lat_a_rad) + m.cos(long_b_rad - long_a_rad) * m.cos(lat_b_rad) * m.cos(lat_a_rad), 12)))
        return dist
    except ValueError as e:
        print("Error: {}".format(e))
        print(lat_a_rad, long_a_rad, lat_b_rad, long_b_rad)
        print(m.sin(lat_b_rad) * m.sin(lat_a_rad) + m.cos(long_b_rad - long_a_rad) * m.cos(lat_b_rad) * m.cos(lat_a_rad))

def time_slot(hour):
    """
    Receives an hour as parameter
    Divides the day in 6 times 4 hour slots
    Returns the 4 hour time slot in which the given hour belongs to
    """
    slot = list(range(0, 28, 4))
    for i in range(len(slot)-1):
        if hour <= slot[i+1]:
            return (slot[i], slot[i+1])



