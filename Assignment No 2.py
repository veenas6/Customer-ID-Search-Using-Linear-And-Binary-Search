def linear (list,target):
    for id in list:
        if id==target:
            return True
    return False

def binary(list, target):
    list.sort()
    low=0
    high= len(list)-1
    while low<=high:
        mid=(low+high)//2
        if list[mid]==target:
            return True
        elif list[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return False

id=[131, 132, 133, 134, 135, 136, 137, 138, 139, 140]
target= int(input("Enter id: "))

if linear(id,target):
    print("Linear Search: ID found")
else:
    print("Linear Search: ID not found")

if binary(id,target):
    print("Binary Search: ID found")
else:
    print("Binary Search: ID not found")
