class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        tracker = defaultdict(set)
        for i in range(0,9):
            rows = set()
            cols = set()
            
            #check squares            
            for j in range(0,9):
                #check subs
                sub_number = i//3 * 3 + j//3
                if board[i][j]!= '.' and (board[i][j] in tracker[str(sub_number)]):
                    return False
                tracker[str(sub_number)].add(board[i][j])
                
            #check rows
                if board[i][j] != '.' and board[i][j] in rows:
                    # print(i,j,'row')
                    return False
                rows.add(board[i][j])
                
            #check columns
                if board[j][i] != '.' and board[j][i] in cols:
                    #print(j,i,'column')
                    return False
                cols.add(board[j][i])

        return True
