# tic-tac-toe
This project was the second assignment of the Artificial Intelligence course at my school. It involved creating a tic-tac-toe game using Minmax and Alpha-Beta pruning algorithms to ensure the computer made the optimal move.

# MinMax(minmax.py)
This is a console-based implementation of a standard 3x3 tic-tac-toe board with an opponent powered by the Minmax Algorithm for decision-making. It evaluates possible moves recursively simulating both players' optimal strategies to find the best move. The algorithm ensures that the computer/AI opponent minimizes potential losses and maximizes its chances of winning

# Alpha-Beta Pruning(alphabeta.py)
This is a console-based implementation of tic-tac-toe as well however this time it involves playing on a 7x7 board. The AI/computer utilizes the Alpha-Beta pruning variant of min max for intelligent move selection. The alpha-beta algorithm optimises the minimax search to reduce the number of explored nodes in the game tree. However, to prevent the algorithm from running for a long time the user specifies the depth at which the AI should reach in the tree.
