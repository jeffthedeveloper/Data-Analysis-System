from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
import matplotlib.pyplot as plt
import io
from reportlab.lib import colors

def gerar_relatorio():
    # Criando o canvas do PDF
    c = canvas.Canvas("analysis_report.pdf", pagesize=letter)
    c.setFont("Helvetica", 12)
    
    # Página 1: Capa
    c.drawString(100, 750, "Relatório de Análise de Dados Corporativos")
    c.drawString(100, 735, "Análise de Marketing, Vendas, Sinistros e Recomendações de Produtos")
    c.drawString(100, 720, "Data: Fevereiro de 2025")
    c.drawString(100, 705, "Equipe: Synapse Dados, Marketing e Web")
    c.showPage()

    # Página 2: Introdução
    c.drawString(100, 750, "Introdução")
    c.drawString(100, 735, "Este relatório foi produzido pela Synapse Dados, Marketing e Web e apresenta análises sobre dados corporativos.")
    c.showPage()

    # Página 3: Tabelas de Marketing
    c.drawString(100, 750, "Análise de Marketing")
    
    # Criando uma tabela com dados de Marketing
    data = [
        ['Localização', 'Total de Clientes', 'Idade Média'],
        ['São Paulo', 120, 33],
        ['Rio de Janeiro', 85, 28],
        ['Belo Horizonte', 60, 35]
    ]
    
    table = Table(data, colWidths=[100, 150, 100])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    table.wrapOn(c, 400, 600)
    table.drawOn(c, 100, 500)
    c.showPage()

    # Página 4: Gráfico de Marketing
    c.drawString(100, 750, "Gráfico de Marketing: Distribuição de Clientes por Localização")
    
    # Gerando um gráfico com Matplotlib
    fig, ax = plt.subplots(figsize=(6, 3))  # Definindo o tamanho da imagem
    locations = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
    clientes = [120, 85, 60]
    
    ax.bar(locations, clientes, color='skyblue')
    ax.set_title('Distribuição de Clientes por Localização')
    ax.set_xlabel('Localização')
    ax.set_ylabel('Total de Clientes')
    
    # Salvando o gráfico como uma imagem em memória
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    
    # Inserindo o gráfico no PDF
    c.drawImage(image_stream, 100, 350, width=400, height=200)
    c.showPage()

    # Página 5: Análise de Vendas (Tabela)
    c.drawString(100, 750, "Análise de Vendas")
    
    # Tabela de vendas
    sales_data = [
        ['Categoria', 'Total de Vendas', 'Receita Total (R$)'],
        ['Tecnologia', 500, 150000],
        ['Moda', 300, 60000],
        ['Alimentação', 250, 50000]
    ]
    
    sales_table = Table(sales_data, colWidths=[100, 150, 150])
    sales_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    sales_table.wrapOn(c, 400, 600)
    sales_table.drawOn(c, 100, 500)
    c.showPage()

    # Página 6: Gráfico de Vendas
    c.drawString(100, 750, "Gráfico de Vendas por Categoria")
    
    # Gerando um gráfico de vendas
    fig, ax = plt.subplots(figsize=(6, 3))
    categories = ['Tecnologia', 'Moda', 'Alimentação']
    sales = [150000, 60000, 50000]
    
    ax.pie(sales, labels=categories, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
    ax.set_title('Distribuição de Receita por Categoria de Produto')

    # Salvando o gráfico como imagem em memória
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    
    # Inserindo o gráfico no PDF
    c.drawImage(image_stream, 100, 350, width=400, height=200)
    c.showPage()

    # Salvando o PDF
    c.save()

gerar_relatorio()
