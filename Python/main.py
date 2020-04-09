from incrementalSearch import incrementalSearch
from bisection import bisection
from newton import newton
from falseRule import falseRule
import inspect 


def incOpt():
    args = inspect.getfullargspec(incrementalSearch)[0]
    return incrementalSearch(*defineParams(args))

def bicOpt(): 
    args = inspect.getfullargspec(bisection)[0]
    return bisection(*defineParams(args))

def newtonOpt():
    args = inspect.getfullargspec(newton)[0]
    return newton(*defineParams(args))

def falseOpt(): 
    args = inspect.getfullargspec(falseRule)[0]
    return falseRule(*defineParams(args))


def main():
    print('1 for incremental search\n'
    '2 for bisection\n'
    '3 for newton\n'
    '4 for false rule')

    option = int(input())
    
    switch = {
        1: incOpt,
        2: bicOpt,
        3: newtonOpt,
        4: falseOpt
    }

    func = switch.get(option, lambda: "Invalid month")
    showTable(func())


def defineParams(params):
    values = []
    for param in params:
        print('Enter %s ' % (param)) 
        values.append(float(input()))
    return values

def showTable(table):
    for key in table[0].keys():
        print('%s | ' % (key) ,end =" ")
    print('')
    for row in table:
        for value in row.values():
            print('%s | ' % (value) ,end =" ")
        print('')

if __name__ == "__main__":
    main()
