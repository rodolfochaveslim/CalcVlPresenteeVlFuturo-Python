import tkinter as tk
from tkinter import ttk, messagebox


class CalculadoraFinanceiraApp:
    def __init__(self):
        # Configuração da janela principal
        self.janela_principal = tk.Tk()
        self.janela_principal.title("Calculadora Financeira Avançada")
        self.janela_principal.geometry("450x450")

        # Configuração de estilo
        self.definir_estilos()

        # Criação dos componentes da interface
        self.criar_secao_entrada()
        self.criar_secao_resultado()
        self.criar_secao_botoes()

    def definir_estilos(self):
        """Configura o estilo visual dos componentes"""
        estilo = ttk.Style()
        estilo.configure("TLabel", font=("Calibri", 11))
        estilo.configure("TButton", font=("Calibri", 11))
        estilo.configure("TLabelframe", font=("Calibri", 12, "bold"))

    def criar_secao_entrada(self):
        """Cria a seção de entrada de dados"""
        self.secao_entrada = ttk.LabelFrame(
            self.janela_principal, text="Informe os Dados", padding="10"
        )
        self.secao_entrada.pack(padx=15, pady=10, fill="both")

        # Campos de entrada
        self.dados_entrada = {}
        campos = [("Montante:", 0), ("Taxa de Juros (%):", 1), ("Número de Períodos:", 2)]
        for label_texto, linha in campos:
            ttk.Label(self.secao_entrada, text=label_texto).grid(row=linha, column=0, padx=10, pady=5)
            campo = ttk.Entry(self.secao_entrada, width=20)
            campo.grid(row=linha, column=1, padx=10, pady=5)
            self.dados_entrada[label_texto] = campo

    def criar_secao_resultado(self):
        """Cria a seção para exibir o resultado"""
        self.secao_resultado = ttk.LabelFrame(
            self.janela_principal, text="Resultado do Cálculo", padding="10"
        )
        self.secao_resultado.pack(padx=15, pady=10, fill="both")
        self.label_exibir_resultado = ttk.Label(self.secao_resultado, text="", justify="center")
        self.label_exibir_resultado.pack(padx=10, pady=10)

    def criar_secao_botoes(self):
        """Cria a seção dos botões de ação"""
        self.secao_botoes = ttk.Frame(self.janela_principal)
        self.secao_botoes.pack(padx=10, pady=15)

        # Botões de ações
        ttk.Button(
            self.secao_botoes, text="Calcular Valor Futuro",
            command=lambda: self.processar_calculo("VF")
        ).pack(side="left", padx=10)

        ttk.Button(
            self.secao_botoes, text="Calcular Valor Presente",
            command=lambda: self.processar_calculo("VP")
        ).pack(side="left", padx=10)

        ttk.Button(self.secao_botoes, text="Limpar", command=self.limpar_campos).pack(side="left", padx=10)
        ttk.Button(self.secao_botoes, text="Sair", command=self.janela_principal.quit).pack(side="left", padx=10)

    def calcular_valor_futuro(self, vp, taxa, periodos):
        """Calcula o Valor Futuro (VF)"""
        try:
            vp = float(vp)
            taxa = float(taxa) / 100
            periodos = float(periodos)
            return vp * (1 + taxa) ** periodos
        except ValueError:
            return None

    def calcular_valor_presente(self, vf, taxa, periodos):
        """Calcula o Valor Presente (VP)"""
        try:
            vf = float(vf)
            taxa = float(taxa) / 100
            periodos = float(periodos)
            return vf / ((1 + taxa) ** periodos)
        except ValueError:
            return None

    def processar_calculo(self, tipo):
        """Executa o cálculo conforme o tipo selecionado"""
        valor = self.dados_entrada["Montante:"].get()
        taxa = self.dados_entrada["Taxa de Juros (%):"].get()
        periodos = self.dados_entrada["Número de Períodos:"].get()

        if tipo == "VF":
            resultado = self.calcular_valor_futuro(valor, taxa, periodos)
            tipo_valor = "Valor Presente"
        else:
            resultado = self.calcular_valor_presente(valor, taxa, periodos)
            tipo_valor = "Valor Futuro"

        if resultado is not None:
            self.label_exibir_resultado.config(
                text=f"{'Valor Futuro' if tipo == 'VF' else 'Valor Presente'}: R$ {resultado:.2f}\n"
                     f"--- Dados Utilizados ---\n"
                     f"{tipo_valor}: R$ {float(valor):.2f}\n"
                     f"Taxa de Juros: {float(taxa)}%\n"
                     f"Períodos: {periodos}"
            )
        else:
            messagebox.showerror("Erro", "Insira valores numéricos válidos nos campos!")

    def limpar_campos(self):
        """Limpa todos os campos de entrada e o resultado"""
        for campo in self.dados_entrada.values():
            campo.delete(0, tk.END)
        self.label_exibir_resultado.config(text="")

    def iniciar(self):
        """Inicia o aplicativo"""
        self.janela_principal.mainloop()


if __name__ == "__main__":
    app = CalculadoraFinanceiraApp()
    app.iniciar()
