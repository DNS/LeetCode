import java.util.*;

class Solution {
    
	public static boolean CheckAttack (int[][] board, int[] position) {
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
	
	public static boolean IsValid (char[][] board, int n, int x, int y) {
		for (int t=0; t<n; t++) {
			// check vertical (y)
			if (board[t][y] == 'Q') {
				//System.out.printf( "vertical hit: %d, %d\n", t, y );
				return false;
			}
			
			// check horizontal (x)
			if (board[x][t] == 'Q') {
				//System.out.printf( "horizontal hit: %d, %d\n", x, t );
				return false;
			}
		}
		
		// check diagonally
		// linear gradient formula: m = (y2-y1) / (x2-x1)
		// top-left to bottom-light: 1
		// top-right to bottom-left: -1
		for (int i=0; i<n; i++) {
			if (i == x) continue;
			for (int j=0; j<n; j++) {
				//System.out.printf( ": %d,%d - %d,%d\n", j,y , i,x );
				int m = (j-y) / (i-x);
				if (board[i][j] == 'Q' && (m == 1 || m == -1)) {
					//System.out.printf( "diagonal hit: %d, %d\n", i, j );
					return false;
				}
			}
		}
		
		
		return true;
	}
	
	public static char[][] TryQueen (char[][] board, int n) {
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				if (IsValid(board, n, i, j)) {
					board[i][j] = 'Q';
				}
				//System.out.print( board[i][j] );
			}
			//System.out.println(  );
		}
		
		return board;
	}
	
	public static void main (String[] args) {
		//List<List<String>> board = solveNQueens(1);
		
		int n = 5;
		char[][] board = CreateBoard(n);
		TryQueen(board, n);
		//board[2][3] = 'Q';
		PrintBoard(board, n);
		
		
		//boolean b = IsValid(board, n, 1, 2);
		//System.out.println( b );
		
	}
	
	/*
	public static void main (String []args) {
		System.out.println( "hello" );
	}*/
}






