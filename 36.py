def print_operation(operation, num_rows=6,num_columns=6):
    print(" \t".join([str(i)for i in range(1, num_columns+1)]))
    for i in range(2,num_rows+1):
        print(i,end=" \t")
        for j in range(2,num_columns+1):
            print(operation(i,j),end=" \t")
        print()

print_operation(lambda x,y: x+y)            