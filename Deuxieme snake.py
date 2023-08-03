from tkinter import*
import random

tk = Tk()
canvas = Canvas(tk,width = 599, height = 599 , bd=0, bg="darkblue")
canvas.pack(padx=10,pady=10)
#taille du canvas etc

Pos_X=250
Pos_Y=450
#position de la tête au début

dx=50
dy=0
#déplacement de la tête au début

serp1 = canvas.create_rectangle(Pos_X,Pos_Y,Pos_X+50,Pos_Y+50,fill='red')
#taille de la tête, couleur etc

score = 0

def deplacement():
    global dx,dy
    if canvas.coords(serp1)[2]>599:
        close()
    elif canvas.coords(serp1)[0]<1:
        close()
    elif canvas.coords(serp1)[1]<1:
        close()
    elif canvas.coords(serp1)[3]>599:
        close()
    canvas.move(serp1,dx,dy)
    tk.after(235,deplacement)


      
def close():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,
                       canvas.winfo_height()/2,
                       font=('consolas', 45),
                       text="PARTIE TERMINÉE !", fill="red")
                       
    print(" Tu as mangé " + str(score)+" pommes ")
   
# si la tête touche le bord, le fenetre se ferme

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


canvas.bind_all('<Right>', droite)
canvas.bind_all('<Left>', gauche)
canvas.bind_all('<Up>', haut)
canvas.bind_all('<Down>', bas)
#binding des flèches du clavier

deplacement()

tk.mainloop()



