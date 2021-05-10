from project_charles.charles import Population, Individual
from project_charles.selection import fps, tournament
from project_charles.mutation import swap_mutation, bad_mut
from project_charles.crossover import cycle_co, arithmetic_co
from random import choices
from copy import deepcopy
#from snake import one_game #Delete this



pop = Population(
    size=5,
    optim="max",
)

pop.evolve(
    gens=5, 
    select= tournament,
    crossover= arithmetic_co,
    mutate=bad_mut,
    co_p=0.8,
    mu_p=0.5,
    elitism=False
)
