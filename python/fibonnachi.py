#imports

def fibonacci(i):
    last = 1
    current = 1
    for k in range(1, i + 1):
        print(current)
        next = last + current
        last = current
        current = next

def main():
    fibonacci(5)

#Entry Point
if __name__ == "__main__":
    main()