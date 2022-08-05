import os

if not os.path.exists('Data Analyst'):
    os.mkdir("Data Analyst")

print("the urent location")
print(os.getcwd())

print('the current directory content')
content = os.listdir()
print(content)

if os.path.isdir('Data Aalyst'):
    print('Data Ananlyst is a directory')

if os.path.isfile('set.ipynb'):
    print('set.ipynb is a file')

print('size of pic',os.path.getsize('assignment.ipynb')/1024,'KB')