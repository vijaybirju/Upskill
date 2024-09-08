class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = float('inf')
        min_elements = []
        for i,element in enumerate(list1):
            try:
                j = list2.index(element)
                current_sum = i+j
                if current_sum < min_sum:
                    min_sum = current_sum
                    min_elements = [element]
                if current_sum == min_sum:
                    if element not in min_elements:
                        min_elements.append(element)
            except:
                pass
        return min_elements

        
