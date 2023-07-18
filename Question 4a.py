'''
Question 4
a)
There are n tasks you need to complete for a game, labelled from 1 to n.
We are given r[i]=[x,y] representing a prerequisite relationship between task x and task y: task x has to be completed before task y.
In one step you can complete any number of task as long as you have completed all the prerequisites for the tasks you are provided while playing game.
Return the minimum number of steps needed to complete all tasks. If there is no way to complete all the tasks, return -1.

Input: N = 3, r= [[1,3],[2,3]] Output: 2 Explanation: In the first step, you can complete task 1 and 2. In the second semester, step task 3 can be completed.

'''

from collections import defaultdict, deque

def minimumSteps(N, r):
    # Create a directed graph
    graph = defaultdict(list)
    inDegree = [0] * (N+1)  # inDegree array to track the prerequisites count for each task

    # Populate the graph and in-degree array
    for prerequisite in r:
        x, y = prerequisite
        graph[x].append(y)
        inDegree[y] += 1

    # Enqueue tasks with in-degree 0
    q = deque()
    for task in range(1, N+1):
        if inDegree[task] == 0:
            q.append(task)

    steps = 0  # Count the number of steps

    # Process tasks in topological order
    while q:
        cur = q.popleft()
        steps += 1

        # Decrement in-degree of prerequisite tasks
        for task in graph[cur]:
            inDegree[task] -= 1
            if inDegree[task] == 0:
                q.append(task)

    if steps == N:
        return steps
    else:
        return -1


# Example usage
N = 3
r = [[1, 3], [2, 3]]
result = minimumSteps(N, r)
print(result)  # Output: 2
