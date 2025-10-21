


function replace {
	for ($i = 0; $i -lt $b.length-2; $i++) {
		if ($b.Substring($i, 2) -eq '()') {
			$b = substring_replace $b '..' $i 2
		}
	}
	
	for ($i = 0; $i -lt $b.length-2; $i++) {
		if ($b[$i] -eq '(') {
			
		}
	}
	
	return $b
}



function find_openbracket {
	param ($a)
	
	for ($i = 0; $i -lt $b.length-2; $i++) {
		if ($b[i] -eq '(') {
			
		} elseif ($b[i] -eq '(') {
			break
		}
	}
}

function substring_replace {
	param ($src, $replace, $start, $length)
	$prefix  = $src.Substring(0, $start)
	$suffix  = $src.Substring($start + $length)
	$new    = $prefix + $replace + $suffix
	return $new
}



#$a = '('
#$a = '(()'
#$a = '(()((('
#$a = '((()))'
#$a = '())()()((()()()))()()()()()()())))(()(())))()())()()()())(((()))))()()())()()()()())))('
#$a = '()(())'
$a = ')(((((()())()()))()(()))('
$a
$Global:b = $a
$Global:stack
replace

