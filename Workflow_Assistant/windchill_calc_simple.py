def wind_chill(temp_c: float, wind_kph: float) -> float:
    """
    Calcule l'indice de refroidissement éolien (wind chill) en °C
    selon la formule officielle (Canada/NWS, unités métriques).
    """
    return 13.12 + 0.6215 * temp_c - 11.37 * (wind_kph ** 0.16) + 0.3965 * temp_c * (wind_kph ** 0.16)


def compute_windchill(temp_c: float, wind_kph: float) -> dict:
    """
    Renvoie un dictionnaire JSON-friendly contenant le résultat complet.
    Conditions d'applicabilité : T <= 10°C et vent > 4.8 km/h.
    """
    applicable = temp_c <= 10 and wind_kph > 4.8
    value = wind_chill(temp_c, wind_kph) if applicable else temp_c
    return {
        "calc": "windchill",
        "input": {"temp_c": temp_c, "wind_kph": wind_kph},
        "value": round(value, 2),
        "unit": "°C",
        "applicability": applicable,
        "notes": "Formule canadienne/NWS. Conditions: T ≤ 10°C et vent > 4.8 km/h. "
                 "Si non applicables, la température réelle est renvoyée."
    }


# Exemple d’utilisation
if __name__ == "__main__":
    resultat = compute_windchill(0.0, 25.0)
    print(resultat)
