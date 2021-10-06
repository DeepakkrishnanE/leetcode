1089. Duplicate Zeros
_____________________

solution:1
----------
        zeros=arr.count(0)
        i=len(arr)-1
        j=len(arr)+zeros-1
        while(i<j):
            if (j<len(arr)):
                arr[j]=arr[i]
            if (arr[i]==0):
                j-=1
                if j<len(arr):
                    arr[j]=arr[i]
            i-=1
            j-=1
            
  solution:2
  ----------
  
        new=[]
        i=0
        while(i<len(arr)): 
            new.append(arr[i])
            if(arr[i]==0):
                new.append(0)
            arr[i]=new[i]
            i+=1
            
            
  solution:3
  ----------
  
        i=0
        while(i<len(arr)):
            if arr[i]!=0:
                i+=1
            else:
                arr.insert(i+1,0)
                i+=2
                arr.pop()
