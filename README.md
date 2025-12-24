BFS(G, start) create empty set VISITED create empty queue Q

add start to VISITED
enqueue start into Q

while Q is not empty do
    node ← dequeue from Q
    print node

    for each neighbour in G[node] do
        if neighbour not in VISITED then
            add neighbour to VISITED
            enqueue neighbour into Q
DFS(v): mark v visited print v for each adjacent u of v if u not visited DFS(u) A_STAR(G, H, start, goal) create empty list OPEN create empty set CLOSED create map g_cost create map PARENT

add start to OPEN g_cost[start] ← 0 PARENT[start] ← NULL

while OPEN is not empty do node ← element in OPEN with lowest (g_cost[node] + H[node]) remove node from OPEN
if node = goal then
    return path using PARENT

add node to CLOSED

for each neighbour, cost in G[node] do
    if neighbour not in CLOSED then
        new_cost ← g_cost[node] + cost
        if neighbour not in g_cost OR new_cost < g_cost[neighbour] then
            g_cost[neighbour] ← new_cost
            PARENT[neighbour] ← node
            add neighbour to OPEN
            ALPHABETA(depth, node, maximizingPlayer, values, alpha, beta)

if depth = maximumDepth then return values[node]

if maximizingPlayer then best ← −∞ for each child of node do val ← ALPHABETA(depth+1, child, FALSE, values, alpha, beta) best ← max(best, val) alpha ← max(alpha, best) if beta ≤ alpha then break // Beta cut-off return best

else best ← +∞ for each child of node do val ← ALPHABETA(depth+1, child, TRUE, values, alpha, beta) best ← min(best, val) beta ← min(beta, best) if beta ≤ alpha then break // Alpha cut-off return best WATER_JUG(jug1, jug2, target) create empty set VISITED create empty queue Q

enqueue (0, 0, path) into Q

while Q is not empty do (a, b, path) ← dequeue from Q

if (a, b) is in VISITED then
    continue
add (a, b) to VISITED

if a = target OR b = target then
    return path

enqueue (a, jug2) into Q          // fill jug2
enqueue (jug1, b) into Q          // fill jug1
enqueue (0, b) into Q             // empty jug1
enqueue (a, 0) into Q             // empty jug2
pour ← min(a, jug2 − b)
enqueue (a − pour, b + pour)      // jug1 → jug2
pour ← min(jug1 − a, b)
enqueue (a + pour, b − pour)      // jug2 → jug1
return NO SOLUTION DECISION_TREE(outlook, humidity)

if outlook = "Sunny" then if humidity = "High" then return "No" else return "Yes"

else if outlook = "Overcast" then return "Yes"

else if outlook = "Rain" then return "Yes" FEED_FORWARD_NEURAL_NETWORK(X, W1, b1, W2, b2)

apply input X to the network

calculate hidden layer input: hidden_input ← X × W1 + b1

apply activation function: hidden_output ← sigmoid(hidden_input)

calculate output layer input: final_input ← hidden_output × W2 + b2

apply activation function: final_output ← sigmoid(final_input)

return final_output TIC_TAC_TOE()

initialize board with 9 empty positions

for each turn from 0 to 8 do display the board if turn is even then player ← 'X' else player ← 'O'

read position from player
place player mark at position

if WIN(player) then
    display board
    print player wins
    stop game
display board print Draw UNIFORM_COST_SEARCH(G, start, goal)

create empty set VISITED create priority queue PQ

insert (0, start) into PQ // cost, node

while PQ is not empty do (cost, node) ← remove node with lowest cost from PQ

if node is in VISITED then
    continue
add node to VISITED

if node = goal then
    return cost

for each neighbour with edge cost in G[node] do
    if neighbour not in VISITED then
        insert (cost + edge_cost, neighbour) into PQ
return NO SOLUTION GREEDY_BEST_FIRST_SEARCH(G, H, start, goal)

create empty set VISITED create priority queue PQ

insert (H[start], start) into PQ // heuristic, node

while PQ is not empty do (h, node) ← remove node with lowest heuristic from PQ

if node is in VISITED then
    continue
add node to VISITED

if node = goal then
    return SUCCESS

for each neighbour in G[node] do
    if neighbour not in VISITED then
        insert (H[neighbour], neighbour) into PQ
return FAILURE MINIMAX(node, depth, maximizingPlayer)

if depth = 0 OR node is terminal then return evaluation of node

if maximizingPlayer then best ← −∞ for each child of node do value ← MINIMAX(child, depth−1, FALSE) best ← max(best, value) return best

else best ← +∞ for each child of node do value ← MINIMAX(child, depth−1, TRUE) best ← min(best, value) return best CRYPTARITHMETIC(words, result)

extract all unique letters assign each letter a unique digit (0–9)

for each possible digit assignment do if leading letter has value 0 then continue

convert words and result to numbers
if sum of word values = result value then
    return valid assignment
return NO SOLUTION
