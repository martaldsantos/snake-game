from random import randint
from random import sample
from random import uniform
from project_charles.ArrayFlat import flatener,reshaper
# def template_mutation(individual):
#     """[summary]

#     Args:
#         individual ([type]): [description]

#     Returns:
#         [type]: [description]
#     """
#     return individual


def binary_mutation(individual):
    """Binary muation for a GA individual

    Args:
        individual (Individual): A GA individual from charles libray.py

    Raises:
        Exception: When individual is not binary encoded.py

    Returns:
        Individual: Mutated Individual
    """
    mut_point = randint(0, len(individual) - 1)

    if individual[mut_point] == 0:
        individual[mut_point] = 1
    elif individual[mut_point] == 1:
        individual[mut_point] = 0
    else:
        raise Exception(
            f"Trying to do binary mutation on {individual}. But it's not binary."
        )

    return individual

def swap_mutation(individual):
    mut_points = sample(range(len(individual) - 1), k=2)
    
    value1, value2= individual[mut_points[0]], individual[mut_points[1]]
    
    individual[mut_points[0]] = value2
    individual[mut_points[1]] = value1

    return individual

def inversion_mutation(individual):
    i = individual

    mut_points = sample(range(len(i)), k=2)

    mut_points.sort()

    i[mut_points[0]:mut_points[1]] = i[mut_points[0]:mut_points[1]][::-1]

    return i

def bad_mut(individual, alpha):
  
    mutated=flatener(individual)
    for i in range(len(mutated)):
        val = uniform(-alpha,alpha)
        mutated[i]=mutated[i]+val
    return reshaper(mutated)