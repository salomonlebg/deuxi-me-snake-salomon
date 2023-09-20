from tkinter import*
import random

# vitesse du sepend
speed=500


x = [-50,0,50,100,150,200,250,300,350,400,450,500,550,600]

#taille du canvas etc
tk = Tk()
canvas = Canvas(tk,width = 600, height = 600 , bd=0, bg="darkblue")
canvas.pack(padx=10,pady=10)


#position de la tête au début
Pos_X=x[6]
Pos_Y=x[10]

#déplacement de la tête au début
dx=x[2]
dy=x[1]

#position du prmier corps au début
Pos_X2=x[5]
Pos_Y2=x[10]

#déplacement du premier corps au début
dx2=x[2]
dy2=x[1]

#position du 2ieme corps au début
Pos_X3=x[4]
Pos_Y3=x[10]

#déplacement du 2ieme corps au début
dx3=x[2]
dy3=x[1]

#liste des rectangle du serpent
serp = [canvas.create_rectangle(Pos_X,Pos_Y,Pos_X+50,Pos_Y+50,fill='darkgreen'),canvas.create_rectangle(Pos_X2,Pos_Y2,Pos_X2+50,Pos_Y2+50,fill='green'),canvas.create_rectangle(Pos_X3,Pos_Y3,Pos_X3+50,Pos_Y3+50,fill='green')]


score = 0


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
    canvas.move(serp[0],dx,dy)
    canvas.move(serp[1],dx2,dy2)
    canvas.move(serp[2],dx3,dy3)
    dx3=dx2
    dy3=dy2
    dx2=dx
    dy2=dy
    collision()
    tk.after(speed,deplacement)
 # si la tête touche le bord, le fenetre se ferme


# quand la tête touche la pomme
def collision():
    if canvas.coords(serp[0]) == canvas.coords(pomme1):
        canvas.delete(pomme1)
        créer_pomme()


# création de la pomme
ma_liste = [0,50,100,150,200,250,300,350,400,450,500,550]
def créer_pomme():
    x = random.choice(ma_liste)
    y = random.choice(ma_liste)
    p = canvas.create_rectangle(x,y,x+50,y+50,fill='red')
    return(p)

pomme1 = créer_pomme()


# actions des flèches directionelles         
def droite(event):
    global dx,dy
    dx=x[2]
    dy=x[1]
#mouvement a droite
def gauche(event):
    global dx,dy
    dx=x[0]
    dy=x[1]
#mouvement a gauche
def haut(event):
    global dx,dy
    dx=x[1]
    dy=x[0]
#mouvement en haut
def bas(event):
    global dx,dy
    dx=x[1]
    dy=x[2]
#mouvement en bas



# ce qu'il se passe quand la tête touche le bord
def close():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,
                       canvas.winfo_height()/2,
                       font=('consolas', 45),
                       text="PARTIE TERMINÉE !", fill="red")
                       
    print(" Tu as mangé " + str(score)+" pommes ")



#binding des flèches du clavier
canvas.bind_all('<Right>', droite)
canvas.bind_all('<Left>', gauche)
canvas.bind_all('<Up>', haut)
canvas.bind_all('<Down>', bas)

deplacement()

tk.mainloop()



