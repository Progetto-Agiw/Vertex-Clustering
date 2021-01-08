import sys
from core.ShingleExtractor import extract_shingle_set
from core.ShingleVectorFactory import create_shingle_vector
from core.loader import Loader
from core.utils import k_shingle_cover
from core.algoritmo import Algoritmo


if len(sys.argv) < 3:
	print("usage: main.py <datasets-folder> <dataset>")
	exit()

dataset_folder = sys.argv[1]
dataset = sys.argv[2]
loader = Loader()
pages = loader.load_pages(dataset_folder, dataset)


hash_table = {}

## PASSO 1 v.0.1
algoritmo = Algoritmo()
hash_table = algoritmo.passo1(pages)

print(hash_table)
         
        
        
## TODO: maximum count covering 
## TODO: decrement counts in H
## TODO: testing passo1
    
webpage = pages[0]
shingle_set = extract_shingle_set(webpage, 10)
shingle_vector = create_shingle_vector(shingle_set)
for elem in tuple(k_shingle_cover(shingle_vector, 7)):
    print(elem.getContent())
print('Contenuto (hash) shingle_vector: ' + str(shingle_vector.getContent()))
print('Nome (webpage) shingle_vector: ' + shingle_vector.getWebpage().getName())
