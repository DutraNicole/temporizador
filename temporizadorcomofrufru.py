def criar_janela_temporizador():

    global root
    root = tk.Tk()
    root.title("Escolher")
    root.geometry("400x400")
    root.configure(bg="#a2d8f1")

    frame_central = tk.Frame(root, bg='#a2d8f1')
    frame_central.pack(expand=True, fill='both')

    quadro_fundo = tk.Frame(frame_central, bg='#90c7e8', padx=20, pady=20)  # Adiciona preenchimento interno (padding)
    quadro_fundo.pack(expand=True)

    frame_interno = tk.Frame(quadro_fundo, bg='#90c7e8')
    frame_interno.pack(expand=True)

    # escrever na tela
    label = tk.Label(frame_interno, text="Faça sua escolha!", fg="#f9e653", bg="#90c7e8", font="Helvetica 24 bold")
    label.grid(row=0, column=0, pady=(20, 10), sticky='nsew')

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=0)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)  # Permite expansão da coluna 0

    # botoes e suas configs
    f = tk.Frame(frame_interno, bg='#90c7e8')
    f.grid(row=1, column=0, pady=(5, 20))

    cronometro = tk.Button(f, text='Cronômetro', font=("Helvetica 12 bold"), bg="#5fa3f1", fg="#f9e653", width=15, height=1, command=lambda: [print("Botão Cronômetro pressionado"), root.withdraw(), Cronometro()])
    cronometro.grid(row=0, column=1, padx=5, pady=20, sticky='ns')

    timer = tk.Button(f, text='Timer', font=("Helvetica 12 bold"), bg="#5fa3f1", fg="#f9e653", width=15, height=1, command=lambda: [print("Botão Cronômetro pressionado"), root.withdraw(), Timer()])
    timer.grid(row=1, column=1, padx=5, pady=20, sticky='ns')

    f.grid_rowconfigure(0, weight=1)
    f.grid_rowconfigure(1, weight=0)
    f.grid_rowconfigure(2, weight=1)
    f.grid_columnconfigure(0, weight=1)  # Permite expansão da coluna 0
    f.grid_columnconfigure(1, weight=0)  # Permite expansão da coluna 0
    f.grid_columnconfigure(3, weight=1)  # Permite expansão da coluna 0

    root.mainloop()
    criar.temporizador()
