def fibonacci(n):
    fibonacci_list = [0,1]
    if n<1:
        return fibonacci_list[:n+1]
    for i in range(2,n+1):
        fibonacci_list.append(fibonacci_list[i-1]+fibonacci_list[i-2])
        return fibonacci_list
    n = 9
    fibonacci_hasil = fibonacci_list(n)
    print("Deret fibonacci hingga ke",n,"adalah",fibonacci_hasil)