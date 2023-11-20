import tkinter as tk
from tkinter import messagebox as mg
from libsql import MysqlComands
from libpdf import PDF

class Main():

    def __init__(self, host, user, password, database):
        self.mysql_comands = MysqlComands(host, user, password, database)
        self.pdf_comands = PDF()
        self.janela1 = tk.Tk()
        self.janela1.geometry("900x650")
        self.janela1.title("Curriculos")

        # Frame para deixar os inputs e botões para o lado esquerdo

        self.left_frame = tk.Frame(self.janela1)
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Botões e inputs

        self.retulo_nome = tk.Label(self.left_frame, text="Nome")
        self.retulo_nome.pack(pady=5)
        self.campo_nome = tk.Entry(self.left_frame, width=40)
        self.campo_nome.pack(pady=5)

        self.rotulo_telefone = tk.Label(self.left_frame, text="Telefone")
        self.rotulo_telefone.pack(pady=5)
        self.campo_telefone = tk.Entry(self.left_frame, width=40)
        self.campo_telefone.pack(pady=5)

        self.rotulo_minibio = tk.Label(self.left_frame, text="Minibio")
        self.rotulo_minibio.pack(pady=5)
        self.campo_minibio = tk.Entry(self.left_frame, width=40)
        self.campo_minibio.pack(pady=5)

        self.rotulo_entrevista = tk.Label(self.left_frame, text="Nota da Entrevista")
        self.rotulo_entrevista.pack(pady=5)
        self.campo_entrevista = tk.Entry(self.left_frame, width=40)
        self.campo_entrevista.pack(pady=5)

        self.rotulo_teste_teorico = tk.Label(self.left_frame, text="Nota do Teste Teórico")
        self.rotulo_teste_teorico.pack(pady=5)
        self.campo_teste_teorico = tk.Entry(self.left_frame, width=40)
        self.campo_teste_teorico.pack(pady=5)

        self.rotulo_teste_pratico = tk.Label(self.left_frame, text="Nota do Teste Pratico")
        self.rotulo_teste_pratico.pack(pady=5)
        self.campo_teste_pratico = tk.Entry(self.left_frame, width=40)
        self.campo_teste_pratico.pack(pady=5)

        self.rotulo_soft_skill = tk.Label(self.left_frame, text="Nota de Soft Skills")
        self.rotulo_soft_skill.pack(pady=5)
        self.campo_soft_skill = tk.Entry(self.left_frame, width=40)
        self.campo_soft_skill.pack(pady=5)

        self.botao_cadastrar = tk.Button(self.left_frame, width=25, text="Cadastrar", command=self.cadastrar)
        self.botao_cadastrar.pack(pady=10)

        self.botao_filtrar = tk.Button(self.left_frame, width=25, text="Filtrar", command=self.filtrar)
        self.botao_filtrar.pack(pady=10)

        self.botao_pdf = tk.Button(self.left_frame, text="Gerar PDF", width=25, command=self.gerarPdfCompleto)
        self.botao_pdf.pack(pady=10)

        self.botao_pdf_resumido = tk.Button(self.left_frame, width=25, text="Gerar PDF 'Resumido'", command=self.gerarPdfResumido)
        self.botao_pdf_resumido.pack(pady=10)

        # ScrollBox 

        def rolar(*args):
            self.text.yview(*args)

        self.text = tk.Text(self.janela1, wrap="none", width=40, height=10)
        self.text.pack(side="left", fill="both", expand=True)
        self.scrollbar = tk.Scrollbar(self.janela1, command=rolar)
        self.scrollbar.pack(side="right", fill="y")
        self.text.configure(yscrollcommand=self.scrollbar.set)

        for i in self.mysql_comands.get():
            self.text.insert(tk.END, f"NOME: {i[1]}, TELEFONE: {i[2]} MINIBIO: {i[3]} \n NOTAS: [ENTREVISTA: {i[4]}, TESTE_TÓRICO: {i[5]}, TESTE_PRÁTICO: {i[6]}, SOFT_SKILL: {i[7]} ] \n _________________________________________________________________________ \n")

        self.janela1.mainloop()

    # Função para cadastrar os dados no banco de dados

    def cadastrar(self):

        if((self.campo_nome.get() == "" or self.campo_nome.get() == None) or (self.campo_telefone.get() == "" or self.campo_telefone.get() == None) or (self.campo_minibio.get() == "" or self.campo_minibio.get() == None) or (self.campo_entrevista.get() == "" or self.campo_entrevista.get() == None) or (self.campo_teste_teorico.get() == "" or self.campo_teste_teorico.get() == None) or (self.campo_teste_pratico.get() == "" or self.campo_teste_pratico.get() == None) or (self.campo_soft_skill.get() == "" or self.campo_soft_skill.get() == None)):
            self.messageFalse()
        else:
            self.nome = self.campo_nome.get()
            self.telefone = int(self.campo_telefone.get())
            self.minibio = self.campo_minibio.get()
            self.entrevista = int(self.campo_entrevista.get())
            self.teste_teorico = int(self.campo_teste_teorico.get())
            self.teste_pratico = int(self.campo_teste_pratico.get())
            self.soft_skill = int(self.campo_soft_skill.get())
            self.mysql_comands.insert(self.nome, self.telefone, self.minibio, self.entrevista, self.teste_teorico, self.teste_pratico, self.soft_skill)
            self.text.insert(tk.END, f"NOME: {self.nome}, TELEFONE: {self.telefone} MINIBIO: {self.minibio} \n NOTAS: [ENTREVISTA: {self.entrevista}, TESTE_TÓRICO: {self.teste_teorico}, TESTE_PRÁTICO: {self.teste_pratico}, SOFT_SKILL: {self.soft_skill} ] \n _________________________________________________________________________ \n")
            self.messageTru()
        
    # Funções que geram os pfds

    def gerarPdfCompleto(self):
        self.pdf_comands.gerarPdf()

    def gerarPdfResumido(self):
        self.pdf_comands.gerarPfdResumido()

    def gerarPdfFiltrado(self):
        self.pdf_comands.gerarPdfFiltrado(self.filtro_entrevista, self.filtro_teste_teorico, self.filtro_teste_pratico, self.filtro_soft_skill)

    def gerarPdfFiltradoResumido(self):
        self.pdf_comands.gerarPdfFiltradoResumido(self.filtro_entrevista, self.filtro_teste_teorico, self.filtro_teste_pratico, self.filtro_soft_skill)

    # Tela de filtragem das notas 

    def tela_filtrar(self):

        if((self.campo_filtro_entrevista.get() == "" or self.campo_filtro_entrevista.get() == None) or (self.campo_filtro_teste_teorico.get() == "" or self.campo_filtro_teste_teorico.get() == None) or (self.campo_filtro_teste_pratico.get() == "" or self.campo_filtro_teste_pratico.get() == None) or (self.campo_filtro_soft_skill.get() == "" or self.campo_filtro_soft_skill.get() == None)):
            self.messageFalse()
        else:
            self.janela_filtro = tk.Toplevel()
            self.janela_filtro.geometry("650x500")
            self.janela_filtro.title("Curriculos")

            self.botao_filtro_pdf = tk.Button(self.janela_filtro, width=20, text="Gerar PDF", command=self.gerarPdfFiltrado)
            self.botao_filtro_pdf.pack(pady=10)

            self.botao_filtro_resumido_pdf = tk.Button(self.janela_filtro, width=20, text="Gerar PDF 'Resumido'", command=self.gerarPdfFiltradoResumido)
            self.botao_filtro_resumido_pdf.pack(pady=10)

            self.botao_filtro_fechar = tk.Button(self.janela_filtro, width=20, text="Fechar", command=self.janela_filtro.destroy)
            self.botao_filtro_fechar.pack(pady=10)

            def rolar(*args):
                self.text_filtro.yview(*args)

            self.text_filtro = tk.Text(self.janela_filtro, wrap="none", width=40, height=10)
            self.text_filtro.pack(side="left", fill="both", expand=True)
            self.scrollbar = tk.Scrollbar(self.janela_filtro, command=rolar)
            self.scrollbar.pack(side="right", fill="y")
            self.text_filtro.configure(yscrollcommand=self.scrollbar.set)
        
            self.filtro_entrevista = self.campo_filtro_entrevista.get()
            self.filtro_teste_teorico = self.campo_filtro_teste_teorico.get()
            self.filtro_teste_pratico = self.campo_filtro_teste_pratico.get()
            self.filtro_soft_skill = self.campo_filtro_soft_skill.get()

            for i in self.mysql_comands.get_filtrado(self.filtro_entrevista, self.filtro_teste_teorico, self.filtro_teste_pratico, self.filtro_soft_skill):
                self.text_filtro.insert(tk.END, f"NOME: {i[1]}, TELEFONE: {i[2]} MINIBIO: {i[3]} \n NOTAS: [ENTREVISTA: {i[4]}, TESTE_TÓRICO: {i[5]}, TESTE_PRÁTICO: {i[6]}, SOFT_SKILL: {i[7]} ] \n _________________________________________________________________________ \n")

    # Mensagens para ficar mais bunitim :)

    def messageTru(self):
        mg.showinfo("Sucesso!", "Realizado com Sucesso!")

    def messageFalse(self):
        mg.showerror("Erro!", "Erro, algum campo não preenchido!")

    # Tela onde você digita as notas para filtrar

    def filtrar(self):
        self.janela_filtrar = tk.Toplevel()
        self.janela_filtrar.geometry("250x350")
        self.janela_filtrar.title("Curriculos")

        self.rotulo_filtro_entrevista = tk.Label(self.janela_filtrar, text="Entrevista")
        self.rotulo_filtro_entrevista.pack(pady=5)
        self.campo_filtro_entrevista = tk.Entry(self.janela_filtrar)
        self.campo_filtro_entrevista.pack(pady=5)

        self.rotulo_filtro_teste_teorico = tk.Label(self.janela_filtrar, text="Teste Teórico")
        self.rotulo_filtro_teste_teorico.pack(pady=5)
        self.campo_filtro_teste_teorico = tk.Entry(self.janela_filtrar)
        self.campo_filtro_teste_teorico.pack(pady=5)

        self.rotulo_filtro_teste_pratico = tk.Label(self.janela_filtrar, text="Teste Pratico")
        self.rotulo_filtro_teste_pratico.pack(pady=5)
        self.campo_filtro_teste_pratico = tk.Entry(self.janela_filtrar)
        self.campo_filtro_teste_pratico.pack(pady=5)

        self.rotulo_filtro_soft_skill = tk.Label(self.janela_filtrar, text="Soft Skill")
        self.rotulo_filtro_soft_skill.pack(pady=5)
        self.campo_filtro_soft_skill = tk.Entry(self.janela_filtrar)
        self.campo_filtro_soft_skill.pack(pady=5)

        self.botao_filtrar_notas = tk.Button(self.janela_filtrar, text="Filtrar", width=10, command=self.tela_filtrar)
        self.botao_filtrar_notas.pack(pady=10)

        self.botao_filtrar_notas_fechar = tk.Button(self.janela_filtrar, text="Fechar", width=10, command=self.janela_filtrar.destroy)
        self.botao_filtrar_notas_fechar.pack(pady=10)

inicializador = Main("localhost", "root", "", "curriculos_bd")


