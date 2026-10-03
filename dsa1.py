# class Solution:
#     def __init__(self, n, temp, i):
#         self.n = n
#         self.temp = temp
#         self.i = i
# 
#         while self.i <= self.n:
#             self.j = self.temp + self.i
#             self.temp = self.j
#             self.i += 1
# 
# 
# sol = Solution(5, 0, 1)
# print(sol.temp)
# 
# class Solution:
#     def __init__(self,n,i,j,temp):
#         self.n = n
#         self.i=i
#         self.j=j
#         self.temp = temp
#         
#         while(self.i<=self.n):
#             if(self.i%2==0):
#                 self.temp = self.i + self.j
#             self.j = self.temp
#             self.i +=1
#                 
#         
#         
# sol = Solution(5,1,0,0)
# print(sol.temp)

# class Solution:
#     def __init__(self,n,i,j,temp):
#         self.n=n
#         self.i=i
#         self.j=j
#         self.temp=temp
#         
#         while(self.n>=self.i):
#             if self.i%2!=0:
#                 self.temp = self.i +self.j
#                 self.j = self.temp
#             self.i += 1
# sol = Solution(10,1,0,0)
# print(sol.temp)
#             
# class Factorial:
#     def __init__(self,n,i,temp):
#         self.n = n
#         self.i = i
#         self.temp = temp
#         
#         while(self.n>=1):
#             self.temp = self.n * self.i
#             self.i = self.temp
#             self.n -= 1
# sol = Factorial(10,1,0)
# print(sol.i)
# 
# class Count:
#     def __init__(self,n,i,j,lis,op):
#         self.n = n
#         self.j =j
#         self.i=i
#         self.lis = lis
#         self.op=op
#         while self.n!=0:
#             self.i = self.n % 10
#             self.j = self.n // 10
#             self.lis.append(self.i)
#             self.n = self.j
#         self.op=len(self.lis)
#             
# counting=Count(5699,0,0,[],0)
# print(counting.op)
# 
# class Solution:
#     def __init__(self,n,i,j,temp):
#         self.n =n
#         self.i = i
#         self.j = j
#         self.temp = temp
#         
#         while(self.n>=1):
#             self.i = self.n % 10
#             self.j = self.n // 10
#             self.temp = self.temp * self.i
#             self.n = self.j
# product = Solution(5699,0,0,1)
# print(product.temp)
# 
# class Adition:
#     def __init__(self,n,i,j,temp):
#         self.n = n
#         self.i = i
#         self.j = j
#         self.temp = temp
#         
#         while(self.n >=1):
#             self.i = self.n % 10
#             self.j = self.n // 10
#             self.temp += self.i
#             self.n = self.j
# sol = Adition(5699,0,0,0)
# print(sol.temp)
# 
# class SolutionforArmstrong:
#     def __init__(self,n,i,j,arm):
#         self.n = n
#         self.j = j
#         self.i = i
#         self.arm = arm
#         
#         while(self.n>=1):
#             self.i = self.n % 10
#             self.arm =self.arm + self.i**3
#             self.j = self.n // 10
#             self.n = self.j
# sof = SolutionforArmstrong(5699,0,0,0)
# print(sof.arm)
# 
# class Solution:
#     def __init__(self,n,i,reverse):
#         self.n = n
#         self.i = i
#         self.reverse = reverse
#         
#         while(self.n >= 1):
#             self.i = self.n % 10
#             self.i = str(self.i)
#             self.reverse = self.reverse + self.i
#             self.n = self.n // 10
# s=Solution(5699,0,"")
# print(s.reverse)
            
# def patternE(n):
#     for row in range(1, n + 1):
#         printVal = 0 if row % 2 == 0 else 1
#         for col in range(1, row + 1):
#             print(printVal, end=" ")
#             printVal = 0 if printVal == 1 else 1
#         print()
#     
# patternE(5)

# n=5
# def Pattern(n):
#     for i in range(n,0,-1):
#         for j in range(i,0,-1):
#             print("*",end="")
#         print()
# Pattern(n)



n=int(input())
for i in range(1,n+1):
    eve_odd = 0 if i%2 == 0 else 1
    for j in range(1,i+1):
        print(eve_odd,end="")
        eve_odd = not(int(eve_odd))
    print()



        