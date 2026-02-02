import random

class Food:
    def __init__(self, block_size, height, width, snake_body):
        self.position = self.create(width, block_size, height, snake_body)

    def create(self, width, block_size, height, snake_body):
        while True:
          x = random.randint(0, (width - block_size) // block_size) * block_size
          y = random.randint(0, (height - block_size) // block_size) * block_size
          if(x, y) not in snake_body:
             return x, y