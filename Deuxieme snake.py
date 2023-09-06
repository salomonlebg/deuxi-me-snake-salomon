from tkinter import*
import random

speed=500

tk = Tk()
canvas = Canvas(tk,width = 600, height = 600 , bd=0, bg="darkblue")
canvas.pack(padx=10,pady=10)
#taille du canvas etc

Pos_X=250
Pos_Y=450
#position de la tête au début

dx=50
dy=0
#déplacement de la tête au début

Pos_X2=200
Pos_Y2=450

dx2=50
dy2=0

Pos_X3=150
Pos_Y3=450

dx3=50
dy3=0


serp1 = canvas.create_rectangle(Pos_X,Pos_Y,Pos_X+50,Pos_Y+50,fill='dark green')
#taille de la tête, couleur etc
serp2 = canvas.create_rectangle(Pos_X2,Pos_Y2,Pos_X2+50,Pos_Y2+50,fill='green')
#corps
serp3 = canvas.create_rectangle(Pos_X3,Pos_Y3,Pos_X3+50,Pos_Y3+50,fill='green')


score = 0


def deplacement():
    global dx,dy,dx2,dy2,dx3,dy3
    if canvas.coords(serp1)[2]>600:
        close()
    elif canvas.coords(serp1)[0]<0:
        close()
    elif canvas.coords(serp1)[1]<0:
        close()
    elif canvas.coords(serp1)[3]>600:
        close()
    canvas.move(serp1,dx,dy)
    canvas.move(serp2,dx2,dy2)
    canvas.move(serp3,dx3,dy3)
    dx3=dx2
    dy3=dy2
    dx2=dx
    dy2=dy
    tk.after(speed,deplacement)
 # si la tête touche le bord, le fenetre se ferme

ma_liste = [0,50,100,150,200,250,300,350,400,450,500,550]

def créer_pomme():
    x = random.choice(ma_liste)
    y = random.choice(ma_liste)
    canvas.create_rectangle(x,y,x+50,y+50,fill='red')
    return (x,y)


   
def droite(event):
    global dx,dy
    dx=50
    dy=0
#mouvement a droite
def gauche(event):
    global dx,dy
    dx=-50
    dy=0
#mouvement a gauche
def haut(event):
    global dx,dy
    dx=0
    dy=-50
#mouvement en haut
def bas(event):
    global dx,dy
    dx=0
    dy=50
#mouvement en bas




def close():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,
                       canvas.winfo_height()/2,
                       font=('consolas', 45),
                       text="PARTIE TERMINÉE !", fill="red")
                       
    print(" Tu as mangé " + str(score)+" pommes ")



canvas.bind_all('<Right>', droite)
canvas.bind_all('<Left>', gauche)
canvas.bind_all('<Up>', haut)
canvas.bind_all('<Down>', bas)
#binding des flèches du clavier

deplacement()
créer_pomme()


tk.mainloop()



