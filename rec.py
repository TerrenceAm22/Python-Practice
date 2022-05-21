# class solution:
#     def fib(self, n: int) -> int:
#         # BASE CASE
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
        
#         # recursive case
#         self.fib(n - 1) + self.fib(n - 2) # if not 1 then program will run forever

#         return
    

# Factorial Solution

def hanoi(n, source, target, spare):
    if n > 0:
        # Move the nth disk from source to target, so they are out of the way
        hanoi(n-1, source, spare,target)
    
     # Move the nth disk from source to target
    target.append(source.pop(0))
    count = count + 1

    # Move the n - 1 disks spare to target
    hanoi(n - 1, spare, target, source)


# initiate call from source A to target  C with auxillary
num_moves =[]

for x in range(1,25):
    A = list(range(x,0,-1))
    B = []
    C = []
    count = 0
    num_moves(x, A, C, B)
    num_moves.append(count)
print(num_moves)

