## Introdução

Neste trabalho construímos uma aplicação para comparar investimentos em CDB e LCI/ LCA que rendem segundo o CDI. 

Usando o CDB como referência, calculamos o LCI/ LCA que tem rendimento equivalente ao CDB selecionado.
Posteriormente damos a opção de comparar os dois investimentos em um prazo de 2 anos. Na última seção explico brevemente como usar corretamente a aplicação.

Segue o link para a aplicação: [comparador_de_investimentos](https://comparador-investimentos.streamlit.app/)

## CDB *versus* LCI/ LCA

Neste trabalho, estamos comparando somente os investimentos pós-fixados atrelados ao CDI. Então, ambos rendem um percentual do CDI. No momento do desenvolvimento do texto, a taxa do CDI estimada para 2024 era de 12.86% ao ano (https://calculadorarendafixa.com.br/). Esta taxa está sendo utilizada na aplicação para a construção do gráfico. 

O rendimento dos títulos estudados é diário e ocorre somente em dias úteis mas a liquidez pode ser diária ou somente no dia do vencimento. Para quem investe, a principal diferença entre o CDB e o LCI/ LCA é a incidência de imposto de renda. Enquanto o LCI/ LCA é isento do imposto, o CDB tem um imposto cobrado sobre o rendimento. A cobrança é inversamente proporcional ao tempo que o dinheiro fica aplicado, como vemos na tabela abaixo:

| DIAS       | IMPOSTO | 
| ---------- | ------  |
| até 180    | 22.5 %  |
| 181 - 360  | 22.0 %  | 
| 361 - 720  | 17.5 %  | 
| mais de 721| 15.0 %  |

## Objetivo

O objetivo deste trabalho é comparar um investimento em  CDB com um em LCI ou LCA. Quando nos deparamos com duas ofertas de títulos, como exemplo, um CDB rendendo 110% do CDI e um LCI rendendo 90% do CDI, qual é a melhor opção? Apesar do CDB ter um rendimento bruto maior, há incidência regressiva de imposto. A pergunta não é simples de responder.

Pensando nisso, desenvolvemos uma aplicação capaz de calcular a partir de uma oferta de CDB, qual seria a oferta com rendimento líquido equivalente para um LCI ou LCA. Com base na expressões fornecidas por um banco de investimentos, escrevemos as expressões para o rendimento do CDB e para o rendimento do LCI/ LCA. Igualando as duas expressões, consiguimos obter uma curva de equivalência considerando a duração do investimento. Essa equivalência independe do valor da taxa do CDI.

## Como usar a aplicação

Insira as datas inicial e final do investimento desejado. Depois disso, escolha o percentual de rendimento do CDB. Uma caixa de informação te dirá qual o precentual de rendimento de um LCI equivale ao investimento do CDB em rendimento líquido.

Caso queira comparar a evolução do rendimento dos dois títulos por um prazo de 2 anos, clique no botão correspondente. Um gráfico será gerado mostrando a evolução do rendimento dos investimentos ao longo do tempo.

***
**AVISO**: Este trabalho tem fins meramente didáticos, não devendo ser considerado como orientação de investimento. Não nos responsabilisamos por quaisquer decisões que sejam tomadas com base neste comparador. Sempre busque a orientação de um consultor financeiro antes de tomar suas decisões de investimento.
***

MP-resuldados

Dos dados aos resultados. Um pouco de física, matemática, negócios e finanças.


