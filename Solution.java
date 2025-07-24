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
				if (board[i][j] == 'Q' && (m == 1 || m == -1)) return false;
			}
		}
		
		
		return true;
	}
	
	public static char[][] TryQueen (int n, int x, int y) {
		char[][] board = CreateBoard(n);
		board[x][y] = 'Q';
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				if (x==i && y==j) continue;
				if (IsValid(board, n, i, j)) board[i][j] = 'Q';
			}
		}
		
		// count queens on the board
		int q = 0;
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				if (board[i][j] == 'Q') q++;
			}
		}
		
		//if (q == n) PrintBoard(board, n);
		
		
		return board;
	}
	
	public static void RemoveDuplicate(ArrayList<char[][]> list, int n) {
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				
			}
		}
		
		for (char[][] i : list) {
            PrintBoard(i,n);
        }
	}
	
	public static void main (String[] args) {
		//List<List<String>> board = solveNQueens(1);
		List<char[][]> boards = new ArrayList<>();
		
		int n = 4;
		char[][] board = CreateBoard(n);
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				char[][] b = TryQueen(n, i, j);
				//PrintBoard(b, n);
				//System.out.println("-------");
				
				boards.add( b );
				
			}
		}
		
		//PrintBoard( boards.get(), n);
		//removeDuplicate(boards);
		
	}
	
	/*
	public static void main (String []args) {
		System.out.println( "hello" );
	}*/
}






