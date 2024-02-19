import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interact  
import datetime
from workadays import workdays as wd
import streamlit as st


#############################################################
# PARÂMETROS DE ENTRADA

cols = st.columns(2)

with cols[0]:
    st.subheader('MP-resuldados', divider=True)
    st.caption('Comparador de investimentos')

    col1, col2 = st.columns(2)
    with col1:
        a = st.date_input('Data inicial',
                          datetime.date.today(),
                          format='DD.MM.YYYY'
                         )
    with col2:

        b = st.date_input('Data final',
                          datetime.date.today()+datetime.timedelta(days=365),
                          format='DD.MM.YYYY')

    cursor = st.slider(
        'rendimento do CBD (% do CDI)',
        value = 100,
        min_value = 80,
        max_value = 230,
    )

    info = st.empty()

    figura = st.button('comparar investimentos por 2 anos')
    

#############################################################
# FUNÇÕES

with cols[1]:
    taxaDI = 0.1125
    C = (1+taxaDI)**(1/252) - 1


    def contador(a, b):
        N = (b-a).days
        n = wd.networkdays(a, b)
        return N, n

    def imposto(N):
        if N<=180:
            return 0.225
        elif N<=360:
            return 0.20
        elif N<=720:
            return 0.175
        else:
            return 0.15

    @np.vectorize
    def P_LCI(a, b, P_CDB):
        N, n = contador(a, b)
        return 100*((( ((C*0.01*P_CDB+1)**n -1)*(1-imposto(N))) + 1)**(1/n) -1) / C
        
    info.info(f'Um CDB com {cursor}% do CDI tem o mesmo rendimento que um LCI/ LCA de {round(P_LCI(a, b, cursor).item(),1)}% no período escolhido.', icon='💰')

    @np.vectorize
    def P_CDB(a, b, P_LCI):
        N, n = contador(a, b)
        return 100*( (((C*0.01*P_LCI+1)**n - 1)/(1-imposto(N)) + 1 )**(1/n) -1) / C

    @np.vectorize
    def R_CDB(a, b, P):
        N, n = contador(a, b)
        rendimento = 100*( ((C*0.01*P + 1)**n - 1) * (1-imposto(N)) )
        return rendimento

    @np.vectorize
    def R_LCI(a, b, P):
        N, n = contador(a, b)
        return 100*((C*0.01*P + 1)**n - 1)

    #############################################################
    # GRÁFICO DE COMPARAÇÃO DE RENTABILIDADE

    if figura:

        st.info('O carregamento do gráfico pode demorar um pouco.', icon='⏳')
        
        tempo = pd.date_range(a, a + datetime.timedelta(days=2*365))
        dias = [tempo[i].date() for i in range(len(tempo))][1:]

        fig, ax = plt.subplots()

        for label in ax.get_xticklabels(which='major'):
            label.set(rotation=15)
            
        cdb = cursor
        lci = P_LCI(a, b, cursor).item()

        ax.plot(dias, R_CDB(a, dias, cdb), label=f'CDB {cdb}%')
        ax.plot(dias, R_LCI(a, dias, lci), label=f'LCI {round(lci,1)}%')
        ax.set_title('Comparação entre um CDB e um LCI/ LCA')
       # ax.set_xlabel('datas')
        ax.set_ylabel('rendimento líquido em %')
        ax.legend(loc='upper left', ncols=1)
        ax.grid()
        ax.text(
            0.5,
            0.5,
            "MP-resuldados",
            transform=ax.transAxes,
            fontsize=40,
            color="gray",
            alpha=0.1,
            ha="center",
            va="center",
            rotation=45,
        )
        
        st.pyplot(fig)

