class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n=len(box)
        for i in range(n):
            row=(''.join(box[i])).split('*')
            row=[''.join(sorted(x,reverse=True)) for x in row]
            box[i]=list('*'.join(row))
        box=list(zip(*box[::-1]))
        return box