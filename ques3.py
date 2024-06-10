
def find_largest_smallest(numbers):
    if not numbers:  
        return None, None 

    largest = smallest = numbers[0]  

    
    for num in numbers:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    return largest, smallest  

def main():
    numbers = []  
    n = int(input("Enter the number of elements: "))  
    
    print("Enter numbers:")
    for _ in range(n):
        num = float(input())  
        numbers.append(num)  

    largest, smallest = find_largest_smallest(numbers) 

    if largest is not None and smallest is not None:  
        print(f"Largest number: {largest}")
        print(f"Smallest number: {smallest}")
    else:
        print("No numbers provided.")

if __name__ == "__main__":
    main()  



