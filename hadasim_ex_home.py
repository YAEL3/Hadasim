
def ex_file(str):
    count_lines=0
    count_words=0
    colors=['red','yellow','blue','green','orange','purple','pink','black','white','grey','brown']
    Syntax_words=['i','am','is','are','a','d\'ont','but','do','does','as','in','and','with','the','that','there','of','they']
    x=[]
    y=[]
    list=[]  
    dic_words={}
    dic_colors={}
    max=0
    with open(str,'r',encoding="unicode_escape") as open_file:
        #print(open_file.read())
        x=open_file.readlines()
        for word in colors:
            dic_colors[word]=0
        for item in x:
            y=item.split()
            if len(y)>max:
                max=len(y)
            for word in y:
                count_words+=1
                list.append(word)
                dic_words[word]=0
                if word.lower() in colors:
                     dic_colors[word]=dic_colors[word]+1
            y=[]
            count_lines+=1 
        i=1
        count_one_words=len(dic_words.keys()) 
        for word in list:
            if dic_words[word]==1:
                count_one_words-=1
            dic_words[word]=dic_words[word]+1  
        max_key=''
        max_value=0
        max_key2=''
        max_value2=0
        for (key, value) in dic_words.items():#בדיקת המילה הפופולארית ביותר
            if (key.lower() not in Syntax_words) and value>max_value2:
                    max_key2=key
                    max_value2=value
            if value > max_value:
                max_value=value
                max_key=key
        for (key, value) in dic_colors.items():
            if value>0:
                print("color",key ,"appear ",value, "times")
    print(dic_words)
    print(count_lines)
    print(count_words)
    print(count_one_words)
    print("avarage is:" ,count_words/count_lines)
    print("max:", max)
    print("the populer word is:", max_key)
    print("the populer word (not syntask) is:", max_key2)

ex_file('another_file.txt')

