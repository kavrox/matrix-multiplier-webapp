def genm(): #takes rows and columns and returns a user input matrix
    rows = int(input("Enter rows: "))
    columns = int(input("Enter columns: "))
    m = [[] for i in range(rows)]
    for i, row in enumerate(m):
        for j in range(1,columns+1):
            row.append(float(input(f"Enter ({i+1},{j})th value: ")))
    return m

def dispm(m):
    if m == -1:
        print("Provide valid matrices for multiplication")
    rows = len(m)
    columns = len(m[0])
    print('---------------------------------------------')
    print(f"MATRIX ({rows} x {columns})\n")
    for row in m:
        print(row)
    print('---------------------------------------------')

def mm(a,b):
    if len(a[0]) != len(b):
        return -1
    r,c = len(a),len(b[0])
    ab = [[0 for i in range(c)] for j in range(r)]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):                
                ab[i][j] += a[i][k] * b[k][j]
    return ab
dispm(mm(genm(),genm()))
       
