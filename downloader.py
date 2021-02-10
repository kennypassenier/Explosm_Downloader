from urllib.request import urlretrieve

f = open('URLLIST.txt', 'r')
fileString = []
counter = 0
for line in f:
    fileString.append(line)
for item in fileString:
    counter = counter + 1
    try:
        print(item)
        print(item.endswith('.jpg\n') or item.endswith('.JPG\n'))
        '''
        if item.endswith('.jpg\n') or item.endswith('.JPG\n'):
            urlretrieve(item, "Number " + str(counter) + ".jpg")
        elif item.endswith('.png\n') or item.endswith('.PNG\n'):
            urlretrieve(item, "Number " + str(counter) + ".png")
        elif item.endswith('.gif\n') or item.endswith('.GIF\n'):
            urlretrieve(item, "Number " + str(counter) + ".gif")
        '''
    except:
        print('Your program sucks\n')
f.close
