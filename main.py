import pygame
import numpy as np
from agent import Agent
from environment import Environment

pygame.init()
screen = pygame.display.set_mode((600, 400))

#Creamos el entorno y el agente inicial
environment = Environment()
agents = [Agent([100, 100])]


running = True
clock = pygame.time.Clock()

while running:
    screen.fill((255,255,255))  # Limpiar la pantalla
    
    # Dibujamos el entorno (comida)
    environment.draw(screen)
    
    # Actualizamos y dibujamos a los agentes
    new_agents = []
    for agent in agents:
        # Movieminto del agente, aleatorio de momento
        direction = np.random.randint(-1, 2, size=2)  
        agent.move(direction)
        
        # De momento se come si se encuentra comida
        food_energy = environment.get_food_at_position(agent.position)
        if food_energy:
            agent.eat(food_energy)
        
        # Reproducciñon
        child = agent.reproduce()
        if child:
            new_agents.append(child)
        
        # Dibujar al agente
        agent.draw(screen)
        
        # Muere si su energía es 0
        if agent.energy > 0:
            new_agents.append(agent)
    
    agents = new_agents
  
    pygame.display.flip()
    
    #Velocidad del bucle
    clock.tick(30)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
