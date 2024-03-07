class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        Why is it a Window:
            it involve subarrays without the need to move elements 
        Why is it a Slide:
            it involves sections of the array to focus and leave the rest 

        
        """
        curSum = sum(arr[:k-1])
        count = 0

        for l in range(len(arr) - k + 1):
            curSum += arr[l + k - 1]
            if (curSum/k) >= threshold:
                count += 1
            curSum -= arr[l]
        return count

      

            # if (sum(arr[i:i+k])//k >= threshold) and len(arr[i:i+k]) == k:
            #     count += 1 
            # print(arr[i:i+k])
            # print(i, i+k)
            
  