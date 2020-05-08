def checkDuplicate():
    listA = ["a","d","n","f","g"]
    index = 0 
    pointer = 0 
    while pointer <= len(listA)-1:
        while index <= len(listA)-1:
            if pointer == index:
                index += 1 
            elif listA[index] == listA[pointer]:
                print("result is false")
                return False
            index += 1 
        pointer += 1 
        index = pointer + 1
    print("result is true")
    return True 
checkDuplicate()