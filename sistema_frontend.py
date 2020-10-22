from tkinter import *

class sistema_aplicacao():
    """Classe que define a interface gráfica da aplicação
    """
    #Criando a janela...
    JanelaPrincipal = Tk()
    JanelaPrincipal.wm_title("Cadastro de Clientes")


    #Criando variáveis que armazenarão o texto inserido pelo usuário...
    txtNome         = StringVar()
    txtSobrenome    = StringVar()
    txtEmail        = StringVar()
    txtCPF          = StringVar()
    txtBuscar       = StringVar()


    #Criando os objetos que estarão na janela...
    lblnome        = Label(JanelaPrincipal, text="Nome")
    lblsobrenome   = Label(JanelaPrincipal, text="Sobrenome")
    lblemail       = Label(JanelaPrincipal, text="Email")
    lblcpf         = Label(JanelaPrincipal, text="CPF")
    entNome        = Entry(JanelaPrincipal, textvariable=txtNome, width=30)
    entSobrenome   = Entry(JanelaPrincipal, textvariable=txtSobrenome, width=30)
    entEmail       = Entry(JanelaPrincipal, textvariable=txtEmail, width=30)
    entCPF         = Entry(JanelaPrincipal, textvariable=txtCPF, width=30)
    entBuscar      = Entry(JanelaPrincipal, textvariable=txtBuscar)
    listaClientes  = Listbox(JanelaPrincipal, width=80)
    scrollClientes = Scrollbar(JanelaPrincipal)
    btnVerTodos    = Button(JanelaPrincipal, text="Ver todos")
    btnBuscar      = Button(JanelaPrincipal, text="Buscar")
    btnInserir     = Button(JanelaPrincipal, text="Inserir")
    btnAtualizar   = Button(JanelaPrincipal, text="Atualizar Selecionados")
    btnDel         = Button(JanelaPrincipal, text="Deletar Selecionados")
    btnClose       = Button(JanelaPrincipal, text="Fechar")


    #Associando os objetos a grid da janela...
    lblnome.grid(row=0,column=0, padx=5, pady=3, sticky='N')
    lblsobrenome.grid(row=1,column=0, padx=5, pady=3, sticky='N')
    lblemail.grid(row=2,column=0, padx=5, pady=3, sticky='N')
    lblcpf.grid(row=3, column=0, padx=5, pady=3, sticky='N')

    entNome.grid(row=0, column=1, padx=5, pady=3, sticky='N')
    entSobrenome.grid(row=1, column=1, padx=5, pady=3, sticky='N')
    entEmail.grid(row=2, column=1, padx=5, pady=3, sticky='N')
    entCPF.grid(row=3, column=1, padx=5, pady=3, sticky='N')
    #entBuscar.grid(row=1, column=2, pady=3, sticky='WE')
    entBuscar.grid(row=0, column=2, columnspan=2, padx=50, pady=3, sticky='WE')

    listaClientes.grid(row=2, column=2, columnspan=2, rowspan=15, padx=0, pady=0, sticky='NS')
    scrollClientes.grid(row=2, column=4, rowspan=15, padx=0, pady=0, sticky='NS')

    btnBuscar.grid(row=1, column=2, columnspan=2, padx=50, pady=3, sticky='WE')
    btnVerTodos.grid(row=4, column=0, columnspan=2, sticky='WE', padx=8, pady=2)
    btnInserir.grid(row=6, column=0, columnspan=2, sticky='WE', padx=8, pady=2)
    btnAtualizar.grid(row=7, column=0, columnspan=2, sticky='WE', padx=8, pady=2)
    btnDel.grid(row=8, column=0, columnspan=2, sticky='WE', padx=8, pady=2)
    btnClose.grid(row=9, column=0, columnspan=2, sticky='WE', padx=8, pady=2)

    """
    sticky: Indica em qual ponto da janela (norte – N, sul – S, leste – E ou oeste W) o objeto estará ancorado. 
    Se você combinar o ponto leste e oeste (EW), o elemento ocupará todo o espaço horizontal da coluna em que está localizado. 
    O mesmo ocorre se colocarmos NS (norte-sul), o elemento ocupará todo o espaço vertical.
     N
    W E
     S   
    """

    #Associando a Scrollbar (scrollClientes) com a Listbox (listaClientes).
    listaClientes.configure(yscrollcommand=scrollClientes.set)

    """
    No fonte acima, o argumento yscrollcommand é responsável por definir qual é o 
    objeto do tipo scrollbar que será o responsável por acompanhar o rolamento vertical. 
    Note que é necessário utilizar a propriedade .set do objeto scrollbar para que ele seja definido na ListBox.
    """

    scrollClientes.configure(command=listaClientes.yview)

    """
    O argumento command (command=listClientes.yview) define qual o função será chamada quando a scrollbar for ativada. 
    Neste caso, estamos falando que a posição vertical será alterada sempre que o ScrollBar for manipulado.
    """

    #Adicionando um pouco de SWAG a interface...
    """for child in JanelaPrincipal.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')
"""
    def rodar(self):
        sistema_aplicacao.JanelaPrincipal.mainloop()