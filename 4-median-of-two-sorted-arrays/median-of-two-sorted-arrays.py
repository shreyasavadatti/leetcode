class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        i=0
        j=0
        n=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                n.append(nums1[i])
                i=i+1
            else:
                n.append(nums2[j])
                j=j+1
        while i<len(nums1):
            n.append(nums1[i])
            i=i+1
        while j<len(nums2):
            n.append(nums2[j])
            j=j+1

        if len(n)%2==0:
            mid=len(n)//2
            m1=n[mid]
            m2=n[mid-1]
            midx=(m1+m2)/2.0
            return midx
        else:
            i=len(n)//2
            mid=n[i]
            return mid
