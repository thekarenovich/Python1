def fibonacci(string):
    for i in string:
        yield i.upper()
        
string = 'hello world'
i = fibonacci(string)
while True:
    try:
        print(next(i))
    except StopIteration:
        break

