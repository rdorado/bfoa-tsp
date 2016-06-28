from reader import read_tsp_file
from tsp_greedy import solve_greedy

tsp = read_tsp_file("/home/rdorado/project/tsp/data/berlin52.tsp")
solution = solve_greedy(tsp["DATA"])
