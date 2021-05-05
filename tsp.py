from project_charles.charles import Population, Individual
from project_charles.search import hill_climb, sim_annealing
from project_charles.selection import fps, tournament
from project_charles.mutation import swap_mutation, bad_mut
from project_charles.crossover import cycle_co, arithmetic_co2
from random import choices
from copy import deepcopy
#from snake import one_game #Delete this







pop = Population(
    size=100,
    optim="max",
)

pop.evolve(
    gens=100, 
    select= tournament,
    crossover= arithmetic_co2,
    mutate=bad_mut,
    co_p=0.8,
    mu_p=0.5,
    elitism=False
)
