/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
	a = nums1.concat(nums2)
	a = a.sort((a, b) => a - b)
	
	// odd or even
	if (a.length % 2 == 1) {
		return a[parseInt(a.length/2)];
	} else {
		var i = a.length/2-1;
		return (a[i] + a[i+1])/2;
	}
};