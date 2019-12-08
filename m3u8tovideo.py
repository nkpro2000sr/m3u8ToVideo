import os, requests

index_file_path = input("Enter Index file path with extension m3u8 : ")

index_file = open(index_file_path,'r')

indexes = index_file.read()

index_file.close()

output_file_path = input("Enter output file path : ")

output_file = open(output_file_path,'wb')

folder_path = input("Enter folder path with extension m3u8_contents ('#<internet>' for get file from internet) : ")

if folder_path == '#<internet>' :

    indexes = indexes.split('http')[1:]

    indexes = ['http'+x.split('\n')[0] for x in indexes]

    for index in indexes :

        content = requests.get(index)

        output_file.write(content.content)

else :

    indexes = indexes.split('file:')[1:]

    indexes = [x.split('\n')[0].split('/')[-1] for x in indexes]

    for index in indexes :

        content_file = open(os.path.join(folder_path,index),'rb')

        output_file.write(content_file.read())

        content_file.close()

output_file.close()
