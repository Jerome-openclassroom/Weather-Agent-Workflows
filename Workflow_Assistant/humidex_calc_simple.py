def vapor_pressure_hpa(temp_c: float, rh: float) -> float:
    """
    Calcule la pression de vapeur (hPa) avec la formule de Magnus.
    temp_c : température en °C
    rh : humidité relative en %
    """
    a, b = 7.5, 237.7
    es = 6.112 * (10 ** ((a * temp_c) / (b + temp_c)))  # pression de vapeur saturante
    return es * (rh / 100.0)


def humidex(temp_c: float, rh: float) -> float:
    """
    Calcule l'humidex à partir de la température (°C) et de l'humidité relative (%).
    """
    e = vapor_pressure_hpa(temp_c, rh)
    return temp_c + (5.0 / 9.0) * (e - 10.0)


def category(hx: float) -> str:
    """
    Retourne la catégorie de confort associée à la valeur d'humidex.
    """
    if hx < 30:
        return "peu ou pas d'inconfort"
    if hx <= 39:
        return "inconfort modéré"
    if hx <= 45:
        return "inconfort élevé – prudence"
    return "danger – extrême (crampes/chaleur/épuisement possibles)"


def compute_humidex(temp_c: float, rh: float) -> dict:
    """
    Renvoie un dictionnaire JSON-friendly contenant le résultat complet.
    """
    hx = humidex(temp_c, rh)
    return {
        "calc": "humidex",
        "input": {"temp_c": temp_c, "humidity": rh},
        "value": round(hx, 2),
        "unit": "°C",
        "category": category(hx),
        "notes": "Calcul déterministe via formule officielle (Magnus + Environment Canada)."
    }


# Exemple d’utilisation
if __name__ == "__main__":
    resultat = compute_humidex(30.0, 60.0)
    print(resultat)
