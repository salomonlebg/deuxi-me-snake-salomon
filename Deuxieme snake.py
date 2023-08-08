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


serp1 = canvas.create_rectangle(Pos_X,Pos_Y,Pos_X+50,Pos_Y+50,fill='red')
#taille de la tête, couleur etc
serp2 = canvas.create_rectangle(Pos_X2,Pos_Y2,Pos_X2+50,Pos_Y2+50,fill='green')
#corps


score = 0


def deplacement():
    global dx,dy
    if canvas.coords(serp1)[2]>600:
        close()
    elif canvas.coords(serp1)[0]<0:
        close()
    elif canvas.coords(serp1)[1]<0:
        close()
    elif canvas.coords(serp1)[3]>600:
        close()
    canvas.move(serp1,dx,dy)
    tk.after(speed,deplacement)
 # si la tête touche le bord, le fenetre se ferme


def deplacement2():
    global dx2,dy2
    if canvas.coords(serp2)[1]== canvas.coords(serp1)[3]:
        dx2=0
        dy2=-50
    canvas.move(serp2,dx2,dy2)
    tk.after(speed,deplacement2)
#mouvement corps
   

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
deplacement2()


tk.mainloop()



