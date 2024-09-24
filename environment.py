"""Definición del entorno

De momento establcemos las posiciones de la comida y el método para que los agentes interactúen con ella."""

import pygame
import numpy as np

class Environment:
    """Positiciones de comida en array np dentro de una lista"""
    def __init__(self):
        self.food_positions = [np.array([50, 50]), np.array([150, 150]), np.array([300, 300])]
    

    """Revisar estos metodos son basicos"""
    def get_food_at_position(self, position):
        for food_pos in self.food_positions:
            if np.linalg.norm(food_pos - position) < 10:  # Si está cerca de la comida
                return 20  # Energía ganada
        return 0

    """Dibujar la posicion de comida"""
    def draw(self, screen):
        for pos in self.food_positions:
            pygame.draw.circle(screen, (0, 255, 0), pos.astype(int), 3)  
