import numpy as np

generator_laue_C1 = [ [1.0, 0, 0, 0] ]

generator_laue_C2 = [ [1.0, 0, 0, 0],
                      [0, 0, 1.0, 0] ]

generator_laue_C3 = [ [1.0, 0, 0, 0],
                      [0.5, 0, 0, np.sqrt(3)/2],
                      [0.5, 0, 0, -np.sqrt(3)/2] ]

generator_laue_C4 = [ [1.0, 0, 0, 0],
                      [np.sqrt(2)/2, 0, 0, np.sqrt(2)/2],
                      [0, 0, 0, 1.0],
                      [np.sqrt(2)/2, 0, 0, -np.sqrt(2)/2] ]

generator_laue_C6 = [ [1.0, 0, 0, 0],
                      [np.sqrt(3)/2, 0, 0, 0.5],
                      [0.5, 0, 0, np.sqrt(3)/2],
                      [0, 0, 0, 1.0],
                      [0.5, 0, 0, -np.sqrt(3)/2],
                      [np.sqrt(3)/2, 0, 0, -0.5] ]

generator_laue_D2 = [ [1.0, 0, 0, 0],
                      [0, 0, 0, 1.0],
                      [0, 1.0, 0, 0],
                      [0, 0, 1.0, 0] ]

generator_laue_D3 = [ [1.0, 0, 0, 0],
                      [0.5, 0, 0, np.sqrt(3)/2],
                      [0, 1.0, 0, 0],
                      [0.5, 0, 0, -np.sqrt(3)/2],
                      [0, -0.5, np.sqrt(3)/2, 0],
                      [0, 0.5, np.sqrt(3)/2, 0] ]

generator_laue_D4 = [ [1.0, 0, 0, 0],
                      [np.sqrt(2)/2, 0, 0, np.sqrt(2)/2],
                      [0, 1.0, 0, 0],
                      [0, 0, 0, 1.0],
                      [0, -np.sqrt(2)/2, np.sqrt(2)/2, 0],
                      [np.sqrt(2)/2, 0, 0, -np.sqrt(2)/2],
                      [0, 0, 1.0, 0],
                      [0, np.sqrt(2)/2, np.sqrt(2)/2, 0] ]

generator_laue_D6 = [ [1.0, 0, 0, 0],
                      [np.sqrt(3)/2, 0, 0, 0.5],
                      [0, 1.0, 0, 0],
                      [0.5, 0, 0, np.sqrt(3)/2],
                      [0, -np.sqrt(3)/2, 0.5, 0],
                      [0, 0, 0, 1.0],
                      [0, -0.5, np.sqrt(3)/2, 0],
                      [0.5, 0, 0, -np.sqrt(3)/2],
                      [0, 0, 1.0, 0],
                      [np.sqrt(3)/2, 0, 0, -0.5],
                      [0, 0.5, np.sqrt(3)/2, 0],
                      [0, np.sqrt(3)/2, 0.5, 0] ]

generator_laue_T = [ [1.0, 0, 0, 0],
                     [0, 0, 0, 1.0],
                     [0.5, 0.5, 0.5, 0.5],
                     [0.5, -0.5, 0.5, -0.5],
                     [0.5, -0.5, -0.5, -0.5],
                     [0.5, 0.5, 0.5, -0.5],
                     [0, 1.0, 0, 0],
                     [0.5, 0.5, -0.5, 0.5],
                     [0, 0, 1.0, 0],
                     [0.5, 0.5, -0.5, -0.5],
                     [0.5, -0.5, 0.5, 0.5],
                     [0.5, -0.5, -0.5, 0.5] ]

generator_laue_O = [ [1.0, 0, 0, 0],
                     [np.sqrt(2)/2, 0, 0, np.sqrt(2)/2],
                     [np.sqrt(2)/2, np.sqrt(2)/2, 0, 0],
                     [0, 0, 0, 1.0],
                     [0.5, 0.5, -0.5, 0.5],
                     [np.sqrt(2)/2, 0, 0, -np.sqrt(2)/2],
                     [0, 0, -np.sqrt(2)/2, np.sqrt(2)/2],
                     [0.5, 0.5, 0.5, -0.5],
                     [0, 1.0, 0, 0],
                     [0, 0, np.sqrt(2)/2, np.sqrt(2)/2],
                     [0, np.sqrt(2)/2, 0, np.sqrt(2)/2],
                     [0.5, 0.5, -0.5, -0.5],
                     [0, -np.sqrt(2)/2, 0, np.sqrt(2)/2],
                     [np.sqrt(2)/2, -np.sqrt(2)/2, 0, 0],
                     [0, 0, 1.0, 0],
                     [0.5, -0.5, -0.5, -0.5],
                     [0, -np.sqrt(2)/2, np.sqrt(2)/2, 0],
                     [0.5, -0.5, 0.5, 0.5],
                     [np.sqrt(2)/2, 0, -np.sqrt(2)/2, 0],
                     [0.5, -0.5, 0.5, -0.5],
                     [np.sqrt(2)/2, 0, np.sqrt(2)/2, 0],
                     [0.5, -0.5, -0.5, 0.5],
                     [0, np.sqrt(2)/2, np.sqrt(2)/2, 0],
                     [0.5, 0.5, 0.5, 0.5] ]

map_C1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
map_C2 = [0, 1, 2, 3, 4, 5, 7, 10, 11, 13, 18, 19]
map_C3 = [0, 1, 2, 4]
map_C4 = [0, 2, 8, 10, 13, 12]
map_C6 = [0, 2]
map_D2 = [0, 1, 2, 7, 10, 11]
map_D3 = [0, 1]
map_D4 = [0, 2, 10]
map_D6 = [0]
map_T = [0, 1]
map_O = [0]

generator_dict = { 'C1i': (generator_laue_C1, generator_laue_O,  map_C1),
                   'C2h': (generator_laue_C2, generator_laue_O,  map_C2),
                   'C3i': (generator_laue_C3, generator_laue_D6, map_C3),
                   'C4h': (generator_laue_C4, generator_laue_O,  map_C4),
                   'C6h': (generator_laue_C6, generator_laue_D6, map_C6),
                   'D2h': (generator_laue_D2, generator_laue_O,  map_D2),
                   'D3d': (generator_laue_D3, generator_laue_D6, map_D3),
                   'D4h': (generator_laue_D4, generator_laue_O,  map_D4),
                   'D6h': (generator_laue_D6, generator_laue_D6, map_D6),
                   'Th':  (generator_laue_T,  generator_laue_O,  map_T),
                   'Oh':  (generator_laue_O,  generator_laue_O,  map_O) }
