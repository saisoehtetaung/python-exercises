
def lyrics_to_frequences(lyrics):
        myDict=dict()
        for word in lyrics:
            if word in myDict:
                myDict[word]+=1
            else:
                myDict[word]=1
        return myDict

def most_common_words(freqs):
        values=freqs.values()
        best=max(values)
        word=list()
        for k in freqs:
            if freqs[k]==best:
                word.append(k)
        return (word,best)

def words_often(freqs,minTimes):
        result=list()
        done=False
        while not done:
            temp=most_common_words(freqs)
            if temp[1]>=minTimes:
                result.append(temp)
                for w in temp[0]:
                    del(freqs[w])
            else:
                done=True
        return result


lyrics="when your legs don't work like they used to before and I can't sweep you off of your feet will your mouth still remember the taste of my love"
lyricsList=lyrics.split()
freqs=lyrics_to_frequences(lyricsList)
print(freqs)
print(most_common_words(freqs))
print(words_often(freqs,2))
print(freqs)