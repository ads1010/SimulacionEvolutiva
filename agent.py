"""
Definición del agente

Definimos el comportamiento del agente:  toma decisiones, come, y se reproduce etc.
"""

import numpy as np
import copy
from neural_network import NeuralNetwork
import pygame

class Agent:
    def __init__(self, pos):
        self.brain = NeuralNetwork(4, 5, 2)
        self.position = np.array(pos)
        self.energy = 100
        self.reproduction_energy_threshold = 150
    
    def decide(self, environment_inputs):
        return self.brain.forward(environment_inputs)
    
    def move(self, direction):
        self.energy -= 1
        self.position += direction
    
    def eat(self, food_energy):
        self.energy += food_energy
    
    def reproduce(self):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position.astype(int), 5)
