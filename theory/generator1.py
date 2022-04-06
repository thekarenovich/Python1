def str_up(string):
    for i in string:
        yield i.upper()
        
string = 'hello world'
i = str_up(string)
while True:
    try:
        print(next(i))
    except StopIteration:
        break

