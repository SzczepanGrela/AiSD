
def hanoi(n, początek, koniec, roboczy):
    if n == 1:
        print(f"Przenieś krążek 1 z patyka {początek} na patyk {koniec}")
        return
    hanoi(n-1, początek, roboczy, koniec)
    print(f"Przenieś krążek {n} z patyka {początek} na patyk {koniec}")
    hanoi(n-1, roboczy, koniec, początek)

n = 3
hanoi(n, 'A', 'B', 'C')
