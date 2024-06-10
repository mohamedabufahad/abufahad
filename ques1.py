def display_array(arr):
    print("The elements of array:", ' '.join(map(str, arr)))

def main():
    size = int(input("Enter size: "))
    print("Enter elements:", end=" ")
    arr = list(map(int, input().split()))
    display_array(arr)

if __name__ == "__main__":
    main()

