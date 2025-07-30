import java.util.*;

class Solution {
    
	public static List<List<String>> solveNQueens (int n) {
		List<List<String>> ret = new ArrayList<>();
		
		List<String> l = new ArrayList<>();
		
		// create 1 board
		char[] b = new char[n];
		Arrays.fill(b, '.');
		String s1 = new String(b);
		for (int i=0; i<n; i++) {
			l.add(s1);
		}
		//System.out.println(l);
		
		
		// IsValid
		// check horizontal
		l.set(0, "...Q");
		for (int i=0; i<n; i++) {
			//System.out.println( l.get(i).contains("Q") );
			// if (! l.get(i).contains("Q") )
		}
		
		// check vertical
		for (int i=0; i<n; i++) {
			String s2 = "";
			for (int j=0; j<n; j++) {
				//s2 += new String(l.get(i)[j]);
				//System.out.println( l.get(i).substring(j,j+1) );
				//if ( l.get(i).charAt(j) == 'Q' )
					//System.out.println( l.get(i).charAt(j) );
			}
			//System.out.println(s2);
		}
		
		// check diagonally
		// linear gradient formula: m = (y2-y1) / (x2-x1)
		// top-left to bottom-light: 1
		// top-right to bottom-left: -1
		for (int i=0; i<n; i++) {
			if (i == x) continue;
			for (int j=0; j<n; j++) {
				int m = (j-y) / (i-x);
				if (l.get(i).charAt(j) == 'Q' && (m == 1 || m == -1)) return false;
			}
		}
		
		
		//String row = new String('');
		//b.add(row);
		
		
		//ret.add(a);
		
		return ret;
	}
	
	
	
	
	
	public static void main (String[] args) {
		int n = 4;
		solveNQueens(n);
		
		
		
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



"Q...."
"..Q.."
"....Q"
".Q..."
"...Q."

"Q...."
"...Q."
".Q..."
"....Q"
"..Q.."



*/



