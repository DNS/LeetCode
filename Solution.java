import java.util.*;

class Solution {
    
	
	public static List<List<String>> solveNQueens (int n) {
		List<char[][]> list = new ArrayList<>();
		
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				// try put queen on the board
				char[][] board = CreateBoard(n);
				TryQueen(list, board, n, i, j, 0, 0);
				
				
			}
		}
		
		List<List<String>> list_final = new ArrayList<>();
		
		for (int t=0; t<list.size(); t++) {
			List<String> l = new ArrayList<>();
			for (int i=0; i<n; i++) {
				l.add( new String(list.get(t)[i]) );
			}
			list_final.add( l );
		}
		
		return list_final;
	}
	
	public static char[][] CreateBoard (int n) {
		char[][] board = new char[n][n];
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++)
				board[i][j] = '.';
		
		return board;
	}
	
	public static void PrintBoard (char[][] board, int n) {
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				System.out.print( board[i][j] );
			}
			System.out.println( );
		}
		System.out.println("------");
	}
	
	public static boolean IsValid (char[][] board, int n, int x, int y) {
		for (int t=0; t<n; t++) {
			// check vertical (y)
			if (board[t][y] == 'Q') return false;
			
			// check horizontal (x)
			if (board[x][t] == 'Q') return false;
		}
		
		// check diagonally
		// linear gradient formula: m = (y2-y1) / (x2-x1)
		// top-left to bottom-light: 1
		// top-right to bottom-left: -1
		for (int i=0; i<n; i++) {
			if (i == x) continue;
			for (int j=0; j<n; j++) {
				int m = (j-y) / (i-x);
				if (board[i][j] == 'Q' && (m == 1 || m == -1)) {
					//System.out.printf("%d,%d\n", i,j);
					return false;
				}
			}
		}
		
		
		return true;
	}
	
	// backtrack
	public static void TryQueen (List<char[][]> list, char[][] board, int n, int x, int y, int k, int l) {
		board[x][y] = 'Q';
		for (int i=k; i<n; i++) {
			for (int j=l; j<n; j++) {
				if (x==i && y==j) continue;
				if (IsValid(board, n, i, j)) {
					board[i][j] = 'Q';
					//if (j+1 < n) 
					//	TryQueen(list, board, n, x, y, i, j+1);
					
				}
			}
		}
		
		// count queens on the board
		int q = 0;
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				if (board[i][j] == 'Q') q++;
			}
		}
		
		
		
		
		if (q == n) {
			//PrintBoard(board, n);
			if (!CheckDuplicate( list, board, n ))
				list.add( board );
			//return true;
		}// else {
		//	return false;
		//}
			
	}
	
	public static boolean RemoveDuplicate(List<char[][]> list, char[][] board, int n) {
		for (int t=0; t<n; t++) {
			if ( Arrays.equals(list.get(t), board) ) {
				System.out.printf("%d\n", t);
				return false;
			}
		}
		
		return true;
	}
	
	public static void PrintList (List<char[][]> list, int n) {
		for (int t=0; t<list.size(); t++) {
			for (int i=0; i<n; i++) {
				System.out.println( list.get(t)[i] );				
			}
			System.out.println( "-------" );
		}
	}
	
	public static void PrintListList (List<List<String>> list_final, int n) {
		for (int t=0; t<list_final.size(); t++) {
			for (int i=0; i<list_final.get(t).size(); i++) {
				System.out.println( list_final.get(t).get(i) );
			}
			System.out.println( "-------" );
		}
	}
	
	public static boolean CheckDuplicate (List<char[][]> list, char[][] board, int n) {
		for (int t=0; t<list.size(); t++) {
			int cmp_result = 0;
			for (int i=0; i<n; i++) {
				if ( Arrays.equals(list.get(t)[i], board[i]) ) cmp_result++;
			}
			if (cmp_result == n) return true;
		}
		
		return false;
	}
	
	
	public static void main (String[] args) {
		int n = 5;
		List<List<String>> list_final = solveNQueens(n);
		PrintListList(list_final, n);
		
	}
	
	
}


/*
expected:
[["Q....","..Q..","....Q",".Q...","...Q."],
["Q....","...Q.",".Q...","....Q","..Q.."],
[".Q...","...Q.","Q....","..Q..","....Q"],
[".Q...","....Q","..Q..","Q....","...Q."],
["..Q..","Q....","...Q.",".Q...","....Q"],
["..Q..","....Q",".Q...","...Q.","Q...."],
["...Q.","Q....","..Q..","....Q",".Q..."],
["...Q.",".Q...","....Q","..Q..","Q...."],
["....Q",".Q...","...Q.","Q....","..Q.."],
["....Q","..Q..","Q....","...Q.",".Q..."]]
*/



