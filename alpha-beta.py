# Alpha-Beta Pruning Algorithm

def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    
    # Base case: leaf node
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -1000

        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,
                             False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break   # Beta cut-off

        return best

    else:
        best = 1000

        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,
                             True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break   # Alpha cut-off

        return best


# Leaf node values (game scores)
values = [3, 5, 6, 9, 1, 2, 0, -1]

print("The optimal value is :", alphabeta(0, 0, True, values, -1000, 1000))