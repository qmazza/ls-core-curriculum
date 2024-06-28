def titlize(sentence):
    words = sentence.split()
    new_words = []

    for word in words:
        if len(word) > 2:
            word = word.capitalize()
        new_words.append(word) #Moved out of if block, to append even if not transformed.

    return ' '.join(new_words)

title = 'hello world of programming'
# print(titlize(title))
print(titlize(title))

print('======>')

#To begin, we remove print from code before testing

def titlize(sentence):
    words = sentence.split()
    #print(words)      ##tested first, works.
    new_words = []

    for word in words:
        #print(word) #test if loop is properly iterating second, works.
        if len(word) > 2:
            #print(word) #test words have length of more than 2 third, works.
            word.capitalize()
            #print(word) #error found here. String are immutable. Method call like word.capitalize() won't change value of word.
            #need to capture the return value and reassign word to that value
            new_words.append(word)

    return ' '.join(new_words) # connects the words back together into a single string, separated by spaces.

title = 'hello world of programming'
#print(titlize(title)) # 'hello world programming' lowercase and `of` removed.
titlize(title)
