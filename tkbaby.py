import tkinter as tk

def get_table_data():
    """Retrieves data from the Entry widgets in the table."""
    data = []
    for r in range(rows):
        row_data = []
        for c in range(columns):
            row_data.append(entries[r][c].get())
        data.append(row_data)
    print("Table Data:")
    for row in data:
        print(row)
a =[]
root = tk.Tk()
root.title("Tabular Input Form")
p = 0
while p < 2:
    p +=1
    rows = int(input("Enter rows"))
    columns = int(input("Enter columns"))

    entries = []

    # Create column headers (optional)
    headers = ["C"+str(i+1) for i in range(columns)]
    for c, header_text in enumerate(headers):
        header_label = tk.Label(root, text=header_text, font=("Arial", 10, "bold"))
        header_label.grid(row=0, column=c, padx=5, pady=5)

    # Create Entry widgets for tabular input
    for r in range(rows):
        row_entries = []
        for c in range(columns):
            entry = tk.Entry(root, width=15)
            entry.grid(row=r + 1, column=c, padx=5, pady=5) # +1 to account for headers
            row_entries.append(entry)
        entries.append(row_entries)
    if p == 1:
        a = entries
    elif p == 2:
        b = entries

# # Add a button to retrieve data
# submit_button = tk.Button(root, text="Get Data", command=get_table_data)
# submit_button.grid(row=rows + 1, columnspan=columns, pady=10)

# def genm(): #takes rows and columns and returns a user input matrix
#     rows = int(input("Enter rows: "))
#     columns = int(input("Enter columns: "))
#     m = [[] for i in range(rows)]
#     for i, row in enumerate(m):
#         for j in range(1,columns+1):
#             row.append(float(input(f"Enter ({i+1},{j})th value: ")))
#     return m

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
dispm(mm(a,b))
       


root.mainloop()