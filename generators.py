import numpy as np

generator_laue_C1 = [ [1.0, 0, 0, 0] ]

generator_laue_C2 = [ [1.0, 0, 0, 0],
                      [0, 0, 0, 1.0] ]

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
map_C2 = [0, 1, 2, 3, 4, 10, 11, 13, 15, 16, 18, 21]
map_C3 = [0, 1, 2, 4]
map_C4 = [0, 2, 4, 6, 12, 14]
map_C6 = [0, 2]
map_D2 = [0, 1, 2, 7, 10, 11]
map_D3 = [0, 1]
map_D4 = [0, 2, 10]
map_D6 = [0]
map_T = [0, 1]
map_O = [0]

generator_dict = { 'C1': (generator_laue_C1, generator_laue_O,  map_C1),
                   'C2': (generator_laue_C2, generator_laue_O,  map_C2),
                   'C3': (generator_laue_C3, generator_laue_D6, map_C3),
                   'C4': (generator_laue_C4, generator_laue_O,  map_C4),
                   'C6': (generator_laue_C6, generator_laue_D6, map_C6),
                   'D2': (generator_laue_D2, generator_laue_O,  map_D2),
                   'D3': (generator_laue_D3, generator_laue_D6, map_D3),
                   'D4': (generator_laue_D4, generator_laue_O,  map_D4),
                   'D6': (generator_laue_D6, generator_laue_D6, map_D6),
                   'T':  (generator_laue_T,  generator_laue_O,  map_T),
                   'O':  (generator_laue_O,  generator_laue_O,  map_O) }

#HM names
#C1: '1'
#C2: '2'
#C3: '3'
#C4: '4'
#C6: '6'
#D2: '222'
#D3: '32'
#D4: '422'
#D6: '622'
#T:  '23'
#O:  '432'
