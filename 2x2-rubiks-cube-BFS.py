# Rubiks Cube encode
print('''
Please enter the colours of the stickers in the following sequence:

         +---+---+
         | 5 | 6 |
         +---+---+
         | 7 | 8 | 
 +---+---+---+---+---+---+---+---+
 | 1 | 2 | 9 | 10| 17| 18| 21| 22|
 +---+---+---+---+---+---+---+---+
 | 3 | 4 | 11| 12| 19| 20| 23| 24|
 +---+---+---+---+---+---+---+---+
         | 13| 14|
         +---+---+
         | 15| 16|
         +---+---+

Example: OBBBGGOWYGYORYRBRYGWRWOW
'''
)

# Getting User Input
testData = input("Please Enter a Valid Cube Configuration:")

while((len(testData) != 24) or (not testData.isalpha())):
    testData = input("Please Enter a Valid Cube Configuration:")


# Functions representing legal moves

# Turning Right Face Clock wise (CW)
def R(encode):
    return (encode[0] + encode[1] + encode[2] + encode[3] + 
            encode[4] + encode[9] + encode[6] + encode[11] +
            encode[8] + encode[13] + encode[10] + encode[15] +
            encode[12] + encode[22] + encode[14] + encode[20] +
            encode[18] + encode[16] + encode[19] + encode[17] +
            encode[7] + encode[21] + encode[5] + encode[23] )

# Turning Right Face Counter Clock wise (CCW)
def Rprime(encode):
    return (encode[0] + encode[1] + encode[2] + encode[3] + 
            encode[4] + encode[22] + encode[6] + encode[20] +
            encode[8] + encode[5] + encode[10] + encode[7] +
            encode[12] + encode[9] + encode[14] + encode[11] +
            encode[17] + encode[19] + encode[16] + encode[18] +
            encode[15] + encode[21] + encode[13] + encode[23] )

# Turning Up Face CW
def U(encode):
    return (encode[8] + encode[9] + encode[2] + encode[3] + 
            encode[6] + encode[4] + encode[7] + encode[5] +
            encode[16] + encode[17] + encode[10] + encode[11] +
            encode[12] + encode[13] + encode[14] + encode[15] +
            encode[20] + encode[21] + encode[18] + encode[19] +
            encode[0] + encode[1] + encode[22] + encode[23] )

# Turning Up Face CCW
def Uprime(encode):
    return (encode[20] + encode[21] + encode[2] + encode[3] + 
            encode[5] + encode[7] + encode[4] + encode[6] +
            encode[0] + encode[1] + encode[10] + encode[11] +
            encode[12] + encode[13] + encode[14] + encode[15] +
            encode[8] + encode[9] + encode[18] + encode[19] +
            encode[16] + encode[17] + encode[22] + encode[23] )

# Turning Front Face CW
def F(encode):
    return (encode[0] + encode[12] + encode[2] + encode[13] + 
            encode[4] + encode[5] + encode[3] + encode[1] +
            encode[10] + encode[8] + encode[11] + encode[9] +
            encode[18] + encode[16] + encode[14] + encode[15] +
            encode[6] + encode[17] + encode[7] + encode[19] +
            encode[20] + encode[21] + encode[22] + encode[23] )

# Turning Front Face CCW
def Fprime(encode):
    return (encode[0] + encode[7] + encode[2] + encode[6] + 
            encode[4] + encode[5] + encode[16] + encode[18] +
            encode[9] + encode[11] + encode[8] + encode[10] +
            encode[1] + encode[3] + encode[14] + encode[15] +
            encode[13] + encode[17] + encode[12] + encode[19] +
            encode[20] + encode[21] + encode[22] + encode[23] )


# Get neighbourhood of current configuration
# I.e. all possible configurations for the resulting configuration 
# with legal moves predefined above

# set of legal moves
moves = {R, Rprime, U, Uprime, F, Fprime}

def N(v):
    return {move(v) for move in moves} 

# Vertex processing function 
def solutionFound(V):
    Lsolved = len(set(V[:4])) == 1
    Usolved = len(set(V[4:8])) == 1
    Fsolved = len(set(V[8:12])) == 1
    Dsolved = len(set(V[12:16])) == 1
    Rsolved = len(set(V[16:20])) == 1
    Bsolved = len(set(V[20:])) == 1
    return Lsolved and Usolved and Fsolved and Dsolved and Rsolved and Bsolved

# Breadth-First Search base case
def BFS(u):
    if solutionFound(u):
        return 0
    
    D = [{u}, N(u)]         #D_0 = {u}
                            #D_1 = N_v(u)

    #Determine if solved config exists in D_1                     
    print(f">> Processing Vertices in Distance: {len(D)-1}") 
    for V in D[-1]:         
        if solutionFound(V):
            return len(D)-1

    return BFSRecur(D)

# BFS recursive case
def BFSRecur(D):
    # D_{j} = N_v(v in D_{j-1}) \ D_{j-1} U D_{j-2}
    Dnew = {vnew for v in D[-1] for vnew in N(v) if vnew not in D[-2] 
            and vnew not in D[-1]}     

    D.append(Dnew)

    #Determine if solved config exists in D_j
    print(f">> Processing Vertices in Distance: {len(D)-1}") 
    for vnew in D[-1]:
        if solutionFound(vnew):
            return len(D)-1

    return BFSRecur(D)
            
def solution(problemInstance):
    print("Starting 2x2 Rubiks Cube Solve")
    distanceSearched = BFS(problemInstance)
    return distanceSearched

def printSolution(solutionInstance):
    print(f"The configuration can be solved in {solutionInstance} moves")

printSolution(solution(testData))


