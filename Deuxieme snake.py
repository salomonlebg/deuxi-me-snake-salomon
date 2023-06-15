from tkinter import*

tk = Tk()
canvas = Canvas(tk,width = 600, height = 600 , bd=0, bg="darkblue")
canvas.pack(padx=10,pady=10)
#taille du canvas etc

Pos_X=275
Pos_Y=450
#position de la tête au début

dx=0
dy=0
#déplacement de la tête au début

serp1 = canvas.create_rectangle(Pos_X,Pos_Y,Pos_X+50,Pos_Y+50,fill='red')
#taille de la tête, couleur etc

def deplacement():
    global dx,dy
    if canvas.coords(serp1)[3]>600:
        close()
    elif canvas.coords(serp1)[0]<0:
        close()
    elif canvas.coords(serp1)[1]<0:
        close()
    elif canvas.coords(serp1)[2]>600:
        close()
    canvas.move(serp1,dx,dy)
    tk.after(20,deplacement)

   
def close():
    tk.destroy()
# si la tête touche le bord, le fenetre se ferme



def droite(event):
    global dx,dy
    dx=5
    dy=0
#mouvement a droite
def gauche(event):
    global dx,dy
    dx=-5
    dy=0
#mouvement a gauche
def haut(event):
    global dx,dy
    dx=0
    dy=-5
#mouvement en haut
def bas(event):
    global dx,dy
    dx=0
    dy=5
#mouvement en bas    


canvas.bind_all('<Right>', droite)
canvas.bind_all('<Left>', gauche)
canvas.bind_all('<Up>', haut)
canvas.bind_all('<Down>', bas)
#binding des flèches du clavier


deplacement()

tk.mainloop()



