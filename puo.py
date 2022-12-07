# Histogram maximum area
# histogram  = [4 ,2, 1, 5, 6, 3, 3,3,3, 25]
# prev_ele  =   []
# new_ele = []
# stack = []
# for i in range(len(histogram)):
#     while stack   and histogram[stack[-1]]>= histogram[i]:
#         stack.pop()
#     if not stack:
#         prev_ele.append(-1)
#     if stack:
#         prev_ele.append(stack[-1])
#     stack.append(i)
# stack = []
# for i in range(len(histogram)  -1 ,  -1 ,  -1):
#     while stack   and histogram[stack[-1]]>= histogram[i]:
#         stack.pop()
#     if not stack:
#         new_ele.append(len(histogram))
#     if stack:
#         new_ele.append(stack[-1])
#     stack.append(i)
# new_ele = new_ele[::-1]
# max1 = -10**9
# for i in range(len(histogram)):
#     first1 =  new_ele[i] - 1
#     second1 = prev_ele[i] +1 
#     max1 = max(((first1- second1)+1)*histogram[i] , max1)
# print(max1)

def main(histogram):
    # arr = []
    # for elem in newVal:
    #     if elem !=0:
    #         arr.append(elem) 
    # histogram  = ne
    prev_ele  =   []
    new_ele = []
    stack = []
    for i in range(len(histogram)):
        while stack   and histogram[stack[-1]]>= histogram[i]:
            stack.pop()
        if not stack:
            prev_ele.append(-1)
        if stack:
            prev_ele.append(stack[-1])
        stack.append(i)
    stack = []
    for i in range(len(histogram)  -1 ,  -1 ,  -1):
        while stack   and histogram[stack[-1]]>= histogram[i]:
            stack.pop()
        if not stack:
            new_ele.append(len(histogram))
        if stack:
            new_ele.append(stack[-1])
        stack.append(i)
    new_ele = new_ele[::-1]
    max1 = -10**9
    for i in range(len(histogram)):
        first1 =  new_ele[i] - 1
        second1 = prev_ele[i] +1 
        max1 = max(((first1- second1)+1)*histogram[i] , max1)
    return max1

    
# from operator import add  , sub
# # celebrity problem or largest rectangle with 1's
# M = [[1,0, 1],[1,1,1], [0,1, 1]]
# n  = 3
# max1 =  main(M[0])
# for i in range( 1 , n):
#     for k in range(n ):
#         if M[i][k]!=0:
#             M[i][k]+=M[i-1][k]
        
#     max1 =  max(max1 ,  main(M[i]))
# print(max1)

# Infinix to postfix using stack
# precedence_level  = {"+":1 ,"-":1 , "*":2  , "/":2 , "^":3}
# s = input()
# stack  = []
# arr = []
# for i in s:

#     if i=="(":
#         stack.append("(")
#     elif i==")":
#         while stack and stack[-1]!="(":
#             arr.append(stack.pop())
#         stack.pop()
    
#     elif precedence_level.get(i)==None:
#         arr.append(i)
     
#     else:
      
#         while stack   and precedence_level.get(stack[-1])!=None  and precedence_level[i]<=precedence_level[stack[-1]] :
#             arr.append(stack.pop()) 
#         stack.append(i)
# while stack:
#     arr.append(stack.pop())
# return "".join(arr)

def computing(val, numbers):
    if val =="+":
        return sum(numbers)
    elif val =="-":
        return numbers[0] -  numbers[1]
    elif val =="*":
        return numbers[0]*numbers[1]
    elif val =="/":
        return numbers[0]/numbers[1]
    
s  = input()
operator  = ["+", "-", "/", "*"]
calc = []
i =   0
val  = []
for i in range(len(s)):
    
    opera = []
    if s[i] not in operator:
        val.append(int(s[i]))
    else:
        calc1 = val.pop()
        calc2 =  val.pop()
        new_val = computing(s[i], [calc2 , calc1])
        val.append(new_val)
print(val[0])
            
            
            
    
    
        
