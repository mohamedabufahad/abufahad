import math

def main():
    n = int(input("Enter the number of values: "))
    values = list(map(float, input("Enter values: ").split()))
    
    mean = sum(values) / n
    
    variance = sum((x - mean) ** 2 for x in values) / n
    
    deviation = math.sqrt(variance)
    
    print("Mean =", round(mean, 2))
    print("Variance =", round(variance, 2))
    print("Deviation =", round(deviation, 2))

if __name__ == "__main__":
    main()

