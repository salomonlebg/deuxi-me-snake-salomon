from tkinter import*

tk = Tk()
canvas = Canvas(tk,width = 600, height = 600 , bd=0, bg="darkblue")
canvas.pack(padx=10,pady=10)
#taille du canvas etc

serp1 = canvas.create_rectangle(0, 0, 50, 50,fill='red')
(serp1Left, serp1Top, serp1Right, serp1Bottom) = canvas.coords(serp1)



def deplacement():
    global dx,dy
    canvas.move(serp1,dx,dy)
    tk.after(20,deplacement)

def check_game_over():
    (serp1Left, serp1Top, serp1Right, serp1Bottom) = canvas.coords(serp1)
    if serp1Bottom > 600:
        close()
    elif serp1Top < 0:
        close()
    elif serp1Left < 0:
        close()
    elif serp1Right > 600:
        close()



def close():
    global windowOpen
    windowOpen = False
    window.destroy()



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


#position de la tête au début

dx=0
dy=0
#déplacement de la tête au début



canvas.bind_all('<Right>', droite)
canvas.bind_all('<Left>', gauche)
canvas.bind_all('<Up>', haut)
canvas.bind_all('<Down>', bas)

deplacement()




tk.mainloop()



