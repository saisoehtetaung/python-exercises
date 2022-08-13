from random import randint;

words= ["apple","orange","lemon","pineapple","dragon-fruit"]; 

def randomSentance(word):
    randomidx= randint(0,len(words)-1);
    return f"{word} {words[randomidx]}";

with open("text.txt","r") as aa:
    paragraph= aa.read();
    wordList=paragraph.split();

    sentancelist= list(map(randomSentance, wordList));

    numph = int(input("Enter How Many Paragraph You Want: "));
    with open("general.txt","w") as write_file:
        for count in range(numph):
           write_file.write(''.join(sentancelist)+'\n\n');
