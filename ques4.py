def display_array(arr):
    print("Array elements:", ' '.join(map(str, arr)))

def insert_number(arr, pos, num):
    arr.insert(pos - 1, num)
    print(f"{num} inserted at location {pos}")

def delete_number(arr, pos):
    if 0 < pos <= len(arr):
        deleted_num = arr.pop(pos - 1)
        print(f"{deleted_num} deleted from location {pos}")
    else:
        print("Invalid location")

def main():
    size = int(input("Enter size: "))
    print("Enter", size, "elements:", end=" ")
    arr = list(map(int, input().split()))
    display_array(arr)

    while True:
        print("1. Insert a number")
        print("2. Delete a number")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            pos = int(input("Location: "))
            if 0 < pos <= len(arr) + 1:
                num = int(input("Number: "))
                insert_number(arr, pos, num)
                display_array(arr)
            else:
                print("Invalid location")
        elif choice == 2:
            pos = int(input("Location: "))
            delete_number(arr, pos)
            display_array(arr)
        elif choice == 3:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

