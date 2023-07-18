'''
Task 5
a) Implement hill climbing algorithm
'''

import random

def hill_climbing(initial_state, objective_function, neighbors_function):
    current_state = initial_state
    current_value = objective_function(current_state)

    while True:
        # Generate neighboring states
        neighbors = neighbors_function(current_state)

        # Evaluate the objective function for each neighbor
        neighbor_values = [objective_function(state) for state in neighbors]

        # Find the best neighbor with the highest objective function value
        best_neighbor = max(zip(neighbors, neighbor_values), key=lambda x: x[1])
        best_neighbor_state, best_neighbor_value = best_neighbor

        if best_neighbor_value <= current_value:
            # No better neighbor found, return the current state
            return current_state

        # Move to the best neighbor
        current_state = best_neighbor_state
        current_value = best_neighbor_value

# Example usage
def objective_function(x):
    return -x**2  # Minimize the negative of a quadratic function

def neighbors_function(x):
    return [x + random.uniform(-0.1, 0.1)]  # Generate a single neighbor by perturbing the current state

initial_state = 1.0
best_state = hill_climbing(initial_state, objective_function, neighbors_function)

print("Best state:", best_state)
print("Best value:", objective_function(best_state))
