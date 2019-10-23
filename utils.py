import os
import random
from os import path

def get_random_file(dir):
    random_file=random.choice(os.listdir(dir))
    #To force log error!!!
    if(random_file=='_to_force_err'):
        random_file='to_force_err'
    return path.join(dir,random_file)
