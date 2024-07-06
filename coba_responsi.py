
from ai_pkg.search import *

start = 'munchen'
goal = 'frankfurt'
city_map = Graph(dict(
    frankfurt=dict(mannheim=85, kassel=173, wuzzburg=217),
    mannheim=dict(frankfurt=85,karlsruhe=80),
    karlsruhe=dict(mannheim=80 ,augsburg=250),
    augsburg=dict(karlsruge=250, augsburg=84 ),
    

    wuzzburg=dict(erfurt=186, nurnberg=103, frankfurt=217),
    erfurt=dict(wuzzburg=186),
    nurnberg=dict(wuzzburg=103, stuttgart=183, munchen=167),
    stuttgart=dict(nurnberg=183),


    kassel=dict(frankfurt=173, munchen=502), 
    munchen=dict(augsburg=84, kassel=502, nurnberg=167)),
    directed=True)

class CityProblem(Problem):
    def __init__(self, initial, goal, graph):
        Problem.__init__(self, initial, goal)
        self.graph = graph

    def actions(self, A):
        return list(self.graph.get(A).keys())

    def result(self, state, action):
        return action

    def path_cost(self, cost, A, action, B):
        return cost + (self.graph.get(A, B) or infinity)
    
def depth_first_search(problem):
    global track_path
    frontier = [(Node(problem.initial))]
    explored = set()
    track_path = [problem.initial]
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        expanded = node.expand(problem)
        for child in expanded:
            track_path.append(child.state)
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None

if __name__ == '__main__':
    track_path = []
    romania_problem = CityProblem(start, goal, city_map)

node = depth_first_search(romania_problem)
if node is not None:
    final_path = node.solution()
    final_path.insert(0, start)
    print('TRACKING PATH: ', ' -> '.join(track_path))
    print('SOLUTION PATH: ', ' -> '.join(final_path))