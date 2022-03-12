def run_with_log(func):
    with open('file.log', 'w') as file:
        print(func, file=file)
    return func

def func():
    a=10
    try:
        a=a/0
    except:
        return "Don't divide by zero"

if __name__ == '__main__':
    run_with_log(func())