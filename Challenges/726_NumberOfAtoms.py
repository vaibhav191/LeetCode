class Solution:
    def countOfAtoms(self, formula: str) -> str:
        deck = deque()
        r = '[A-Z][a-z]*[0-9]*|\(|\)|[0-9]+'
        exps = re.findall(r, formula)
        
        for exp in exps:
            if str.isdigit(exp):
                chems = []
                if deck[-1] == ')':
                    deck.pop()
                while deck[-1] != '(':
                    chems.append(deck.pop())
                if deck[-1] == '(':
                    deck.pop()

                r = '[0-9]+'
                for i in range(len(chems)):
                    c = chems[i]
                    digit = re.findall(r, c)
                    if len(digit):
                        # print(digit, c)
                        chems[i] = chems[i].replace(digit[0], str(int(digit[0])*int(exp)))
                    else:
                        chems[i] += exp
                deck += chems
            elif deck and deck[-1] == ')' and not str.isdigit(exp):
                deck.pop()
                chems = []
                while deck[-1] != '(':
                    chems.append(deck.pop())
                deck.pop()
                deck += chems
                deck.append(exp)
            else:
                deck.append(exp)
        if deck[-1] == ')':
            deck.pop()
            chems = []
            while deck[-1] != '(':
                chems.append(deck.pop())
            deck.pop()
            deck += chems
        ans = defaultdict(int)
        r_element = '[A-Z][a-z]*'
        r_digit = '[0-9]+'
        for exp in deck:
            element = re.findall(r_element, exp)[0]
            digit = re.findall(r_digit, exp)
            count = ans[element]
            # print(exp, element, digit)
            if len(digit):
                ans[element] = count + int(digit[0])
            else:
                ans[element] += 1
        keys_sorted = sorted(list(ans.keys()))
        s = ''
        for key in keys_sorted:
            s+=key
            s+=str(ans[key] if ans[key] > 1 else '')
        return s
