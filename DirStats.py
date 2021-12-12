import os

stats = dict(path='', folders=0, files=0, links=0, size=0)

# Get user input
def get_input():
    global stats
    ret = os.path.abspath(input('Enter a folder path: '))

    if not os.path.exists(ret):
        print('Sorry, that path does not exist!')
        exit(1)
    
    if not os.path.isdir(ret):
        print('Sorry, that path is not a directory!')
        exit(2)

    stats['path'] = ret

#Scan the path recursively
def scan(path):
    global stats
    