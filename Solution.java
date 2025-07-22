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
	
	public static boolean IsValid (char[][] board, int n, int pos_i, int pos_j) {
		// check horizontal
		for (int i=0; i<n; i++) {
			if (i == pos_i)
				continue;
			if (board[i][pos_j] == 'Q')
				return false;
		}
		
		// check vertical
		for (int j=0; j<n; j++) {
			if (j == pos_j)
				continue;
			if (board[pos_i][j] == 'Q')
				return false;
			
		}
		
		// check diagonal (top-left to bottom-right)
		//for (int i=0, j=0; i<n, j<n; i++, j++) {
			
		//}
		
		//for (int j=0; j<n; j++) {
			
		//}
		
		
		// check diagonal (top-right to bottom-left)
		
		
		//if (i == pos_i && j == pos_j)
		//	continue;
		
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
			System.out.println(  );
		}
		
		return board;
	}
	
	public static void main (String[] args) {
		//List<List<String>> board = solveNQueens(1);
		
		int n = 4;
		char[][] board = CreateBoard(n);
		//PrintBoard(board, n);
		
		
		//boolean b = CheckAttack(board1, pos);
		
		System.out.println( board[0] );
	}
	
	/*
	public static void main (String []args) {
		System.out.println( "hello" );
	}*/
}






