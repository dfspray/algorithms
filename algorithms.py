def square_root(target, arr=None):
    if arr == None:
        target_range = target*1000
        arr = [number*.001 for number in range(0, target_range)]
    middle = int(len(arr)/2)
    tol = .1

    if len(arr) == 1 or arr[middle]*arr[middle] == target:
        print(arr[middle])
        return
    elif arr[middle]*arr[middle] < target:
        square_root(target, arr[middle:])
    elif arr[middle]*arr[middle] > target:
        square_root(target, arr[:middle])

def dyn_example(arr, target, dyn_dict={}):
    if dyn_dict == {}:
        dyn_dict[target] = []
    for item in arr:
        match = target - item
        if match in arr:
            dyn_dict[target].append([item, match])
    print(dyn_dict)
    return dyn_dict

def median():
    quantity = int(input("how many?"))
    input_list = []

    def median_func(list1):
        list1 = selection_sort(list1)
        if len(list1)%2 != 0:
            med = list1[int(len(list1)/2)]
        else:
            med = (list1[int(len(list1)/2)-1] + list1[int(len(list1)/2)]) / 2
        print(float(med))

    for number in range(0, quantity):
        input_list.append(int(input()))
        median_func(input_list)

def bubble_sort(arr):
    length = len(arr)
    for index in range(length):
        for sub_index in range(length-index-1):
            print(sub_index)
            if arr[sub_index] > arr[sub_index+1]:
                arr[sub_index], arr[sub_index+1] = arr[sub_index+1], arr[sub_index]
            print(arr)
    return arr

def selection_sort(arr):
    for index in range(len(arr)):
        min_index = index
        for sub_index in range(index+1, len(arr)):
            if arr[min_index] > arr[sub_index]:
                min_index = sub_index
        arr[index], arr[min_index] = arr[min_index], arr[index]
        print(arr)
    return arr

def insertion_sort(arr):
    for index in range(1, len(arr)):
        key = arr[index]
        backwards_index = index - 1
        while backwards_index >= 0 and key < arr[backwards_index]:
            arr[backwards_index+1] = arr[backwards_index]
            backwards_index -= 1
            print(key)
            print(arr)
        arr[backwards_index+1] = key
    print(arr)

def merge_sort(arr):
    print(arr)
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        left_index = right_index = index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                arr[index] = left[left_index]
                left_index += 1
            else:
                arr[index] = right[right_index]
                right_index += 1
            index += 1

        while left_index < len(left):
            arr[index] = left[left_index]
            left_index += 1
            index += 1

        while right_index < len(right):
            arr[index] = right[right_index]
            right_index += 1
            index += 1
    return arr
    
def quick_sort(arr, first=0, last=None):
    print(arr)
    if last == None:
        last = len(arr) - 1
    if first < last:
        pi = partition(arr, first, last)
        quick_sort(arr, first, pi-1)
        quick_sort(arr, pi+1, last)
    return arr

def partition(arr, first, last):
    index = first - 1
    pivot = arr[last]
    for sub_index in range(first, last):
        if arr[sub_index] <= pivot:
            index += 1
            arr[index], arr[sub_index] = arr[sub_index], arr[index]
    arr[index+1], arr[last] = arr[last], arr[index+1]
    return index + 1

class Solution(object):    
    def longestPalindrome(self, s):
        palindromes = []
        for index in range(len(s)):
            for subindex in range(index, len(s)):
                marker = True
                count = index
                subcount = subindex
                while count <= subcount and marker == True:
                    if s[count] == s[subcount]:
                        count += 1
                        subcount -= 1
                    else:
                        marker = False
                if marker == True:
                    palindromes.append(s[index:subindex+1])
        long = 0
        longest = ''
        for palindrome in palindromes:
            if len(palindrome)>long:
                longest = palindrome
                long = len(palindrome)
        return longest

def dynamic_fibbonacci(number):
    fib_dict = {}
    fib_dict[0] = 0
    fib_dict[1] = 1
    for index in range(2, number+1):
        fib_dict[index] = fib_dict[index-1] + fib_dict[index-2]
    print(fib_dict)
    return fib_dict[number]

def number_extractor(self, str):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    number_string = ''
    for index in range(len(str)):
        if str[index] != ' ':
            if str[index] in numbers:
                number_string += str[index]
            elif str[index] == '+' and number_string == '':
                number_string += str[index]
            elif str[index] == '-' and number_string == '':
                number_string += str[index]
            else:
                break
        elif number_string != '' and str[index] == ' ':
            break
    print(number_string)
    if number_string != '' and number_string != '-' and number_string != '+':
        value = int(number_string)
        if value > 2**31 - 1:
            value = 2**31 -1
        elif value < (-2)**31:
            value = (-2)**31
        else:
            value = int(value)
    else:
        value = 0
    
    return value

def letterCombinations(self, input_string):
    numpad = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'],
              '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'],                                     '9':['w','x','y','z']}
    if len(input_string) > 1:
        combos = numpad[input_string[0]]
        for index in range(0, len(input_string)-1):
            combo = []
            for item1 in combos:
                for item2 in numpad[input_string[index+1]]:
                    combo.append(item1+item2)
            combos = combo
    elif len(input_string) == 1:
        combos = numpad[input_string[0]]
    else:
        combos = []

    return combos

def twoSum(arr1, target):
    solutions_list = []
    for index in range(len(arr1)):
        new_target = target - arr1[index]
        if new_target in arr1[index+1:]:
            solutions_list = [index, arr1[index+1:].index(new_target)+index+1]
            break
    return solutions_list

def threeSum(self, arr):
    three_list = self.selection_sort(arr)
    print(three_list)
    solution = []
    for index in range(len(arr)-2):
        if (index != 0) and (arr[index] == arr[index-1]):
            continue
        lower = index + 1
        upper = len(arr) - 1
        while upper > lower:
            total = arr[index] + arr[lower] + arr[upper]
            if total == 0:
                solution.append([arr[index], arr[lower], arr[upper]])
                while upper-1>lower and arr[upper] == arr[upper-1]:
                    upper -= 1
                while upper-1>lower and arr[lower] == arr[lower+1]:
                    lower += 1
                lower += 1
                upper -= 1
            elif total < 0:
                lower += 1
            else:
                upper -= 1
    return solution

def node_flattener(node, num_list=[]):
    num_list.append(str(node.val))
    if node.next:
        node_flattener(node.next)
    return int(''.join(num_list[::-1]))

def node_builder(num_list, node = None):
    if node == None:
        node = ListNode(num_list[0])
    if len(num_list)>1:
        node.next = ListNode(num_list[1])
        node_builder(num_list[1:], node.next)
    return node

#two pointer method
#logic: the lower wall has to move inwards, and anything moving inwards requires a taller wall to have a larger volume
def maxArea(height):
    max = 0
    left = 0
    right = len(height) - 1
    while left < right:
        volume = (right - left)*min([height[left], height[right]])
        if volume > max:
            max = volume
        if height[left]<height[right]:
            left += 1
        else:
            right -= 1
    return max

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class BinaryImbalance:
    def __init__(self):
        self.count = 0
    def findTilt(self, root: TreeNode) -> int:
        self.recursive(root)
        return self.count
    
    def recursive(self, node):
        if node:
            left = self.recursive(node.left)
            right = self.recursive(node.right)
            self.count += abs(left - right)
            return left+right+node.val
        else:
            return 0

class UnivalueTree:
    def __init__(self):
        self.mark = None
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root:
            self.mark = root.val
        return self.recursion(root)
    def recursion(self, root):
        if root:
            left = self.recursion(root.left)
            right = self.recursion(root.right)
            if root.val == self.mark and left and right:
                return True
            else:
                return False
        else:
            return True

class maxBinaryTree:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        root = TreeNode(max(nums))
        def recursion(node, nums):
            if node and nums != []:
                middle = nums.index(max(nums))
                left = nums[:middle]
                right = nums[middle+1:]
                if left != []:
                    node.left = TreeNode(max(left))
                    recursion(node.left, left)
                if right != []:
                    node.right = TreeNode(max(right))
                    recursion(node.right, right)
                return node
            else:
                return None
        return recursion(root, nums)

class indexingBinaryTree:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        levels = {}
        def recursion(node, position = 1, level = 0):
            width = 2**level
            if node:
                levels.setdefault(level, [])
                levels[level].append(position)                              
                recursion(node.left, position * 2 - 1, level + 1)
                recursion(node.right, position * 2, level + 1)
            return

        if root:
            recursion(root)
            result = max([max(item) - min(item) + 1 for item in levels.values()])
        else:
            result = 0
        return result

class romanNumeralTranslation:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9,
                 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        result = 0
        dummy = s + ' '
        for index in range(len(s)):
            if index>0:
                if roman.get(dummy[index - 1: index+1], None):
                    continue
            if roman.get(dummy[index:index+2], None):
                result += roman[dummy[index:index+2]]
            else:
                result += roman[dummy[index]]
        return result

class reverseInteger:
    def reverse(self, x: int) -> int:
        int_str = str(x)
        reversed = ""
        sign = ''
        for index in range(len(int_str)):
            if str(x)[index] != '-':
                reversed = str(x)[index] + reversed
            else:
                sign = '-'
        result = int(sign+reversed)
        if result < 2**31-1 and result >-2**31:
            return result
        else:
            return 0

class fullPalindrome:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

class removeNode:
    def __init__(self):
        self.dummy_node = None
        self.head = None
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        self.head = head
        def recursion(node, depth=0):
            if node:
                depth = recursion(node.next)
                if depth == n-1:
                    self.dummy_node = node
                if depth == n+1:
                    node.next = self.dummy_node
                return depth + 1
            else:
                return 1
        depth = recursion(head)
        print(depth)
        if depth == n+1:
            return head.next
        if depth > n+1:
            return head
        else:
            return self.head

if __name__ == '__main__':
    node = Node(5)
    node.next = Node(4)
    node.next.next = Node(3)
    print(node_flattener(node))
