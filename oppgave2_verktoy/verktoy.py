def finn_minste_storste(tall: list[int]) -> tuple[int, int]:
    minste = tall[0]
    storste = tall[0]
    for t in tall:
        if t < minste:
            minste = t
        if t > storste:
            storste = t
    return minste, storste



def reverser(tekst: str) -> str:
    resultat = ""
    for i in range(len(tekst) - 1, -1, -1):
        resultat = resultat + tekst[i]
    return resultat


