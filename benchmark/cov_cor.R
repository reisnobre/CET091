##Alunos: Valter Barbosa, adonioas Alcantara e Gleisson carillo


## M: Rendimento academico em Matematica
## L: Rendimento academico em Linguas

primary = '#1A9988'
highlight = '#EB5600'

M <- c(5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65)

L <- c(2.75, 5.50, 8.25, 11, 13.75, 16.5, 19.25, 22, 24.75, 27.5, 30.25, 33, 35.75)


## visualizacao grafica das variáveis
## aleatórias em um diagrama de dispersão
plot(L ~ M,
     col = primary,
     pch = 19)

segments(mean(M),
         min(L),
         mean(M),
         max(L),
         col = highlight)

text(x = mean(M),
     y = max(L),
     lab = 'Mean (M)')

segments(min(M),
         mean(L),
         max(M),
         mean(L),
         col=primary)

text(x = min(M) + 1,
     y = mean(L) + 1,
     lab = 'Mean (L)')

## Covariancia
cov(M, L)

## calculando a correlacao usando a formula fundamental:
## r = cov(a,b) / sd(a) * sd(b)
(cov(M, L) / (sd(M) * sd(L)))

## calculando a correlção usando função do R
cor(M, L)

## Verificacao da influencia da unidade de medida na covariancia
cov(M, L)

L2 <- L * 100

cov(M, L2)

## Verificando que isto não influencia a correlacao linear simples:
cor(M, L)

cor(M, L2)

## Adicional: Traçar reta de regressao
abline(lm(L ~ M))
