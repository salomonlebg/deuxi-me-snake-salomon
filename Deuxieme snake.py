from tkinter import*
import random

score = 0

# vitesse du serpent, le serpent bouge toute les speed mili secondes
speed=300

# taille d'un carré
tc = 50

# pixel parcouru par tick
v = 50

# nombre de carrés sur un axe
nc = 12

# liste des directions de chaque carrés, dx = direction horizontal, dy = direction vertical
dx = [v,v,v]
dy = [0,0,0]


# taille du canvas et largeur de la bordure 
tk = Tk()
canvas = Canvas(tk,width = nc*tc, height = nc*tc , bd=0, bg="darkblue")
canvas.pack(padx=10,pady=10)



# position de la tête au début
Pos_X=5*tc
Pos_Y=9*tc


# liste des rectangle du serpent
serp = [canvas.create_rectangle(Pos_X,Pos_Y,Pos_X+tc,Pos_Y+tc,fill='darkgreen'),
        canvas.create_rectangle(Pos_X-tc,Pos_Y,Pos_X,Pos_Y+tc,fill='green'),
        canvas.create_rectangle(Pos_X-2*tc,Pos_Y,Pos_X-tc,Pos_Y+tc,fill='green')]



# détections si la tête touche le bord du canvas
# cg,ch,cd,cb = côté gauche, côté du haut, côté droite, côté du bas
def deplacement():
    global dx,dy
    global pomme1
    cg,ch,cd,cb = canvas.coords(serp[0])
    if cg<0:
        close()
    elif ch<0:
        close()
    elif cd>nc*tc :
        close()
    elif cb>nc*tc:
        close()
# déplacement de la tête + des corps
    else :
        for k in range(0,len(dx)):
            canvas.move(serp[k],dx[k],dy[k])
# chaque corps prend le la direction de celui avant lui
        for k in range(len(dx)-1,0,-1):
            dx[k] = dx[k-1]
            dy[k] = dy[k-1]
# si le serpent est autant grand que le canvas le joueur a gagné
        if len(serp) == nc*nc :
                victoire()
        collision()
# si une pomme apparaît sur le corps du serpent, on en créer une nouvelle
        for p in range(len(dx)-1,0,-1):
            if canvas.coords(serp[p]) == canvas.coords(pomme1):
                canvas.delete(pomme1)
                pomme1 = créer_pomme()
# si la tête touche le corps du serpent, le jeu se termine 
        for i in range(len(dx)-1,0,-1):
            if canvas.coords(serp[0]) == canvas.coords(serp[i]):
                close()
        tk.after(speed,deplacement)




#coordonnés possibles de la pomme
cp = range(0,tc*nc-tc,tc)


#création de la pomme sans la faire apparaître
def créer_pomme():
    x = random.choice(cp)
    y = random.choice(cp)
    p = canvas.create_rectangle(x,y,x+tc,y+tc,fill='red')
    return(p)


pomme1 = créer_pomme()



# collision de la pomme et du serpent
def collision():
    global pomme1
    global score
    c1,c2,c3,c4 = canvas.coords(serp[-1])
    if canvas.coords(serp[0]) == canvas.coords(pomme1):
# supression de la pomme, apparition d'une nouvelle pomme et le score augmente de 1
            canvas.delete(pomme1)
            pomme1 = créer_pomme()
            serp.append(canvas.create_rectangle(c1-dx[-1],c2-dy[-1],c3-dx[-1],c4-dy[-1],fill="green"))
            dx.append(dx[-1])
            dy.append(dy[-1])
            score = score + 1
            

# actions des flèches directionelles         
def droite(event):
    global dx,dy
    dx[0]=v
    dy[0]=0
#mouvement a droite
def gauche(event):
    global dx,dy
    dx[0]=-v
    dy[0]=0
#mouvement a gauche
def haut(event):
    global dx,dy
    dx[0]=0
    dy[0]=-v
#mouvement en haut
def bas(event):
    global dx,dy
    dx[0]=0
    dy[0]=v
#mouvement en bas


# ce qu'il se passe quand la tête touche le bord
def close():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,
                       canvas.winfo_height()/2,
                       font=('consolas', 45),
                       text="PARTIE TERMINÉE !", fill="red")
    canvas.create_text(canvas.winfo_width()/2,
                       canvas.winfo_height()/1.5,
                       font=('consolas', 20),
                       text="Bravo! tu as mangé " + str(score)+" pommes ", fill="red")


# ce qu'il se passe quand le serpent mange toutes les pommes
def victoire():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,
                       canvas.winfo_height()/2,
                       font=('consolas', 35),
                       text="BRAVO TU AS GAGNÉ,E !", fill="red")
    canvas.create_text(canvas.winfo_width()/2,
                       canvas.winfo_height()/1.5,
                       font=('consolas', 20),
                       text="Tu as mangé toutes les pommes", fill="red")


                       
#binding des flèches du clavier
canvas.bind_all('<Right>', droite)
canvas.bind_all('<Left>', gauche)
canvas.bind_all('<Up>', haut)
canvas.bind_all('<Down>', bas)

deplacement()

tk.mainloop()



