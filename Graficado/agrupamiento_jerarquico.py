import random
import numpy as np

class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def get_coordenadas(self):
    return (self.x, self.y)
  
  def __str__(self):
    return f'{self.x}#{self.y}'


def generar_vector():
  """ Cada vector tiene caracteristicas heredadas de una clase """
  vectores = []
  for _ in range(6):
    vector = Vector(random.randint(0,6), random.randint(0,6))
    vectores.append(vector)
  return vectores

""" Ahora vamos a obtener la distacia metrica usando Manhattan """
def get_distancia_manhattan(vector_a, vector_b):
  return abs(vector_a.x - vector_b.x) + abs((vector_a.y - vector_b.y))

def main():
  vectores = generar_vector()

  """
  Codigo para graficar

  """

  #Ahora, el alg agrupara vectores en clusters
  clusters = [] #cluster vacío para ir agregando

  #Definimos un primer vector al azar
  primer_vector = random.choice(vectores)
  clusters.append([primer_vector])
  vectores.remove(primer_vector) #Una vez añadido al cluster lo sacamos de la lista de vectores

  """ Memoization para agilizar el cómputo. Guardamos las distancias en un dict"""
  distancias = {}

  cluster = clusters[-1][::] #el primer vector del cluster lo asignamos a la variable

  while vectores:
    menor_distancia = '' #void
    for vector_tracked in cluster:
      for vector in vectores:
        if f'{vector_tracked}*{vector}' not in distancias.keys():
          distancia = get_distancia_manhattan(vector_tracked, vector)
          distancias[f'{vector_tracked}*{vector}'] = distancia
        if menor_distancia:
          if distancias[menor_distancia] > distancias[f'{vector_tracked}*{vector}']:
            menor_distancia = f'{vector_tracked}*{vector}'
        else:
          menor_distancia = f'{vector_tracked}*{vector}'
    #Los pasamos a enteros
    siguiente_v_x = int(menor_distancia.split('*')[1].split('#')[0])
    siguiente_v_y = int(menor_distancia.split('*')[1].split('#')[0])

    for vector in vectores:
      if vector.x == siguiente_v_x and vector.y == siguiente_v_y:
        cluster.append(vector)
        vectores.remove(vector)
        clusters.append(cluster[::])
        break
 
  for cluster in clusters:
    for vector in clusters:
      print(vector)
    print('')
    print('--' * 20)
    print('')
     
    
if __name__ == '__main__':
  main()  
          

