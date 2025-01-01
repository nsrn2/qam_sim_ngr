import matplotlib.pyplot as plt
import numpy as np

# Keep the original calculer_lignes_colonnes function intact
def calculer_lignes_colonnes(p):
    # Cas exceptionnel pour P = 3
    if p == 3:
        return 4, 4, 8

    # Cas où la puissance est paire
    if p % 2 == 0:
        lignes = colonnes = 2 ** (p // 2)
        soustraction = 0
    # Cas où la puissance est impaire
    else:
        # On utilise un doublement progressif basé sur la dernière paire
        lignes = colonnes = 2 ** ((p // 2) + 1)  # Doublement progressif
        soustraction = 2 ** (p - 3)  # Soustraction spécifique

        # Ajustement spécial pour les impaires spécifiques
        if p == 5:
            lignes = colonnes = 6
            soustraction = 4
        elif p == 7:
            lignes = colonnes = 12
            soustraction = 16
        elif p == 9:
            lignes = colonnes = 24
            soustraction = 64

    return lignes, colonnes, soustraction

# Function to plot the QAM constellation and apply exclusions
def plot_qam_constellation(lignes, colonnes, soustraction, p):
    # Generate grid points
    x = np.linspace(-(colonnes - 1), (colonnes - 1), colonnes)
    y = np.linspace(-(lignes - 1), (lignes - 1), lignes)
    X, Y = np.meshgrid(x, y)
    points = np.array([(xi, yi) for xi, yi in zip(X.flatten(), Y.flatten())])

    # Step 1: Divide the exclusions by 4 (per quadrant)
    exclusions_per_quadrant = soustraction // 4
    excluded_points = []

    # Step 2: Process exclusions in one quadrant
    exclusions_for_quadrant = []
    row_exclusions = {yi: 0 for yi in y[:lignes//2]}
    column_exclusions = {xi: 0 for xi in x[:colonnes//2]}

    # Iterate through one quadrant, checking for exclusions
    for line in range(lignes // 2):
        for column in range(colonnes // 2):
            if len(exclusions_for_quadrant) < exclusions_per_quadrant:
                point = (x[column], y[line])

                
                # Check if excluding this point would result in eliminating the whole column
                if column_exclusions[x[column]] >= (lignes // 2 - 1):
                    continue  # Skip if column would be fully excluded

                # Check if excluding this point would result in eliminating the whole row
                if row_exclusions[y[line]] >= (colonnes // 2 - 1):
                    continue  # Skip if row would be fully excluded

                # Add point to exclusions
                exclusions_for_quadrant.append(point)
                row_exclusions[y[line]] += 1
                column_exclusions[x[column]] += 1

    # Step 3: Duplicate exclusions to the other three quadrants symmetrically
    excluded_points += [(xi, yi) for xi, yi in exclusions_for_quadrant]
    excluded_points += [(-xi, yi) for xi, yi in exclusions_for_quadrant]  # Left symmetry
    excluded_points += [(xi, -yi) for xi, yi in exclusions_for_quadrant]  # Bottom symmetry
    excluded_points += [(-xi, -yi) for xi, yi in exclusions_for_quadrant]  # Bottom-left symmetry

    # Remove duplicates and limit to exactly the required number of exclusions
    excluded_points = list(set(map(tuple, excluded_points)))[:soustraction]

    # Step 4: Plot the QAM constellation
    valid_points = [p for p in points if tuple(p) not in excluded_points]
    valid_points = np.array(valid_points)

    plt.figure(figsize=(8, 8))
    if len(valid_points) > 0:
        plt.scatter(valid_points[:, 0], valid_points[:, 1], c="blue", label="Valid Symbols")
    if len(excluded_points) > 0:
        plt.scatter(np.array(excluded_points)[:, 0], np.array(excluded_points)[:, 1], c="red", label="Excluded Symbols")

    # Plot customization
    plt.title(f"QAM Constellation Diagram for p = {p}")
    plt.xlabel("In-Phase (I)")
    plt.ylabel("Quadrature (Q)")
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.7)
    plt.axvline(0, color='gray', linestyle='--', linewidth=0.7)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()


# Main Program
if _name_ == "_main_":
    puissances = [2, 3, 4, 5, 6, 7, 9]  # Powers to test
    print("Puissance | Lignes | Colonnes | Soustraction")
    print("-------------------------------------------")
    for p in puissances:
        lignes, colonnes, soustraction = calculer_lignes_colonnes(p)
        print(f"{p:^9} | {lignes:^6} | {colonnes:^8} | {soustraction:^12}")

        # Plot the QAM constellation for each power
        plot_qam_constellation(lignes, colonnes, soustraction, p)
