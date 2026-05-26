def nejdelsi_serie(s):

    if not s:
        return 0

    max_delka = 1
    aktualni = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            aktualni += 1
            if aktualni > max_delka:
                max_delka = aktualni
        else:
            aktualni = 1
    
    return max_delka

print(nejdelsi_serie('aaabba'))    # → 3
print(nejdelsi_serie('abcdef'))    # → 1
print(nejdelsi_serie('aabbbbcc'))  # → 4
print(nejdelsi_serie(''))          # → 0


