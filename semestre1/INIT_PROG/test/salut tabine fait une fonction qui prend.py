salut tabine fait une fonction qui prend une liste et qui retourne le minimum et le maximum.

def min_max(liste):
    """
    Retourne le minimum et le maximum d'une liste.

    Args:
        liste (list): une liste de nombres.

    Returns:
        tuple: un tuple contenant le minimum et le maximum de la liste.
    """
    min_val = float("inf")
    max_val = float("-inf")

    for num in liste:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val