Rows_Columns = int(input("Enter Number Of Rows/Columns For The Square Matrix: "))
print("\nOPERATIONS MENU:")
print("\t 1. ADDITION.")
print("\t 2. SUBTRACTION.")
print("\t 3. MULTIPLICATION.")
print("\t 4. TRANSPOSE.")
print("\t 5. EXIT.")
Option = int(input("Enter Option Number: "))
Matrix_1=[]
for i in range(1,Rows_Columns+1):
        Matrix_1.append(input(f"Enter values for matrix 1 row {i} separated by commas: ").split(","))
Matrix_2=[]
for i in range(1,Rows_Columns+1):
        Matrix_2.append(input(f"Enter values for matrix 2 row {i} separated by commas: ").split(","))
Result=[]
for i in range(Rows_Columns):
    Result.append([])
    for j in range(Rows_Columns):
        Result[i].append(j)
        Result[i][j]=0
        Result[i][j]+=0
while(True): 
    if(Option==1):
        for i in range(len(Matrix_1)):
            for j in range(len(Matrix_2[0])):
                Result[i][j] = int(Matrix_1[i][j]) + int(Matrix_2[i][j])
        print('THE ANSWER IS:')
        for r in Result:
            print(r)
    elif(Option==2):
        for i in range(len(Matrix_1)):
            for j in range(len(Matrix_2[0])):
                Result[i][j] = int(Matrix_1[i][j]) - int(Matrix_2[i][j])
        print('THE ANSWER IS:')
        for r in Result:
            print(r)
    elif(Option==3):
        for i in range(len(Matrix_1)):
            for j in range(len(Matrix_2[0])):
                for k in range(len(Matrix_2)):
                    Result[i][j] += int(Matrix_1[i][k]) * int(Matrix_2[k][j])
        print('THE ANSWER IS:')
        for r in Result:
            print(r)
        
    elif(Option==4):
        for i in range(len(Matrix_1)):
            for j in range(len(Matrix_2)):
                    Result[j][i] = int(Matrix_1[i][j])
        print('THE ANSWER IS:')
        for r in Result:
            print(r)
        for i in range(len(Matrix_1)):
            for j in range(len(Matrix_2)):
                    Result[i][j] = int(Matrix_2[j][i])
        print('THE ANSWER IS:')           
        for r in Result:
            print(r)
    elif(Option==5):
        print("Program Finished O_0 !!!")
        break
    else:
        print("Please Select Correct Operation!!!")
    print("\nOPERATIONS MENU:")
    print("\t 1. ADDITION.")
    print("\t 2. SUBTRACTION.")
    print("\t 3. MULTIPLICATION.")
    print("\t 4. TRANSPOSE.")
    print("\t 5. EXIT.")
    Option = int(input("Enter Option Number: "))
    for i in range(Rows_Columns):
        for j in range(Rows_Columns):
            Result[i][j]=0
            Result[i][j]+=0
