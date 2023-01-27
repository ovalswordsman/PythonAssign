Approach
	1	Traversing through borders and if we encounter an 'O' we will do dfs on that index
	1	While dfs, if we find any 'O', we change to another character, say 'P'
	2	After previous step, all 'O' that are adjacent to border 'O' or adjacent to 'O' that are not flipped will be changed to 'P'
	3	Now traverse through the board, and change the remaining 'O' to 'X' and simultaneously 'P' to back 'O' again.

		Input:[[“X”,”X”,”X”,”X”],
           [“X”,”O”,”O”,”X”],
           [“X”,”X”,”O”,”X”],
           [“X”,”O”,”X”,”X”]]

    After dfs : 
          [[“X”,”X”,”X”,”X”],
           [“X”,”O”,”O”,”X”],
           [“X”,”X”,”O”,”X”],
           [“X”,”P”,”X”,”X”]]
    After last step : 
          [[“X”,”X”,”X”,”X”],
           [“X”,”X”,”X”,”X”],
           [“X”,”X”,”X”,”X”],
           [“X”,”O”,”X”,”X”]]

Space complexity : O(1) for extra space , O(row * col) for stack space while DFS
Time complexity : O(row * col), traversing through whole board
