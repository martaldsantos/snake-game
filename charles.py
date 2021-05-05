from random import shuffle, choice, sample, random
from operator import  attrgetter
from copy import deepcopy
import numpy as np
from keras import models, layers
import pygame
import sys
import random
from project_charles.snake import main



class Individual:
    def __init__(
        self,
        representation=None
    ):
        if representation == None:
            place_holder = self.create_weigths()
            self.representation = place_holder
        else:
            self.representation = representation

        self.fitness = self.evaluate()
        

    def create_weigths(self):
        print('Cheguei')
        model = models.Sequential()
        model.add(layers.InputLayer(input_shape=(13,)))
        model.add(layers.Dense(13, activation='relu'))
        model.add(layers.Dense(3, activation='softmax'))
        model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['acc'])
        return model.get_weights()

    def evaluate(self):
        print('Hello3')
        return main(self.representation)

    # def __repr__(self):
    #     return f"Individual(size={len(self.representation)}); Fitness: {self.fitness}"


class Population:
    def __init__(self, size, optim, **kwargs):
        self.individuals = []
        self.size = size
        self.optim = optim
        for _ in range(size):
            self.individuals.append(
                Individual()
            )
    def evolve(self, gens, select, crossover, mutate, co_p, mu_p, elitism):
        for gen in range(gens):
            new_pop = []

            if elitism == True:
                if self.optim=='max':
                    elite = deepcopy(max(self.individuals, key=attrgetter('fitness')))
                elif self.optim=='min':
                    elite = deepcopy(min(self.individuals, key=attrgetter('fitness')))

            while len(new_pop) < self.size:
                parent1, parent2 = select(self), select(self)
                # Crossover
                if random() < co_p:
                    offspring1, offspring2 = crossover(parent1, parent2)
                else:
                    offspring1, offspring2 = parent1, parent2
                # Mutation
                if random() < mu_p:
                    offspring1 = mutate(offspring1)
                if random() < mu_p:
                    offspring2 = mutate(offspring2)

                new_pop.append(Individual(representation=offspring1))
                if len(new_pop) < self.size:
                    new_pop.append(Individual(representation=offspring2))

            if elitism == True:
                if self.optim=='max':
                    least = min(new_pop, key=attrgetter('fitness'))
                elif self.optim=='min':
                    least = max(new_pop, key=attrgetter('fitness'))
                new_pop.po(new_popindex(least))
                new_pop.append(elite)

            self.individuals = new_pop
            if self.optim=='max':
                print(f'Best Individual: {max(self, key=attrgetter("fitness"))}')
            if self.optim=='min':
                print(f'Best Individual: {min(self, key=attrgetter("fitness"))}')

    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]

    def __repr__(self):
        return f"Population(size={len(self.individuals)}, individual_size={len(self.individuals[0])})"

    
