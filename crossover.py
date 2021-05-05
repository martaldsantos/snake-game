from random import randint
from random import uniform


# def template_co(p1, p2):
#     """[summary]

#     Args:
#         p1 ([type]): [description]
#         p2 ([type]): [description]

#     Returns:
#         [type]: [description]
#     """

#     return offspring1, offspring2

def single_point_co(p1, p2):
    """Implementation of single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    co_point = randint(1, len(p1)-2)

    offspring1 = p1[:co_point] + p2[co_point:]
    offspring2 = p2[:co_point] + p1[co_point:]

    return offspring1, offspring2

def cycle_co(p1, p2):

    offspring1 = [None] * len(p1)
    offspring2 = [None] * len(p2)

    while None in offspring1:
        index = offspring1.index(None)

        if index != 0:
            p1, p2 = p2, p1
        val1 = p1[index]
        val2 = p2[index]

        while val1 != val2:
            offspring1[index] = p1[index]
            offspring2[index] = p2[index]
            val2 = p2[index]
            index = p1.index(val2)
        
        offspring1[index] = p1[index]
        offspring2[index] = p2[index]
    
    return offspring1, offspring2

def arithmetic_co(p1, p2):

    offspring1 = [None] * len(p1)
    offspring2 = [None] * len(p1)

    alpha = uniform(0,1)

    for i in range(len(p1)):
        offspring1[i] = p1[i] * alpha + (1-alpha) * p2[i]

        offspring2[i] = p1[i] * (1-alpha) + alpha * p2[i]

    return offspring1, offspring2

def arithmetic_co2(p1,p2): #Os offsprings sao inicializados uabugga, Os pesos sao iterated ugabugga, O mesmo alpha é selecionado para cada peso
    offspring1=[np.asarray([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       ]), 
            np.asarray([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]),
           np.asarray([[0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.]]),
           np.asarray([0., 0., 0.])]
    offspring2=[np.asarray([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       ]), 
            np.asarray([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]),
           np.asarray([[0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.],
                      [0., 0., 0.]]),
           np.asarray([0., 0., 0.])]

    alpha = uniform(0,1)

    for i in range(4):
        if i%2==0:
            for j in range(13):
                offspring1[i][j] = p1[i][j] * alpha + (1-alpha) * p2[i][j]

                offspring2[i][j] = p1[i][j] * (1-alpha) + alpha * p2[i][j]

        else:
            offspring1[i] = p1[i] * alpha + (1-alpha) * p2[i]

            offspring2[i] = p1[i] * (1-alpha) + alpha * p2[i]
    return offsprigng1, offspring2
