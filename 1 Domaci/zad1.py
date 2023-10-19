"""
Pascal Triangle

Problem Description:
Given an integer A, equal to numRows, generate the first numRows of Pascal's triangle.
Pascal's triangle: To generate A[C] in row R, sum up A'[C] and A'[C-1] where A' is array from row R - 1.

Problem Constraints:
0 <= A <= 25

Example Input:
A = 5

Example Output:
[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
"""

# @param A : integer
# @return a list of list of integers
def solve(A):
    
    lista = [1]*A
    for i in range(A):
        lista2 = [1]*(i+1)
        if i == 1:
            lista2[i] = 1
        else:      
            for j in range(i):
            
                if j == 0 :
                    lista2[j] = 1
                else:
                    lista2[j] = lista[i-1][j] + lista[i-1][j-1]
                    print("lista[i-1][j]:", str(lista[i-1][j]), ", lista[i-1][j-1]: ", str(lista[i-1][j-1]))
        lista[i] = lista2        
    return lista
    
    
if __name__ == "__main__":
    lista = solve(5)
    print(lista)
    print("\n")
    for x in lista:
        print(x)