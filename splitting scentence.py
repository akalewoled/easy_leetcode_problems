class Solution:
    def sortSentence(self, s: str) -> str:
        word=so
        
        splitted = word.split(" ")
        length =len(splitted)
        output=['']*10;
        for i in splitted:
            num =int(i[-1])
            i=i.replace(i[-1],"")
            output[num]=i

        output1 = [x for x in output if x != '']
        output2=" ".join(output1)
        return output2
