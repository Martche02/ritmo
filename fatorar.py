import pickle
from definicoes import TreeNode, TernaryTree, ts
with open('ternary_tree.pkl', 'rb') as file:
    tree = pickle.load(file)

musica = "01221221221221221221221220122122122122012212212212201221221221221221221221221220122"
fatoracoes=[]
def a(music_l:str, carry:list=[], back:list=[])->None:
    if music_l == '':
        fatoracoes.append(back)
    else:
        c = carry.copy()
        c.append(music_l[0])
        if tree.search(ts(''.join([item[0] for item in c]), c[0])):
            a(music_l[1:], c, back)
        back.append(carry)
        a(music_l[1:], [music_l[0]], back)
a(musica)
print(len(fatoracoes))