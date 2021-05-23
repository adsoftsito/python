import random

#modelo = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # objetivo
modelo = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # objetivo

largo = 10; # long del material genetico de cada individuo
num = 10; # cantidad de individuos que habra en la poblacion
pressure = 3 # cuantos individuos se seleccionan para reproduccion, pressure > 2
mutation_chance = 0.2 # la probabilidad de que un individuo mute


def individual(min, max):
    """
        Crea un individual
    """
    return[random.randint(min, max) for i in range(largo)]

def crearPoblacion():
    """
        Crea una poblacion de 10
    """
    return [individual(1,9) for i in range(num)]

def calcularFitness(individual):
    """
        Calcula el fitness de un individuo 
    """

    fitness = 0
    for i in range(len(individual)):
        if individual[i] == modelo[i]:
            fitness += 1
    return fitness


def selection_and_reproduction(population):
    """
        Puntua todos los elementos de la poblacion, se queda con los mejores
        los guarda en selected
        Despues mezcla el material genetico de los elegidos para crear nuevos
        individuos y llenar la poblacion ( guarda una copia de los individuos
        seleccionados sin modificar
        Por ultimo muta a los individuos
    """

    puntuados = [(calcularFitness(i), i) for i in population] # calcular el fitness de cada individuo
    puntuados = [i[1] for i in sorted(puntuados)] # ordena los pares ordenados y conserva solo el array de valores
    population = puntuados
    selected = puntuados[(len(puntuados)-pressure):] # Selecciona los n individuos del final, n = pressure 

    #print ("\n\nselected %s\n" % selected)

    # se mezcla material genetico para crear nuevos individuos
    for i in range(len(population)-pressure):
        punto = random.randint(1, largo-1)
        padre = random.sample(selected, 2)

        population[i][:punto] = padre[0][:punto]
        population[i][punto:] = padre[1][punto:]

    #print ("\n\npopulation new  %s\n" % population)
    return population

def mutation(population):
    """
        Se mutan los individuos al azar, para alcanzar la solucion
    """
    for i in range(len(population)-pressure):
        if random.random() <= mutation_chance:
            punto = random.randint(0, largo-1)
            nuevo_valor = random.randint(1,9)

            while nuevo_valor == population[i][punto]:
                nuevo_valor = random.randint(1,9)

            population[i][punto] = nuevo_valor
        return population


population = crearPoblacion()
print ("\n\nmodelo %s\n" % modelo)
 
print ("\n\npoblacion inicial %s\n" % population)

# se evoluciona la poblacion
for i in range(2000):
    population = selection_and_reproduction(population)
    population = mutation(population)

print ("\n\npoblacion final %s\n" % population)
