from urllib.request import urlretrieve;

link = input("image download link: ");
filename= input("filename: ");

urlretrieve(link ,"image/"+filename+".png");