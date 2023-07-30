def abc():
    print('hello')

data = 'Bahot Saara'

def multiplier(*a):
    k = 1
    for i in a:
        k *= i
    return k

print(__name__)           # when this file is run __name__ returns __name__ and when this file is imported in another file __name__ returns the file name

if __name__ == '__main__':
    print(data)

#m