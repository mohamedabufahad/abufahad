def search_element(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i + 1 
    return -1

def main():
    size = int(input("Enter size: "))
    print("Enter elements:", end=" ")
    arr = list(map(int, input().split()))
    key = int(input("Enter search key: "))
    
    position = search_element(arr, key)
    if position != -1:
        print(f"{key} found at position {position}")
    else:
        print(f"{key} not found")

if __name__ == "__main__":
    main()

