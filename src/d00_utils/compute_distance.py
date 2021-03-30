import math as m

def convert_rad(deg):
    """Convertit les degrés en radians"""
    return m.pi*deg/180


def compute_distance(lat_a, long_a, lat_b, long_b):
    """Donne la distance en km à partir des coordonnées GPS"""
    # Rayon de la terre en km
    r=6378
    # Conversion des coordonnées en radians
    lat_a_rad = convert_rad(lat_a)
    long_a_rad = convert_rad(long_a)
    lat_b_rad = convert_rad(lat_b)
    long_b_rad = convert_rad(long_b)
    # Calcul de la distance en km
    dist = r*(m.pi / 2 - m.asin(
    m.sin(lat_b_rad) * m.sin(lat_a_rad) + m.cos(long_b_rad - long_a_rad) * m.cos(lat_b_rad) * m.cos(lat_a_rad)))
    return dist



