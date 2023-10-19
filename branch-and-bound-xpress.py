import xpress as xp
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

node_counter = 0
edges = []
best_solution = ((None, None), float('-inf'))
node_values = {}


def branch_and_bound(x1_range=(0, xp.infinity), x2_range=(0, xp.infinity)):
    global node_counter, best_solution, edges, node_values

    U34 = xp.problem()

    # Variables
    x1 = xp.var(lb=x1_range[0], ub=x1_range[1] if x1_range[1] is not None else xp.infinity)
    x2 = xp.var(lb=x2_range[0], ub=x2_range[1] if x2_range[1] is not None else xp.infinity)

    U34.addVariable(x1, x2)

    # Constraints
    U34.addConstraint(50 * x1 + 31 * x2 <= 250, 3 * x1 - 2 * x2 >= -4)

    # Objective function
    U34.setObjective(x1 + 0.64 * x2, sense=xp.maximize)

    # Solve
    U34.lpoptimize()
    solution = U34.getSolution()

    node_id = node_counter
    node_counter += 1

    if solution:
        x1_val, x2_val = solution
        objective = U34.getObjVal()

        node_values[node_id] = (round(x1_val, 2), round(x2_val, 2), round(objective, 2))

        if x1_val.is_integer() and x2_val.is_integer() and objective > best_solution[1]:
            best_solution = ((x1_val, x2_val), objective)

        if not x1_val.is_integer():
            x1_floor = int(np.floor(x1_val))
            edges.append((node_id, node_counter))
            branch_and_bound(x1_range=(0, x1_floor), x2_range=x2_range)
            edges.append((node_id, node_counter))
            branch_and_bound(x1_range=(x1_floor+1, None), x2_range=x2_range)

        if not x2_val.is_integer():
            x2_floor = int(np.floor(x2_val))
            edges.append((node_id, node_counter))
            branch_and_bound(x1_range=x1_range, x2_range=(0, x2_floor))
            edges.append((node_id, node_counter))
            branch_and_bound(x1_range=x1_range, x2_range=(x2_floor+1, None))


def visualize_tree(edges, node_values):
    G = nx.DiGraph()
    G.add_edges_from(edges)

    pos = nx.drawing.nx_agraph.graphviz_layout(G, prog='dot')

    nx.draw_networkx_nodes(G, pos, node_color='white', node_size=1)

    nx.draw_networkx_edges(G, pos)

    labels = {}
    for node, values in node_values.items():
        labels[node] = f"x={values[0]}, y={values[1]}, z={values[2]}"

    nx.draw_networkx_labels(G, pos, labels, bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='white'))

    plt.show()


# Execute the Branch-and-Bound algorithm and then print and visualize the result
branch_and_bound()

print(f"Best integer result: x={best_solution[0][0]}, y={best_solution[0][1]}")

# Visualize the tree
visualize_tree(edges, node_values)

