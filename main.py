from readers.uppermodule import record_word_count
from utils import get_random_file
from time import sleep
import random

def main():
    #Gets a random file at the upload folder
    file = get_random_file('upload')
    #Logs and Saves the resoult of the output at a csv file
    record_word_count(file)


    sleep(random.random())

if __name__=='__main__':
    cont = 0
    while(True):
        main()
        # cont+=1
