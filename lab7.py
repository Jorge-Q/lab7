'''
Name: Jorge Quinonez
Assignment: Lab 7
Professor: Diego Aguirre
Purpose of Program: The purpose of this program is to implement a minimum edit distance method
in which it will find the minimum number of changed that must be performed to a word to turn it into
another, both words are entered into the program.
'''


def edit_distance(s1, s2):

    matrix = [[0 for x in range(len(s2)+1)] for x in range(len(s1)+1)]  # Creating matrix in which we store our values
    for i in range(len(s1)+1):
        for a in range(len(s2)+1):
            if i == 0:  # First string is empty
                matrix[i][a] = a
            elif a == 0:  # Second string is empty
                matrix[i][a] = i
            elif s1[i-1] == s2[a-1]:  # If the last characters are the same ignore them
                matrix[i][a] = matrix[i-1][a-1]
            else:
                matrix[i][a] = 1 + min(matrix[i][a-1], matrix[i-1][a], matrix[i-1][a-1])

    return matrix[len(s1)][len(s2)]  # Returning the right most, last row matrix value


    # Testing our edit distance method
def main():
    print("*Testing edit distance from 'Ipad' to 'Iphone', result is: ", edit_distance("Ipad", "Iphone"))
    print("*Testing edit distance from 'Mario' to 'Wario', result is: ", edit_distance("Mario", "Wario"))
    print("*Testing edit distance from 'Cars' to 'GoKarts', result is: ", edit_distance("Cars", "GoKarts"))
    print("*Testing edit distance from 'Batman' to 'Batcave', result is: ", edit_distance("Batman", "Batcave"))


main()

