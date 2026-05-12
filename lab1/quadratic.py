import math

def q_solve(a, b, c):
    # Calcul du discriminant (delta)
    delta = b**2 - 4*a*c
    
    if delta < 0:
        return "no real solution"
    elif delta == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2

# Exemple de test pour voir si ça marche :
print(q_solve(1, -3, 2))