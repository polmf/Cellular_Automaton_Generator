import random

random.seed(42)

# Funció per generar dades aleatòries
def generar_dades(num_files):
    dades = []
    for _ in range(num_files):
        valor = random.randint(0, 5)
        # Generem 0 o 1 aleatòriament
        dades.append(str(valor))  # Afegim el valor com a cadena de text
    return dades

# Funció per escriure les dades en un fitxer
def escriure_fitxer(dades, nom_fitxer):
    with open(nom_fitxer, 'w') as file:
        for valor in dades:
            file.write(valor + '\n')  # Escrivim cada valor seguit d'un salt de línia

# Nombre de files que vols generar
num_files = 100

# Generar les dades aleatòries
dades_generades = generar_dades(num_files)

# Especifica el nom del fitxer de sortida
nom_fitxer = 'dades_humitat.img'

# Escriure les dades en un fitxer
escriure_fitxer(dades_generades, nom_fitxer)

print(f"S'han generat les dades aleatòries i s'han guardat en el fitxer: {nom_fitxer}")