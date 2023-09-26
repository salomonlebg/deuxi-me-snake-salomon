from tkinter import*
import random

score = 0

# vitesse du sepend
speed=500

m = 50
n = 12

#x = [0,50,100,150,200,250,300,350,400,450,500,550,600]
x =  range(0,n*m,50)


dx = [m,m,m]
dy = [0,0,0]


#taille du canvas etc
tk = Tk()
canvas = Canvas(tk,width = 600, height = 600 , bd=0, bg="darkblue")
canvas.pack(padx=10,pady=10)


#position de la tête au début
Pos_X=x[5]
Pos_Y=x[9]

#déplacement de la tête au début
dx=x[1]
dy=x[0]

#position du prmier corps au début
Pos_X2=x[4]
Pos_Y2=x[9]

#déplacement du premier corps au début
dx2=x[1]
dy2=x[0]

#position du 2ieme corps au début
Pos_X3=x[3]
Pos_Y3=x[9]

#déplacement du 2ieme corps au début
dx3=x[1]
dy3=x[0]

#liste des rectangle du serpent
serp = [canvas.create_rectangle(Pos_X,Pos_Y,Pos_X+50,Pos_Y+50,fill='darkgreen'),
        canvas.create_rectangle(Pos_X2,Pos_Y2,Pos_X2+50,Pos_Y2+50,fill='green'),
        canvas.create_rectangle(Pos_X3,Pos_Y3,Pos_X3+50,Pos_Y3+50,fill='green')]

# détections si la tête touche le bord du canvas
# déplacement de la tête + des corps
# on vérifie les coordonées de la tête pour la collision
def deplacement():
    global dx,dy,dx2,dy2,dx3,dy3
    if canvas.coords(serp[0])[2]>600:
        close()
    elif canvas.coords(serp[0])[0]<0:
        close()
    elif canvas.coords(serp[0])[1]<0:
        close()
    elif canvas.coords(serp[0])[3]>600:
        close()
    else :
        canvas.move(serp[0],dx,dy)
        canvas.move(serp[1],dx2,dy2)
        canvas.move(serp[2],dx3,dy3)
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


# quand la tête touche la pomme
def collision():
    global pomme1
    global score
    if canvas.coords(serp[0]) == canvas.coords(pomme1):
        canvas.delete(pomme1)
        pomme1 = créer_pomme()
        score = score + 1

# actions des flèches directionelles         
def droite(event):
    global dx,dy
    dx=m
    dy=x[0]
#mouvement a droite
def gauche(event):
    global dx,dy
    dx=-m
    dy=x[0]
#mouvement a gauche
def haut(event):
    global dx,dy
    dx=x[0]
    dy=-m
#mouvement en haut
def bas(event):
    global dx,dy
    dx=x[0]
    dy=m
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



