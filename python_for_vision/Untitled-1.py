def fibonacci(n): # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a = 0
    b = 1
    the_list = []
    while n > len(the_list):
        the_list.append(a)
    #By saying a = b and b = a+b we define the
    #fibonacci sequence, since this is how the
    #fibonacci sequence works.
        a = b
        b = a+b
    print the_list
    
fibonacci(10)