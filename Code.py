def remove_item(arr,n,i,j):
    if i>=j:
        return False,  arr
    m = (i+j)//2
    if arr[m]==n:
        arr.pop(m)
        return True ,  arr
    elif j-i == 1 :
        return False,  arr
    
    else:
        if arr[m]> n :
            return remove_item(arr,n,i,m)
        else:
            return remove_item(arr,n,m,j)
    

def insert_n(arr,n,i,j):
    m = (i+j)//2
    if arr[m]>n and arr[m-1]<n:
        return arr[:m] + [n]+ arr[m:]
    elif arr[m] == n :
        return arr[:m] + [n]+ arr[m:]
    
    else:
        if arr[m]> n :
            return insert_n(arr,n,i,m)
        else:
            return insert_n(arr,n,m,j)

        
        
        
def insert_f(arr,n):
    l = len(arr)
    if l == 0 :
        arr.append(n)
    elif l == 1:
        if arr[0] > n:
            arr.insert(0,n)
        else:
            arr.append(n)
    
    elif n < arr[0]:
        arr.insert(0,n)
        return arr 
    elif n> arr[-1]:
        arr.append(n)
        return arr
    else:
        arr = insert_n(arr,n,0,l)
    return arr

def cal_medina(arr):
    l = len(arr)
    if l == 0 :
        print("Wrong!")
    else:
        # arr = sorted(arr)
        if l%2==0:
            c = int(l/2)
            ave = (arr[c]+arr[c-1])/2
            if ave% 1 == 0 :
                print(int(ave))
            else:
                print(ave)
            
        else:
            print(arr[int(l/2)])
    
def median(a,x):
    arr = [] 
    # opers = zip(a,x)
    for i in range(len(x)):
        if a[i] == "r":
            if len(arr)==0:
                print("Wrong!")
            else:
                f, arr = remove_item(arr,x[i],0,len(arr))
                if f :
                    cal_medina(arr)
                else:
                    print("Wrong!")
            # else:
            #     print("Wrong!")

        elif a[i] == 'a':
            arr = insert_f(arr,x[i])
            # print(arr)
            cal_medina(arr)

        

N = int(input())
s = []
x = []
for i in range(0, N):
   tmp = input().strip().split(' ')
   a, b = [xx for xx in tmp]
   s.append(a)
   x.append(int(b))
median(s,x) 
