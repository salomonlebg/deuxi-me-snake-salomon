from tkinter import*
import random

score = 0

# vitesse du serpent
speed=300

#taille d'un carré
tc = 50

#vitesse d'un carré
v = 50

#nombre de carrés
nc = 12

# liste des directions de chaque carrés
dx = [v,v,v]
dy = [0,0,0]


#taille du canvas etc
tk = Tk()
canvas = Canvas(tk,width = nc*tc, height = nc*tc , bd=0, bg="darkblue")
canvas.pack(padx=10,pady=10)


#position de la tête au début
Pos_X=5*tc
Pos_Y=9*tc


#liste des rectangle du serpent
serp = [canvas.create_rectangle(Pos_X,Pos_Y,Pos_X+tc,Pos_Y+tc,fill='darkgreen'),
        canvas.create_rectangle(Pos_X-tc,Pos_Y,Pos_X,Pos_Y+tc,fill='green'),
        canvas.create_rectangle(Pos_X-2*tc,Pos_Y,Pos_X-tc,Pos_Y+tc,fill='green')]

# détections si la tête touche le bord du canvas
# déplacement de la tête + des corps
# on vérifie les coordonées de la tête pour la collision avec la pomme et le corps 
def deplacement():
    global dx,dy
    if canvas.coords(serp[0])[2]>nc*tc:
        close()
    elif canvas.coords(serp[0])[0]<0:
        close()
    elif canvas.coords(serp[0])[1]<0:
        close()
    elif canvas.coords(serp[0])[3]>nc*tc:
        close()
    else :
        for k in range(0,len(dx)):
            canvas.move(serp[k],dx[k],dy[k])
        for k in range(len(dx)-1,0,-1):
            dx[k] = dx[k-1]
            dy[k] = dy[k-1]
        collision()
        for i in range(len(dx)-1,0,-1):
            if canvas.coords(serp[0]) == canvas.coords(serp[i]):
                close()
        tk.after(speed,deplacement)

#coordonnés possibles de la pomme
cp = [0,50,100,150,200,250,300,350,400,450,500,550]

#création de la pomme sans la faire apparaître
def créer_pomme():
    x = random.choice(cp)
    y = random.choice(cp)
    p = canvas.create_rectangle(x,y,x+50,y+50,fill='red')
    return(p)

pomme1 = créer_pomme()

# collision de la pomme et du serpent
# apparition d'une nouvelle pomme
# si la pomme apparait sur le corps du serpent, on en créer une nouvelle
def collision():
    global pomme1
    global score
    c1,c2,c3,c4 = canvas.coords(serp[-1])
    for p in range(len(dx)-1,0,-1):
        if canvas.coords(serp[p]) == canvas.coords(pomme1):
                canvas.delete(pomme1)
                pomme1 = créer_pomme()
        elif canvas.coords(serp[0]) == canvas.coords(pomme1):
            canvas.delete(pomme1)
            pomme1 = créer_pomme()
            score = score + 1
            serp.append(canvas.create_rectangle(c1-dx[-1],c2-dy[-1],c3-dx[-1],c4-dy[-1],fill="green"))
            dx.append(dx[-1])
            dy.append(dy[-1])
            if len(serp)-1 == 144:
                victoire()
            

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
                       font=('consolas', 40),
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



