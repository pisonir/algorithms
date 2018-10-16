
# coding: utf-8

# ## Implement an algorithm to determine if a string has all unique characters.  

# In[ ]:


def using_length(string):
    for c in string:
        temp = string.replace(c,"")
        if len(temp) < len(string) -1:
            return False
    return True

def using_dictionary(string):
    vocab = {}
    for c in string:
        vocab[c] = 1
    if sum(vocab.values()) < len(string):
        return False
    else:
        return True
    
def built_in_function(string):
    if len(set(string))<len(string):
        return False
    else: return True


# ## Write a method to replace all spaces in a string with '%20': You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. 

# In[ ]:


def urlify(string, length):
    string = string[:length] #like this I get rid of the spaces at the end of the string. Otherwise one could also use the built-in
                               # string function .strip()
    string = string.replace(' ','%20')
    print (string)
    
urlify('Mr John Smith   ',13)


# ## There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away. 

# In[ ]:


def one_way(str1,str2):
    count = 0
    for c1 in str1:
        for c2 in str2:
            if c1==c2:
                count+=1
                
    if abs(len(str1)-len(str2)) == 1 and count == min(len(str1),len(str2)): #if there was an insert character or a remove
        return True
    elif len(str1)==len(str2) and count == len(str1)-1: #if there was a replace character
        return True
    else:
        return False
    
print (one_way('pale','ple'))
print (one_way('pales','pale'))
print (one_way('pale','bale'))
print (one_way('pale','bake'))


# ## Write an algorithm such that if an element in an MxN matrix is 0, its entire row and  column are set to O.  

# In[ ]:


import numpy as np
from copy import deepcopy


def zerofy(matrix):
    res = deepcopy(matrix) #to not modify matrix
    for i in range(len(matrix)): #iterate on rows
        for j in range(len(matrix[0])): #iterate on columns
            if matrix[i][j]==0:
                res[i]=np.zeros_like(res[i]) #zeros the row
                res[:,j]=np.zeros_like(res[:,j]) #zeros the column
                
    return res




matrix1 = np.array([[2,1,3],[4,0,5],[3,5,8],[9,8,9]])
matrix2 = np.array([[0,1,3],[4,1,5],[3,5,8],[9,8,0]])
print (matrix1)
print (zerofy(matrix1))


# ## Assume you have a method isSubst ring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat"). 

# In[ ]:


def is_rotation(s1, s2):
    
    #first check, s1 and s2 don't have same length then s2 cannot be a rotation of s1
    if len(s1) != len(s2):
        return False
    #then, to check if 'erbottlewat' is a substring of 'waterbottle'
    # you can check if 'waterbottle' is a substring of 'erbottlewaterbottlewat'
    else:
        return (isSubstring(s1,s2*2))
    
    #otherwise using slicing
    for i in range(len(s1)):
        
        if s2.startswith(s1[i:]) and s2.endswith(s1[:i]): 
            return True
        
    return False


# ## Write code to remove duplicates from an unsorted linked list.

# In[ ]:


from copy import deepcopy
def remove_dups1(l):
    
    l = set(l) #using set
    return l

def remove_dups2(l): #using a dictionary
    temp = deepcopy(l)
    vocab = {}
    for c in l:
        vocab[c] = 0
    for c in temp:
        
        vocab[c]+=1
        if vocab[c]>1:
            l.remove(c) #.remove doesn't return anything, it change the list in place...watch out because it will affect the for loop
    
    return l

l = [1,2,3,2,1]
print (remove_dups2(l))


# ## Implement an algorithm to find the kth to last element of a singly linked list.

# In[ ]:


def k_to_last(ls,k):
    
    return ls[-k]

print(k_to_last([1,2,3,4,5,6,'ciao'],2))


# ## You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
# 

# In[ ]:


def sum_lists(a,b):
    c = 0
    sum_list = []
    en = 0
    while en < min(len(a),len(b))-1:
        for en,(i,j) in enumerate(zip(a,b)):       
            sum_list.append(((i+j+c)%10))
            if i+j+c >= 10:
                c = 1
            else:  
                c = 0
        
        if len(a)>len(b):
            if c == 1:
                a[en+1] += 1
                sum_list = sum_list + a[en+1:]
            else:
                sum_list = sum_list + a[en+1:]
        else:
            if c == 1:
                b[en+1] += 1
                sum_list = sum_list + b[en+1:]
            else:
                sum_list = sum_list + b[en+1:]
            
    return sum_list

def sum_lists_forward(a,b):
    c = 0
    sum_list = []
    
    for i,j in zip(a[::-1],b[::-1]):
        if i+j >= 10:
            sum_list.append(((i+j)%10)+c)
            c = 1
        else:
            sum_list.append(i+j+c)
            c = 0
    return sum_list[::-1]


print (sum_lists([7,4,5],[5,5]))
print (sum_lists_forward([5,1,7],[2,5,5]))


# ## A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

# In[ ]:


def counts(n):
    
    #base case
    if n == 1 or n == 0: return 1
    if n == 2: return 2
    
    #recursive case
    return counts(n-1) + counts(n-2) + counts(n-3)

print (counts(4))


# ## A magic index in an array A [e ... n -1] is defined to be an index such that A[ i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

# In[ ]:


def magic_index_in(A):
    
    i = 0
    f = len(A)-1
    found = False
    
    while i<=f and found == False:
        
        m = int((f+i)/2)
        
        if A[m] == m:
            found = True
        else:
            if A[m] > m:
                f = m-1
            else:
                i = m+1
    return found


# ## Write a recursive function to multiply two positive integers without using the * operator. You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.

# In[ ]:


def recursive_multiplication(a, b):
    if a == 0 or b == 0: return 0
    
    if a < b:
        return b + recursive_multiplication(a-1, b)
    else:
        return a + recursive_multiplication(a, b-1)
    
print (recursive_multiplication(25,5))


# ## Implement an algorithm to print all valid (e.g., properly opened and closed) combinations of n pairs of parentheses.

# In[ ]:


def parens(n):
    
    if n == 0:
        return ''
    elif n == 1:
        return '()'
   
    
    return  [parens(n-1)*n , '('+str(parens(n-1))+')']

print(parens(3))


# ## You are given 2 over-lapping rectangles on a plane. For each rectangle, you are given its bottom-left and top-right points. How would you find the area of their overlap

# In[ ]:


def min_(a,b):
    if a <= b: return a
    else: return b
def max_(a,b):
    if a >= b: return a
    else: return b
def distance(a,b):
    if a>b:
        return a-b
    else:
        return False
def overlap(rect1,rect2):
    xB=rect1[0][0]
    yB=rect1[0][1]
    xT=rect1[1][0]
    yT=rect1[1][1]
    xB_=rect2[0][0]
    yB_=rect2[0][1]
    xT_=rect2[1][0]
    yT_=rect2[1][1]
    
    area = distance(min_(xT,xT_),max_(xB,xB_))*distance(min_(yT,yT_),max_(yB,yB_))
    print(distance(min_(yT,yT_),max_(yB,yB_)))
    return area

 
Rect1 = [(2,1),(5,5)]
Rect2 = [(3,2),(5,7)]
 
print (overlap(Rect1,Rect2))


# ## A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null. Return a deep copy of the list.

# In[ ]:


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        list_dic = {}
        iterN = head
        while iterN:
            list_dic[iterN]=RandomListNode(iterN.label)
            iterN = iterN.next
            
        iterN = head
        while iterN:
            list_dic[iterN].next=list_dic[iterN.next] if iterN.next else None
            list_dic[iterN].random=list_dic[iterN.random] if iterN.random else None
            iterN = iterN.next
            
        return list_dic[head] if head else None


# ## Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

# In[ ]:


def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in nums:
            if i in dic and i == target-i: # this address the particular case in which you have duplicates
                return [j for j,i in enumerate(nums) if i == target-i] #if you have duplicates and they are your answer then return the result immediately
            dic[i] = target-i
        for k,v in dic.items():
            if v in dic:
                return [nums.index(k),nums.index(v)]
            
print (twoSum([3,2,3],6))


# ## Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

# In[ ]:


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root: # if the tree is empty
            return False
        
        return self._findTarget(root,set(),k)
        
    def _findTarget(self,node,nodes,k):
        if not node: #if we reach the bottom of the tree
            return False

        complement = k-node.val #you look for the complementary of your current node value
        if complement in nodes:
            return True

        nodes.add(node.val) #to add elements to a set you do set.add()

        return self._findTarget(node.left,nodes,k) or self._findTarget(node.right,nodes,k) # you check left and right


# ## Write an efficient function to find the first nonrepeated character in a string. For instance, the first nonrepeated character in “total” is 'o' and the first nonrepeated character in “teeter” is 'r'. Discuss the efficiency of your algorithm.

# In[ ]:


def nonrepeated(s):
    count = {}
    for c in s:
        if c not in count:
            count[c] = 0
        else:
            count[c] += 1
    for c in s:
        if count[c] == 0:
            return c
    return False
        
    

print (nonrepeated('totoaall'))


# ## Write an efficient function that deletes characters from an ASCII string. Use the prototype string removeChars( string str, string remove ); where any character existing in remove must be deleted from str. For example,  given a str of "Battle of the Vowels: Hawaii vs. Grozny" and a remove of  "aeiou", the function should transform str to “Bttl f th Vwls: Hw vs. Grzny”. Justify any design decisions you make, and discuss the efficiency of your solution.

# In[ ]:


def removeChars(s,r):
    tic()
    vocab = {}
    #string are immutable, you have to convert it to a list to change the elements inside
    l = list(s)
    for c in r:
        vocab[c]=True
    for i,c in enumerate(l):
        if vocab.get(c):
            l[i]='' 
    print (toc())
    return ''.join(l)

s = 'Battle of the Vowels: Hawaii vs. Grozny'*10000
r = 'aeiou'

print (removeChars(s,r))


# In[ ]:


def removeChars(s,r):
    tic()
    for c in r:
        s=s.replace(c,'')
    print (toc())
    return s

s = 'Battle of the Vowels: Hawaii vs. Grozny'*10000
r = 'aeiou'

print (removeChars(s,r))


# ## Write a function that reverses the order of the words in a string. Forexample, your function should transform the string "Do or do not, there is no try." to "try. no is there not, do or Do". Assume that all words are space delimited and treat punctuation the same as letters.

# In[ ]:


def rev1(s):
    l = s.split()
    l = l[::-1]
    s_ = ' '.join(l)
    return s_

print (rev1('Do or do not, there is no try.'))


# ## Implement a function that prints all possible combinations of the characters in a string. These combinations range in length from one to the length of the string. Two combinations that differ only in ordering of their characters are the same combination. In other words, “12” and “31” are different combinations from the input string “123”, but “21” is the same as “12”.

# In[ ]:


def comb(s):
    if len(s)==1:
        print (s)
        return s
    else:
        #for i in range(len(s)):
        print (s[0])
        print (comb(s[0:]))
        return (s[0]+comb(s[1:]))
        
print(comb('123'))

