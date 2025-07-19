import java.util.*;

class Solution {
    
	public static boolean CheckAttack (int [][]board, int []position) {
		position[0] = 777;
		return false;
	}
	
	public static List<List<String>> solveNQueens (int n) {
		List<List<String>> solutions = new ArrayList<>();
		//solutions.add(constructString(board));
		
		return solutions;
	}
	
	public static char[][] CreateBoard (int n) {
		char[][] board = new char[n][n];
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				board[i][j] = '.';
			}
		}
		return board;
	}
	
	public static void PrintBoard (char[][] board, int n) {
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				System.out.print( board[i][j] );
			}
			System.out.println(  );
		}
	}
	
	public static boolean IsValid (char[][] board, int n, int pos_x, int pos_y) {
		// check horizontal
		for (int i=0; i<n; i++) {
			if (i == pos_x)
				continue;
			if (board[i][j] == 'Q')
				return false;
		}
		
		// check vertical
		for (int j=0; j<n; j++) {
			if (j == pos_y)
				continue;
			if (board[i][j] == 'Q')
				return false;
			
		}
		
		
		
		// check diagonal (bottom-left/top-right)
		// check diagonal (bottom-right/top-left)
		if (i == pos_x && j == pos_y)
			continue;
		
		return true;
	}
	
	public static char[][] TryQueen (board, int n) {
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				if (IsValid(board, i, j)) {
					board[i][j] = 'Q';
				}
				//System.out.print( board[i][j] );
			}
			System.out.println(  );
		}
		
		return board;
	}
	
	public static void main (String []args) {
		//List<List<String>> board = solveNQueens(1);
		
		int n = 4;
		char[][] board = CreateBoard(n);
		//PrintBoard(board, n);
		
		
		//boolean b = CheckAttack(board1, pos);
		
		System.out.println( board[0] );
	}
}


