from tkinter import*
import random

score = 0

# vitesse du sepend
speed=500

m = 50
n = 12

#x = [0,50,100,150,200,250,300,350,400,450,500,550,600]
x =  range(0,n*m,m)


dx = [m,m,m]
dy = [0,0,0]


#taille du canvas etc
tk = Tk()
canvas = Canvas(tk,width = 600, height = 600 , bd=0, bg="darkblue")
canvas.pack(padx=10,pady=10)


#position de la tête au début
Pos_X=x[5]
Pos_Y=x[9]


#liste des rectangle du serpent
serp = [canvas.create_rectangle(Pos_X,Pos_Y,Pos_X+m,Pos_Y+m,fill='darkgreen'),
        canvas.create_rectangle(Pos_X-m,Pos_Y,Pos_X,Pos_Y+m,fill='green'),
        canvas.create_rectangle(Pos_X-2*m,Pos_Y,Pos_X-m,Pos_Y+m,fill='green')]

# détections si la tête touche le bord du canvas
# déplacement de la tête + des corps
# on vérifie les coordonées de la tête pour la collision
def deplacement():
    global dx,dy
    if canvas.coords(serp[0])[2]>600:
        close()
    elif canvas.coords(serp[0])[0]<0:
        close()
    elif canvas.coords(serp[0])[1]<0:
        close()
    elif canvas.coords(serp[0])[3]>600:
        close()
    else :
        for k in range(0,len(dx)):
            canvas.move(serp[k],dx[k],dy[k])
        for k in range(len(dx)-1,0,-1):
            dx[k] = dx[k-1]
            dy[k] = dy[k-1]
        collision()
        tk.after(speed,deplacement)
 # si la tête touche le bord, le fenetre se ferme

ma_liste = [0,50,100,150,200,250,300,350,400,450,500,550]
def créer_pomme():
    x = random.choice(ma_liste)
    y = random.choice(ma_liste)
    p = canvas.create_rectangle(x,y,x+50,y+50,fill='red')
    return(p)

pomme1 = créer_pomme()


c1,c2,c3,c4 = canvas.coords(serp[-1])

# quand la tête touche la pomme
def collision():
    global pomme1
    global score
    if canvas.coords(serp[0]) == canvas.coords(pomme1):
        canvas.delete(pomme1)
        pomme1 = créer_pomme()
        score = score + 1
        serp.append(canvas.create_rectangle(c1-dx[-1],c2-dy[-1],c3-dx[-1],c4-dy[-1],fill="green"))
        dx.append(dx[-1])
        dy.append(dx[-1])
        

# actions des flèches directionelles         
def droite(event):
    global dx,dy
    dx[0]=x[1]
    dy[0]=x[0]
#mouvement a droite
def gauche(event):
    global dx,dy
    dx[0]=-m
    dy[0]=x[0]
#mouvement a gauche
def haut(event):
    global dx,dy
    dx[0]=x[0]
    dy[0]=-m
#mouvement en haut
def bas(event):
    global dx,dy
    dx[0]=x[0]
    dy[0]=x[1]
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
    
                       
#binding des flèches du clavier
canvas.bind_all('<Right>', droite)
canvas.bind_all('<Left>', gauche)
canvas.bind_all('<Up>', haut)
canvas.bind_all('<Down>', bas)

deplacement()

tk.mainloop()



