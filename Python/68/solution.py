class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        currentWidth = 0
        rows = []
        currentWords = []
        numberOfWords = 0
        for word in words:
            if len(word) + currentWidth + len(currentWords) <= maxWidth:
                currentWords.append(word)
                currentWidth += len(word)
                numberOfWords += 1
            else:
                totalSpaces = padWidth = maxWidth - currentWidth
                extraSpaces = 0
                row = ""
                if numberOfWords == 1:
                    row += currentWords[0] + " " * padWidth
                else:
                    padWidth = totalSpaces // (numberOfWords - 1)
                    extraSpaces = totalSpaces % (numberOfWords - 1)
                    for i in range(numberOfWords - 1):
                        row += currentWords[i] + " " * padWidth
                        if extraSpaces > 0:
                            row += " "
                            extraSpaces -= 1
                    row += currentWords[-1]
                print(len(row))
                rows.append(row)

                #reinit
                currentWords = [word]
                currentWidth = len(word)
                numberOfWords = 1
        #last line
        row = " ".join(currentWords)
        row += " " * (maxWidth - len(row))
        rows.append(row)
        return rows