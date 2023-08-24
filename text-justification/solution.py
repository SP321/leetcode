class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0

        for word in words:
            if len(cur) + num_of_letters + len(word) > maxWidth:
                if len(cur) == 1:
                    res.append(cur[0] + ' ' * (maxWidth - num_of_letters))
                else:
                    num_spaces = (maxWidth - num_of_letters) // (len(cur) - 1)
                    extra_spaces = (maxWidth - num_of_letters) % (len(cur) - 1)
                    for i in range(extra_spaces):
                        cur[i] += ' '
                    res.append((' ' * num_spaces).join(cur))
                cur, num_of_letters = [], 0
            cur += [word]
            num_of_letters += len(word)

        res.append(' '.join(cur) + ' ' * (maxWidth - num_of_letters - len(cur) + 1))
        return res