from mysql.connector import (connection)
from fpdf import FPDF
from libsql import MysqlComands


class Bdpdf():

    def __init__(self, host, user, password, database):
        self.bdpdf = MysqlComands(host, user, password, database)
        self.pdfconexao = connection.MySQLConnection(host = "localhost", user = "root", password = "", database = "curriculos_bd")
        self.pdfcursor = self.pdfconexao.cursor()

init = Bdpdf("localhost", "root", "", "curriculos_bd")

class PDF(FPDF):

    # Cabeçario do pdf

    def header(self):
        self.set_font("Arial", "B", 15)
        self.cell(80)
        self.cell(30, 10, "Curriculos", 1, 0, "C")
        self.ln(20)

    # Rodapé do pdf

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    # Gerar pdf

    def gerarPdf(self):
        self.pdf = PDF()
        self.pdf.alias_nb_pages()
        self.pdf.add_page()
        self.pdf.set_font("Times", "", 12)
        init.pdfcursor.execute("SELECT * FROM usuarios")
        self.dados_pdf = init.pdfcursor.fetchall()
        self.lista_pdf = []
        for i in self.dados_pdf:
            self.lista_pdf.append(i)
        for i in self.lista_pdf:
            self.pdf.cell(0, 10, f"NOME: {i[1]}, TELEFONE: {i[2]}, MINIBIO: {i[3]}", 0, 1)
            self.pdf.cell(0, 10, f"ENTREVISTA: {i[4]}, TESTE_TÓRICO: {i[5]}, TESTE_PRÁTICO: {i[6]}, SOFT_SKILL: {i[7]} ", 0, 1)
            self.pdf.cell(0, 10, "________________________________________________________________________________________", 0, 1)
        self.pdf.output("Entrevistados.pdf", "F")
        init.pdfconexao.commit()

    # Gerar pdf resumido

    def gerarPfdResumido(self):
        self.pdf = PDF()
        self.pdf.alias_nb_pages()
        self.pdf.add_page()
        self.pdf.set_font("Times", "", 12)
        init.pdfcursor.execute("SELECT * FROM usuarios")
        self.dados_pdf = init.pdfcursor.fetchall()
        self.lista_pdf = []
        for i in self.dados_pdf:
            self.lista_pdf.append(i)
        for i in self.lista_pdf:
            self.pdf.cell(0, 10, f"NOME: {i[1]}", 0, 1)
            self.pdf.cell(0, 10, f"ENTREVISTA: {i[4]}, TESTE_TÓRICO: {i[5]}, TESTE_PRÁTICO: {i[6]}, SOFT_SKILL: {i[7]} ", 0, 1)
            self.pdf.cell(0, 10, "________________________________________________________________________________________", 0, 1)
        self.pdf.output("Entrevistados_Resumido.pdf", "F")
        init.pdfconexao.commit()

    # Gerar pdf filtrado

    def gerarPdfFiltrado(self, entrevista, teste_teorico, teste_pratico, soft_skill):
        self.pdf = PDF()
        self.pdf.alias_nb_pages()
        self.pdf.add_page()
        self.pdf.set_font("Times", "", 12)
        init.pdfcursor.execute(f"SELECT * FROM usuarios WHERE entrevista >= {entrevista} AND teste_teorico >= {teste_teorico} AND teste_pratico >= {teste_pratico} AND soft_skills >= {soft_skill}")
        self.dados_pdf = init.pdfcursor.fetchall()
        self.lista_pdf = []
        for i in self.dados_pdf:
            self.lista_pdf.append(i)
        for i in self.lista_pdf:
            self.pdf.cell(0, 10, f"NOME: {i[1]}, TELEFONE: {i[2]}, MINIBIO: {i[3]}", 0, 1)
            self.pdf.cell(0, 10, f"ENTREVISTA: {i[4]}, TESTE_TÓRICO: {i[5]}, TESTE_PRÁTICO: {i[6]}, SOFT_SKILL: {i[7]} ", 0, 1)
            self.pdf.cell(0, 10, "________________________________________________________________________________________", 0, 1)
        self.pdf.output("Entrevistados_Filtrado.pdf", "F")
        init.pdfconexao.commit()

    # Gerar pdf filtrado e resumido

    def gerarPdfFiltradoResumido(self, entrevista, teste_teorico, teste_pratico, soft_skill):
        self.pdf = PDF()
        self.pdf.alias_nb_pages()
        self.pdf.add_page()
        self.pdf.set_font("Times", "", 12)
        init.pdfcursor.execute(f"SELECT * FROM usuarios WHERE entrevista >= {entrevista} AND teste_teorico >= {teste_teorico} AND teste_pratico >= {teste_pratico} AND soft_skills >= {soft_skill}")
        self.dados_pdf = init.pdfcursor.fetchall()
        self.lista_pdf = []
        for i in self.dados_pdf:
            self.lista_pdf.append(i)
        for i in self.lista_pdf:
            self.pdf.cell(0, 10, f"NOME: {i[1]}", 0, 1)
            self.pdf.cell(0, 10, f"ENTREVISTA: {i[4]}, TESTE_TÓRICO: {i[5]}, TESTE_PRÁTICO: {i[6]}, SOFT_SKILL: {i[7]} ", 0, 1)
            self.pdf.cell(0, 10, "________________________________________________________________________________________", 0, 1)
        self.pdf.output("Entrevistados_Filtrado_Resumido.pdf", "F")
        init.pdfconexao.commit()

    