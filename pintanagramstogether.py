def anagrams(words,n):
    '''
    words: list of word
    n:      no of words
    return : list of group of anagram {list will be sorted in driver code (not word in grp)}
    '''
    
    #code here
    def check_anagram(word1, word2):
        if len(word1) != len(word2):
            return False
        for letter in word1:
            if letter in word2 and word1.count(letter) == word2.count(letter):
                    continue
            else:
                return False
        return True
    
    return_list = [[words[0]]]
    i = 1
    #while(i<=n):
    for word in words[1:]:
        for it in return_list:
            #print(it[0],word)
            if check_anagram(word, it[0]):
                #print('hello')
                it.append(word)
                break
        else:
            return_list.append([word])
    
    return return_list

if __name__ == '__main__':
	result = anagrams(['sff', 'sfd', 'dfs'], 3)
	print(result)