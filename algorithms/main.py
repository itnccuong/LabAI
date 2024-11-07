from a_star import solveAstar
from ucs import solveUCS
from bfs_dfs import solveBFS, solveDFS

# import signal

# # Define a timeout handler
# def timeout_handler(signum, frame):
#     raise TimeoutError

# # Setting up the signal
# signal.signal(signal.SIGALRM, timeout_handler)

# def solve_with_timelimit(input_file, output_file, algorithm_name, solve_function, time_limit=60):
#     try:
#         signal.alarm(time_limit)
#         solve_function(input_file, output_file)
#         signal.alarm(0)  # Disable the alarm
#     except TimeoutError:
#         with open(output_file, 'a') as f:
#             f.write(f"{algorithm_name}\nTLE ({time_limit} seconds)!\n")

def solve_with_timelimit(input_file, output_file, results_csv, algorithm_name, solve_function, time_limit=60):
    solve_function(input_file, output_file, results_csv)

if __name__ == "__main__":

  input_root = 'map/map/'
  output_root = 'map/solution/'
  results_csv = 'results.csv'
  TL = 500

  for i in range(1, 11):
    print(f"Running test case : {i}")

    input_file = input_root + "input-" + str(i).zfill(2) + '.txt'
    output_file = output_root + "output-" + str(i).zfill(2) + '.txt'
    
    # Clear the output file before appending
    open(output_file, 'w').close()
   
    print("Running BFS...")
    solve_with_timelimit(input_file, output_file, results_csv, "BFS", solveBFS, TL)

    print("Running DFS...")
    solve_with_timelimit(input_file, output_file, results_csv, "DFS", solveDFS, TL) 

    print("Running UCS...")
    solve_with_timelimit(input_file, output_file, results_csv, "UCS", solveUCS, TL)
    
    print("Running A*...")
    solve_with_timelimit(input_file, output_file, results_csv, "A*", solveAstar, TL)