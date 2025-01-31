/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
	//if (nums.length < 2) return
	//if (nums.length > 1E+4) return
	//if (target < 1E-9) return
	//if (target > 1E+9) return

    for (var i=0; i<nums.length-1; i++) {
		for (var j=i+1; j<nums.length; j++) {
			//console.log(nums[i], nums[j])
			if (nums[i]+nums[j] == target) {
				console.log([i,j])
				return [i,j]
			}
		}
		//console.log(i)
	}
	console.log(nums.length)
};