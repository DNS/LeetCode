

function Permute {
	param (
		[ref] $arr,
		[int] $left,
		[int] $right
	)

	if ($left -eq $right) {
		$arr.Value | ForEach-Object { Write-Host -NoNewline "$_ " }
		Write-Host
	} else {
		for ($i = $left; $i -le $right; $i++) {
			# swap
			$arr.Value[$i], $arr.Value[$left] = $arr.Value[$left], $arr.Value[$i]
			Permute $arr $($left + 1) $right
			$arr.Value[$i], $arr.Value[$left] = $arr.Value[$left], $arr.Value[$i] # backtrack
		}
	}
}

function test {
	param ([ref] $c)
	$c.Value = '222'
}

# Example usage:
[ref] $a = [System.Collections.ArrayList]::new( @(1, 2, 3, 4, 5, 6, 7) )
Permute $a 0 $($a.Value.Count - 1)

#[ref]$a = 'abc'
#test $a
#$a

