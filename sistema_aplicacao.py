from sistema_frontend import *
import sistema_backend as backend

app = None

def view_command():
    rows = backend.view()
    app.listaClientes.delete(0, END)
    for r in rows:
        app.listaClientes.insert(END, r)

def search_command():
    app.listaClientes.delete(0, END)
    #rows = backend.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    rows = backend.search(app.txtBuscar.get())
    for r in rows:
        app.listaClientes.insert(END, r)

def insert_command():
    backend.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def update_command():
    backend.update(selected[0],app.txtNome.get(),app.txtSobrenome.get(),app.txtEmail.get(), app.txtCPF.get())
    view_command()

def del_command():
    id = selected[0]
    backend.delete(id)
    view_command()


def getSelectedRow(event):
    global selected
    index = app.listaClientes.curselection()[0]
    selected = app.listaClientes.get(index)
    app.entNome.delete(0, END)
    app.entNome.insert(END, selected[1])
    app.entSobrenome.delete(0, END)
    app.entSobrenome.insert(END, selected[2])
    app.entEmail.delete(0, END)
    app.entEmail.insert(END, selected[3])
    app.entCPF.delete(0, END)
    app.entCPF.insert(END, selected[4])
    return selected


if __name__ == "__main__":
    app = sistema_aplicacao()
    app.listaClientes.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnVerTodos.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnAtualizar.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.JanelaPrincipal.destroy)
    app.rodar()
