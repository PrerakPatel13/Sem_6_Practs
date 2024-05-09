def push(element):
    global operations_count,unit,stack_len
    if len(stack)<=stack_len:
        stack.append(element)
        operations_count+=1
        unit.append(1)
        print(f"Stack after pushing {element} is {stack} and the unit array is {unit}")    
def pop():
    if len(stack)==0:
        return
    else:
        stack.pop()
def multipop(k):
    global operations_count,unit
    num_of_elements=0
    for i in range(k):
        if len(stack)!=0:
            pop()
            num_of_elements+=1
            operations_count+=1
    unit.append(num_of_elements)
    print(f"Stack after popping {k} elements is {stack} and the unit array is {unit}")
    return num_of_elements
arr=[8,3,1,9,8,7,3,6]
stack=[]
stack_len=8
unit=[]
operations_count=0
for i in arr:
    print(f"element {i} : - ")
    if i<=len(stack):
        print(f"since {i} is less than equal to {len(stack)}, therefore we multipop {i} element/s")
        multipop(i)
    push(i)
print(f"T(n)={sum(unit)} and num of operations is {operations_count}")
print(f"Time complexity O({sum(unit)//operations_count})")