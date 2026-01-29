import os

folder = 'C:/Users/bwillis26/Documents/Repository/377-web-app-dev/python-stuff/photos'
prefix = 'Quincy'
filetype = 'jpg'
count = 1

for filename in os.listdir(folder):
    extension = filename.split('.')[-1]
    if extension == filetype:
        source = folder + '/' + filename
        destination = folder + '/' + prefix + '-' + str(count) + '.jpg'

        os.rename(source, destination)

        print(filename)
        count += 1