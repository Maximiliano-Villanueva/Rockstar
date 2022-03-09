def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
    
    result = list()
    for a in words1:
        should_append=True
        for b in words2:
            tmp = a
            or_lenght = len(tmp)
            
            for letter in b:
                if letter in tmp:
                    tmp = tmp.lstrip(letter)
                    if len(tmp) == or_lenght:
                        should_append=False
                        break
                else:
                    should_append=False
                    break
        if should_append:
            result.append(a)
    return result

print(wordSubsets(["amazon","apple","facebook","google","leetcode"], ['e', 'o']))