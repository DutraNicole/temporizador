import tkinter as Tkinter
from datetime import datetime, timezone
import datetime as dt

import tkinter as Tkinter
from datetime import datetime, timezone
import datetime as dt


# Colocando data e hora no cadastro
mes = dt.datetime.now().strftime("%m")
dia = dt.datetime.now().strftime("%d")

# Função para centralizar os widgets dentro da janela
def centralizar_widgets(root):
# Configurando as colunas para se expandirem uniformemente
    for i in range(3):
     root.grid_columnconfigure(i, weight=1)

def voltar_para_escolha(rootcr, root):
    bvoltar = Tkinter.Label(rootcr, text="voltar", font=("Helvetica", 12, "bold"), fg="#f9e653", bg="#a2d8f1", cursor="hand2")
    bvoltar.bind("<Button-1>", lambda e: [rootcr.withdraw(), root.deiconify])
    bvoltar.grid(row=5, column=0, columnspan=3, pady=(10, 10))

def Cronometro():
    global counter, running
    counter = 0
    running = False

    def counter_label(labelcr):
        def count():
            if running:
                global counter
                if counter == 0:
                    display = "iniciando..."
                else:
                    ttcr = datetime.fromtimestamp(counter, timezone.utc)
                    string = ttcr.strftime("%H:%M:%S")
                    display = string

                labelcr['text'] = display
                labelcr.after(1000, count)
                counter += 1
        count()

    def Start(labelcr):
        global running
        running = True
        counter_label(labelcr)
        startcr['state'] = 'disabled'
        stopcr['state'] = 'normal'
        resetcr['state'] = 'normal'

    def Stop():
        global running
        startcr['state'] = 'normal'
        stopcr['state'] = 'disabled'
        resetcr['state'] = 'normal'
        running = False

    def Reset(labelcr):
        global counter
        counter = 0
        if not running:
            resetcr['state'] = 'disabled'
            labelcr['text'] = 'Welcome!'
        else:
            labelcr['text'] = 'Starting...'

    rootcr = Tkinter.Toplevel()
    rootcr.title("Temporizador")
    rootcr.geometry("400x400")
    rootcr.configure(bg="#a2d8f1")

    labelcr = Tkinter.Label(rootcr, text="Iniciar!", bg="#a2d8f1", fg="#f9e653", font="Verdana 24 bold")
    labelcr.grid(row=0, column=0, columnspan=3, pady=20, sticky='n')

    fcr = Tkinter.Frame(rootcr, bg='#a2d8f1')
    fcr.grid(row=1, column=0, columnspan=3, pady=10)

    startcr = Tkinter.Button(fcr, text='Start', width=6, bg="lightgreen", command=lambda: Start(labelcr))
    stopcr = Tkinter.Button(fcr, text='Stop', font="Helvetica 12 bold", fg="#f9f58a", width=6, bg="#539aff", state='disabled', command=Stop)
    resetcr = Tkinter.Button(fcr, text='Reset', width=6, bg="lightgreen", state='disabled', command=lambda: Reset(labelcr))

    startcr.grid(row=0, column=0, padx=5)
    stopcr.grid(row=0, column=1, padx=5)
    resetcr.grid(row=0, column=2, padx=5)

    # Centralizando os widgets
    centralizar_widgets(rootcr)

    voltar_para_escolha(rootcr, root)
    rootcr.mainloop()

def Timer():
    global running, counter
    counter = 0
    running = False

    def counter_label(labelmr):
        def count():
            if running:
                global counter
                if counter <= 0:
                    display = "Fim..."
                else:
                    ttmr = datetime.fromtimestamp(counter, timezone.utc)
                    string = ttmr.strftime("%H:%M:%S")
                    display = string

                labelmr['text'] = display
                labelmr['bg'] = '#a2d8f1'
                labelmr['fg'] = 'yellow'
                labelmr.after(1000, count)
                counter -= 1

        count()

    def Start(labelmr):
        startmr.config(text='Start')
        global running, counter
        running = True

        time_str = entrymr.get()
        if time_str.isdigit():
            counter = int(time_str)
        else:
            labelmr['text'] = "Digite um número válido!"
            return

        counter_label(labelmr)
        startmr['state'] = 'disabled'
        stopmr['state'] = 'normal'
        resetmr['state'] = 'normal'

    def Stop():
        global running
        startmr.config(text="Run", command=lambda: Run(labelmr))
        startmr['state'] = 'normal'
        stopmr['state'] = 'disabled'
        resetmr['state'] = 'normal'
        running = False

    def Run(labelmr):
        global running
        running = True
        counter_label(labelmr)
        startmr['state'] = 'normal'
        stopmr['state'] = 'normal'
        resetmr['state'] = 'normal'
        startmr.config(text="Start", font=("helvetica", 10, "bold"), command=lambda: Start(labelmr))

    def Reset(labelmr):
        global counter
        time_str = entrymr.get()
        if time_str.isdigit():
            counter = int(time_str)
        else:
            labelmr['text'] = "Digite um número válido!"

        if not running:
            resetmr['state'] = 'disabled'
            labelmr['text'] = 'Welcome!'
        else:
            labelmr['text'] = 'Starting...'

    rootmr = Tkinter.Toplevel()
    rootmr.title("Timer")
    rootmr.geometry("400x400")
    rootmr.configure(bg="#a2d8f1")

    # Centralizando o label
    labelmr = Tkinter.Label(rootmr, text="Welcome!", bg='#a2d8f1', fg="yellow", font="Verdana 24 bold")
    labelmr.grid(row=0, column=0, columnspan=3, pady=20, sticky='nsew')

    # Centralizando o entry (sem sticky)
    entrymr = Tkinter.Entry(rootmr, width=10)
    entrymr.grid(row=1, column=0, columnspan=3, pady=10, sticky='n')

    # Frame para os botões
    fmr = Tkinter.Frame(rootmr, bg='#a2d8f1')
    fmr.grid(row=2, column=0, columnspan=3, pady=10)

    startmr = Tkinter.Button(fmr, text='Start', width=6, bg="lightgreen", command=lambda: Start(labelmr))
    stopmr = Tkinter.Button(fmr, text='Stop', width=6, bg="#539aff", fg="red", state='disabled', command=Stop)
    resetmr = Tkinter.Button(fmr, text='Reset', width=6, bg="lightgreen", state='disabled', command=lambda: Reset(labelmr))

    # Centralizando os botões no Frame
    startmr.grid(row=0, column=0, padx=2)
    stopmr.grid(row=0, column=1, padx=2)
    resetmr.grid(row=0, column=2, padx=2)

    # Centralizando a coluna e as linhas
    rootmr.grid_columnconfigure(0, weight=1)
    rootmr.grid_columnconfigure(1, weight=1)
    rootmr.grid_columnconfigure(2, weight=1)

    # Chama a função de voltar para escolha (caso exista)
    voltar_para_escolha(rootmr, root)
    rootmr.mainloop()


def temporizador(criar_janela_inicial):
  # O LOOP FUNCIONA MAS A JANELA NUNCA FECHA DE VDD
  global root
root = Tkinter.Tk()
root.title("Escolher")
root.geometry("400x400")
root.configure(bg="#a2d8f1")

# escrever na tela
label = Tkinter.Label(root, text="Faça sua escolha!", fg="#f9e653", bg="#a5d4f1", font="Helvetica 24 bold")
label.grid(row=0, column=0, pady=(20, 10), sticky='nsew')

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)  # Permite expansão da coluna 0

# botoes e suas configs
f = Tkinter.Frame(root, bg='#a2d8f1')
f.grid(row=1, column=0, pady=(10, 20), sticky='nsew')

cronometro = Tkinter.Button(f, text='Cronômetro', font=("Helvetica 12 bold"), bg="#5fa3f1", fg="#f9e653", width=15, height=1, command=Cronometro)
cronometro.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

timer = Tkinter.Button(f, text='Timer', font=("Helvetica 12 bold"), bg="#5fa3f1", fg="#f9e653", width=15, height=1, command=Timer)
timer.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

# Para que os botões tenham a mesma largura
f.grid_columnconfigure(0, weight=1)
f.grid_columnconfigure(1, weight=1)

root.mainloop()

criar.temporizador()

# Colocando data e hora no cadastro
mes = dt.datetime.now().strftime("%m")
dia = dt.datetime.now().strftime("%d")

# Função para centralizar os widgets dentro da janela
def centralizar_widgets(root):
# Configurando as colunas para se expandirem uniformemente
    for i in range(3):
     root.grid_columnconfigure(i, weight=1)

def voltar_para_escolha(rootcr, root):
    bvoltar = Tkinter.Label(rootcr, text="voltar", font=("Helvetica", 12, "bold"), fg="#f9e653", bg="#a2d8f1", cursor="hand2")
    bvoltar.bind("<Button-1>", lambda e: [rootcr.withdraw(), root.deiconify])
    bvoltar.grid(row=5, column=0, columnspan=3, pady=(10, 10))

def Cronometro():
    global counter, running
    counter = 0
    running = False

    def counter_label(labelcr):
        def count():
            if running:
                global counter
                if counter == 0:
                    display = "iniciando..."
                else:
                    ttcr = datetime.fromtimestamp(counter, timezone.utc)
                    string = ttcr.strftime("%H:%M:%S")
                    display = string

                labelcr['text'] = display
                labelcr.after(1000, count)
                counter += 1
        count()

    def Start(labelcr):
        global running
        running = True
        counter_label(labelcr)
        startcr['state'] = 'disabled'
        stopcr['state'] = 'normal'
        resetcr['state'] = 'normal'

    def Stop():
        global running
        startcr['state'] = 'normal'
        stopcr['state'] = 'disabled'
        resetcr['state'] = 'normal'
        running = False

    def Reset(labelcr):
        global counter
        counter = 0
        if not running:
            resetcr['state'] = 'disabled'
            labelcr['text'] = 'Welcome!'
        else:
            labelcr['text'] = 'Starting...'

    rootcr = Tkinter.Toplevel()
    rootcr.title("Temporizador")
    rootcr.geometry("400x400")
    rootcr.configure(bg="#a2d8f1")

    labelcr = Tkinter.Label(rootcr, text="Iniciar!", bg="#a2d8f1", fg="#f9e653", font="Verdana 24 bold")
    labelcr.grid(row=0, column=0, columnspan=3, pady=20, sticky='n')

    fcr = Tkinter.Frame(rootcr, bg='#a2d8f1')
    fcr.grid(row=1, column=0, columnspan=3, pady=10)

    startcr = Tkinter.Button(fcr, text='Start', width=6, bg="lightgreen", command=lambda: Start(labelcr))
    stopcr = Tkinter.Button(fcr, text='Stop', font="Helvetica 12 bold", fg="#f9f58a", width=6, bg="#539aff", state='disabled', command=Stop)
    resetcr = Tkinter.Button(fcr, text='Reset', width=6, bg="lightgreen", state='disabled', command=lambda: Reset(labelcr))

    startcr.grid(row=0, column=0, padx=5)
    stopcr.grid(row=0, column=1, padx=5)
    resetcr.grid(row=0, column=2, padx=5)

    # Centralizando os widgets
    centralizar_widgets(rootcr)

    voltar_para_escolha(rootcr, root)
    rootcr.mainloop()

def Timer():
    global running, counter
    counter = 0
    running = False

    def counter_label(labelmr):
        def count():
            if running:
                global counter
                if counter <= 0:
                    display = "Fim..."
                else:
                    ttmr = datetime.fromtimestamp(counter, timezone.utc)
                    string = ttmr.strftime("%H:%M:%S")
                    display = string

                labelmr['text'] = display
                labelmr['bg'] = 'lightblue'
                labelmr['fg'] = 'green'
                labelmr.after(1000, count)
                counter -= 1

        count()

    def Start(labelmr):
        startmr.config(text='Start')
        global running, counter
        running = True

        time_str = entrymr.get()
        if time_str.isdigit():
            counter = int(time_str)
        else:
            labelmr['text'] = "Digite um número válido!"
            return

        counter_label(labelmr)
        startmr['state'] = 'disabled'
        stopmr['state'] = 'normal'
        resetmr['state'] = 'normal'

    def Stop():
        global running
        startmr.config(text="Run", command=lambda: Run(labelmr))
        startmr['state'] = 'normal'
        stopmr['state'] = 'disabled'
        resetmr['state'] = 'normal'
        running = False

    def Run(labelmr):
        global running
        running = True
        counter_label(labelmr)
        startmr['state'] = 'normal'
        stopmr['state'] = 'normal'
        resetmr['state'] = 'normal'
        startmr.config(text="Start", command=lambda: Start(labelmr))

    def Reset(labelmr):
        global counter
        time_str = entrymr.get()
        if time_str.isdigit():
            counter = int(time_str)
        else:
            labelmr['text'] = "Digite um número válido!"

        if not running:
            resetmr['state'] = 'disabled'
            labelmr['text'] = 'Welcome!'
        else:
            labelmr['text'] = 'Starting...'

    rootmr = Tkinter.Toplevel()
    rootmr.title("Timer")
    rootmr.geometry("400x400")
    rootmr.configure(bg="#a2d8f1")

    labelmr = Tkinter.Label(rootmr, text="Welcome!", bg='lightblue', fg="green", font="Verdana 24 bold")
    labelmr.grid(row=0, column=0, columnspan=3, pady=20, sticky='n')

    entrymr = Tkinter.Entry(rootmr, width=10)
    entrymr.grid(row=1, column=0, columnspan=3, pady=10, sticky='n')

    fmr = Tkinter.Frame(rootmr, bg='#a2d8f1')
    fmr.grid(row=2, column=0, columnspan=3, pady=10)

    startmr = Tkinter.Button(fmr, text='Start', width=6, bg="lightgreen", command=lambda: Start(labelmr))
    stopmr = Tkinter.Button(fmr, text='Stop', width=6, bg="#539aff", fg="red", state='disabled', command=Stop)
    resetmr = Tkinter.Button(fmr, text='Reset', width=6, bg="lightgreen", state='disabled', command=lambda: Reset(labelmr))

    startmr.grid(row=0, column=0, padx=5)
    stopmr.grid(row=0, column=1, padx=5)
    resetmr.grid(row=0, column=2, padx=5)

    voltar_para_escolha(rootmr, root)
    rootmr.mainloop()

def temporizador(janela_inicial):
  # O LOOP FUNCIONA MAS A JANELA NUNCA FECHA DE VDD
  global root
root = Tkinter.Tk()
root.title("Escolher")
root.geometry("400x400")
root.configure(bg="#a2d8f1")

# escrever na tela
label = Tkinter.Label(root, text="Faça sua escolha!", fg="#f9e653", bg="#a5d4f1", font="Helvetica 24 bold")
label.grid(row=0, column=0, pady=(20, 10), sticky='nsew')

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)  # Permite expansão da coluna 0

# botoes e suas configs
f = Tkinter.Frame(root, bg='#a2d8f1')
f.grid(row=1, column=0, pady=(10, 20), sticky='nsew')

cronometro = Tkinter.Button(f, text='Cronômetro', font=("Helvetica 12 bold"), bg="#5fa3f1", fg="#f9e653", width=15, height=1, command=Cronometro)
cronometro.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

timer = Tkinter.Button(f, text='Timer', font=("Helvetica 12 bold"), bg="#5fa3f1", fg="#f9e653", width=15, height=1, command=Timer)
timer.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

# Para que os botões tenham a mesma largura
f.grid_columnconfigure(0, weight=1)
f.grid_columnconfigure(1, weight=1)

root.mainloop()

criar.temporizador()
