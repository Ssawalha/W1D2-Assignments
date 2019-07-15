def read_matrix(filename):
    """ loads a text file of a grid of integers and creates a list of lists
    of integers representing the matrix. matrix[r][c] is the element on
    row #r and column #c """
    with open(filename, 'r') as input_file:
        return [[int(column) for column in row.split()] for row in input_file]

matrix = read_matrix('testmatrix0.txt')
# print(matrix[1][2] == 27)  # this is true
print(read_matrix("testmatrix0.txt"))
print(matrix)

def rowsum(lst):
        sumlst = 0
        for num in lst:
                sumlst += num
        return sumlst


def sum_matrix(filename):
        matrix = read_matrix(filename)
        rowssumlst = []
        columnsumlst = [sum(i) for i in list(zip(*matrix))]
        for row in matrix:
                rowssumlst.append(rowsum(row))      
        print ("Row Sums: " + str(rowssumlst))
        print("Column Sums: " + str(columnsumlst))

# sum_matrix("testmatrix0.txt")

def rowsum_sort(filename):
        matrix = read_matrix(filename)
        rowssumlst = []
        for row in matrix:
                rowssumlst.append(row)
        sortedrows = sorted(rowssumlst, key = sum)
        return sortedrows

print(rowsum_sort("testmatrix0.txt"))

def column_sort(filename):
        matrix = read_matrix(filename)
        collst = []
        collst = [list(i) for i in zip(*matrix)]
        sortedcol = sorted(collst, key = sum, reverse = False)
        return sortedcol

print(column_sort("testmatrix0.txt"))

print(column_sort("testmatrix1.txt"))



# testlst = [[1,2],[2,3],[0,5]]
# newlst = sorted(testlst, key = sum, reverse=True)
# emp = []

# for num in testlst:
#         emp.append(rowsum(num))

# print (testlst)
# print(newlst)