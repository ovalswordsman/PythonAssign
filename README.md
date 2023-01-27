Approach
1. Traversing through borders and if we encounter an 'O' we will do dfs on that index
2. While dfs, if we find any 'O', we change to another char, say 'P' 
3. After this step, all 'O' that are adjacent to border 'O' or adjacent to 'O' that are not flipped will be changed to 'P'
4. Now traverse through the board, and first change the remaining 'O' to 'X' and simultaneously all 'P' to back 'O' again.

Space complexity : O(1) for extra space , O(row * col) for stack space while DFS

Time complexity : O(row * col), traversing through whole board
