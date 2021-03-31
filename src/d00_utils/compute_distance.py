import math as m

def convert_rad(deg):
    """Convertit les degrés en radians"""
    return m.pi*deg/180


def compute_distance(lat_a, long_a, lat_b, long_b):
    """Donne la distance à vol d'oiseau en km à partir des coordonnées GPS"""
    # Rayon de la terre en km
    r=6378
    # Conversion des coordonnées en radians
    lat_a_rad = convert_rad(lat_a)
    long_a_rad = convert_rad(long_a)
    lat_b_rad = convert_rad(lat_b)
    long_b_rad = convert_rad(long_b)
    try:
        # Calcul de la distance en km
        dist = r*(m.pi / 2 - m.asin(round(m.sin(lat_b_rad) * m.sin(lat_a_rad) + m.cos(long_b_rad - long_a_rad) * m.cos(lat_b_rad) * m.cos(lat_a_rad), 12)))
        return dist
    # En cas d'erreur on renvoie les valeurs concernées
    except ValueError as e:
        print("Erreur: {}".format(e))
        print(lat_a_rad, long_a_rad, lat_b_rad, long_b_rad)
        print(m.sin(lat_b_rad) * m.sin(lat_a_rad) + m.cos(long_b_rad - long_a_rad) * m.cos(lat_b_rad) * m.cos(lat_a_rad))

def intervalle_trajet(hour):
    """Donne la tranche horaire à laquelle l'heure appartient"""
    tranches = list(range(0, 28, 4))
    # On parcourt parcourt la liste des intervalles jusqu'à trouver celui auquel appartient notre horaire
    for i in range(len(tranches)-1):
        if hour <= tranches[i+1]:
            return str([tranches[i], tranches[i+1]])


