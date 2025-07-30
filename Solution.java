import java.util.*;

class Solution {
    
	public static List<List<String>> solveNQueens (int n) {
		List<List<String>> ret = new ArrayList<>();
		
		List<String> l = new ArrayList<>();
		
		// create 1 board
		char[] b = new char[n];
		Arrays.fill(b, '.');
		String s = new String(b);
		for (int i=0; i<n; i++) {
			l.add(s);
		}
		System.out.println(l);
		
		// try put queen
		for (int i=0; i<n; i++) {
			
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



