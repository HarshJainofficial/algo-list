def findMedianSortedArrays(nums1, nums2):
    n = len(nums1)
    
    # Ensure nums1 is the smaller array
    if n > len(nums2):
        nums1, nums2 = nums2, nums1
        n = len(nums1)

    low, high = 0, n - 1

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (n + 1) // 2 - partitionX

        maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minX = float('inf') if partitionX == n else nums1[partitionX]

        maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minY = float('inf') if partitionY == n else nums2[partitionY]

        if maxX <= minY and maxY <= minX:
            # Found the correct partition
            if (n + n) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2
            else:
                return max(maxX, maxY)
        elif maxX > minY:
            high = partitionX - 1
        else:
            low = partitionX + 1

# Example usage:
nums1 = [1, 2]
nums2 = [3, 4]

median = findMedianSortedArrays(nums1, nums2)
print(median)
