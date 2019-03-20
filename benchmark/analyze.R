CLIENT = 1
primary = '#1A9988'
highlight = '#EB5600'

clients <- list(rep(CLIENT,8))
transactions <- c(1, 15 , 30, 45, 60, 75, 90, 100)
latency <- c() 
tps1 <- c()
tps2 <- c()

for (i in transactions) {
	path = paste('./outs/out_', toString(CLIENT), 'x', toString(i),'.csv', sep="")
	a = read.csv(path, header=FALSE)
	latency  <- append(latency, a$V1)
	tps1 <- append(tps1, a$V2)
	tps2 <- append(tps2, a$V3)
}
(latency)
(tps1)
(tps2)

x = transactions
y = tps1

plot(x, y,
     xlab = 'Quandidade de Transações',
     ylab = 'Transações por segundo (excluindo tempo de conexão)',
	 # Simbolos
     pch = 19,
	 # Numero de pelo qual a largura deve escalar relativo ao tamanho normal 
     cex = 1.5,
     col = highlight)

# Calculo do coeficiente de correlacao
(cor_coeff <- cor(x, y))

# Obtendo modelo linear ajustado
r <- lm(y ~ x)
summary(r)

# Reta de regressao a partir de modelo linear
abline(r, col = primary)

# Obtencao de residuos e preditos atraves de modelo linear
pre <- predict(r)
res <- signif(residuals(r), 5)

# Plot dos valores preditos
points(x, pre,
       pch = 19,
       cex = 1.5,
       col = primary) 

# Adicional: representacao grafica dos residuos e seus
# respectivos valores       
segments(x, y, y1 = pre, col = primary)

text(x, y, signif(res, 4), pos = 2)
