# Projeto GUI para Analise Sensorial de Chá

import tkinter

def preparo_cha(parametro):
        label_preparo = tkinter.Label(janela, font= 'Helvetica 14 bold', fg='dark green')
        label_preparo['text'] = '\nInformações do Chá:'
        label_preparo.pack()
        
        label_preparo = tkinter.Label(janela)
        label_preparo['text'] = 'Tipo de Chá: {}\nNome: {}\nMarca: {}\nPaís: {}\nSafra: {}'.format(options_tipo.get(),ent_tea.get(),ent_brand.get(),options_country.get(),options_safra.get())
        label_preparo.pack()

        label_preparo = tkinter.Label(janela, font= 'Helvetica 14 bold', fg='dark green')
        label_preparo['text'] = '\nModo de Preparo:'
        label_preparo.pack()
        
                # Quantidade
        
        qt_tea = round(float(options_qt_h2o.get()) * 0.015,0)
        label_qtd = tkinter.Label(janela)
        label_qtd['text'] = 'Para {} ml de água, você deve infusionar {} gramas de {} {} da {}.'.format(options_qt_h2o.get(),qt_tea,options_tipo.get(),ent_tea.get(),ent_brand.get())
        label_qtd.pack()

                 # Temperatura

        if options_tipo.get() == 'chá amarelo' or options_tipo.get() == 'chá branco' or options_tipo.get() == 'chá verde':
                temp = int(80)
                lbl_temp = tkinter.Label(janela, text = 'A temperatura da água deve ser de 80ºC.')
                lbl_temp.pack()
        else:
                temp = int(100)
                lbl_temp = tkinter.Label(janela, text = 'A temperatura da água deve ser de 100ºC.')
                lbl_temp.pack()
              
                # Tempo de infusão
        
        if options_tipo.get() == 'chá amarelo' or options_tipo.get() == 'puerh maduro':
                time = float(1.0)
                lbl_time = tkinter.Label(janela, text = 'Tempo de infusão: 1 minuto.')
                lbl_time.pack()
        elif options_tipo.get() == 'chá branco':
                time = float(2.0)
                lbl_time = tkinter.Label(janela, text = 'Tempo de infusão: 2 minutos.')
                lbl_time.pack()
        elif options_tipo.get() == 'chá verde':
                time = float(0.40)
                lbl_time = tkinter.Label(janela, text = 'Tempo de infusão: 40 segundos.')
                lbl_time.pack()
        elif options_tipo.get() == 'chá preto':
                time = float(0.20)
                lbl_time = tkinter.Label(janela, text = 'Tempo de infusão: 20 segundos.')
                lbl_time.pack()
        elif options_tipo.get() == 'oolong claro' or options_tipo.get() == 'oolong médio':
                time = float(0.50)
                lbl_time = tkinter.Label(janela, text = 'Tempo de infusão: 50 segundos.')
                lbl_time.pack()
        elif options_tipo.get() == 'oolong escuro':
                time = float(0.30)
                lbl_time = tkinter.Label(janela, text = 'Tempo de infusão: 30 segundos.')
                lbl_time.pack()
        elif options_tipo.get() == 'puerh cru':
                time = float(0.15)
                lbl_time = tkinter.Label(janela, text = 'Tempo de infusão: 15 segundos.')
                lbl_time.pack()
        else:
                lbl_time = tkinter.Label(janela)
                lbl_time['text'] = 'Tempo de infusão (minutos):'
                lbl_time.pack()
                ent_time = tkinter.Entry(janela)
                ent_time.pack()

        label_preparo = tkinter.Label(janela, font='Helvetica 13 italic')
        label_preparo['text'] = '\nEnjoy your cuppa!\n'
        label_preparo.pack()

                # Salvar no arquivo

        file = open('PreparoCha.csv','a')
        file.write(options_tipo.get()+', '+ent_tea.get()+', '+ent_brand.get()+', '+options_country.get()+', '+options_safra.get()+', '+str(options_qt_h2o.get())+', '+options_h2o.get()+', '+str(temp)+', '+str(time)+'\n')
        file.close()
        
janela = tkinter.Tk()
janela.title('Preparo do Chá')

janela.geometry('750x750')
janela.tk_setPalette(background='floral white')

lbl_titulo = tkinter.Label(janela, font= 'Helvetica 18 bold', fg='dark green')
lbl_titulo['text'] = 'Ficha Técnica de Preparo de Chá'
lbl_titulo.pack()

        # Input dados do chá a ser preparado:

lbl_tipo = tkinter.Label(janela)
lbl_tipo['text'] = '\n1. Tipo do chá:'
lbl_tipo.pack()   
Ltipo = ['chá amarelo', 'chá branco', 'chá verde', 'chá preto', 'oolong claro', 'oolong médio','oolong escuro','puerh cru','puerh maduro','outros']
options_tipo = tkinter.StringVar(janela)
options_tipo.set(Ltipo[2])
opt_tipo = tkinter.OptionMenu(janela, options_tipo, *Ltipo)
opt_tipo.pack()

lbl_tea = tkinter.Label(janela)
lbl_tea['text'] = '2. Nome do Chá:'
lbl_tea.pack()
ent_tea = tkinter.Entry(janela)
ent_tea.pack()

lbl_brand = tkinter.Label(janela)
lbl_brand['text'] = '3. Marca:'
lbl_brand.pack()
ent_brand = tkinter.Entry(janela)
ent_brand.pack()

lbl_country = tkinter.Label(janela)
lbl_country['text'] = '4. País:'
lbl_country.pack()
Lcountry = ['Africa do Sul','Argentina','Brasil','China','Coreia do Sul','India','Japão','Nepal','Quênia','Sri Lanka','Taiwan','Outros países']
options_country = tkinter.StringVar(janela)
options_country.set(Lcountry[3])
opt_country = tkinter.OptionMenu(janela, options_country, *Lcountry)
opt_country.pack()

lbl_safra = tkinter.Label(janela)
lbl_safra['text'] = '5. Safra:'
lbl_safra.pack()
Lsafra = ['2020','2019','2018','2017','2016','2015','2014','2013','2012','2011','2010','anterior']
options_safra = tkinter.StringVar(janela)
options_safra.set(Lsafra[1])
opt_safra = tkinter.OptionMenu(janela, options_safra, *Lsafra)
opt_safra.pack()

lbl_qt_h2o = tkinter.Label(janela)
lbl_qt_h2o['text'] = '6. Quantidade de água (ml):'
lbl_qt_h2o.pack()
Lqt_h2o = ['100','140','150','170','200','250','500','1000']
options_qt_h2o = tkinter.StringVar(janela)
options_qt_h2o.set(Lqt_h2o[1])
opt_qt_h2o = tkinter.OptionMenu(janela, options_qt_h2o, *Lqt_h2o)
opt_qt_h2o.pack()

lbl_h2o = tkinter.Label(janela)
lbl_h2o['text'] = '7. Tipo de água:'
lbl_h2o.pack()
Lh2o = ['água filtrada','água mineral','água de mina/poço','outros']
options_h2o = tkinter.StringVar(janela)
options_h2o.set(Lh2o[0])
opt_h2o = tkinter.OptionMenu(janela, options_h2o, *Lh2o)
opt_h2o.pack()

lbl_espaço = tkinter.Label(janela)
lbl_espaço['text'] = ''
lbl_espaço.pack()

btn_preparo = tkinter.Button(janela, font= 'Helvetica 12 bold', fg='dark green')
btn_preparo['text'] = 'Salvar Dados'
btn_preparo['command'] = lambda: preparo_cha(options_tipo.get())
btn_preparo.pack()

janela.mainloop()
