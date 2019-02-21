(deffacts h1
	(dato 2)
	(dato 4)
	(dato 3)
)

(defrule multiplicar
	(dato ?x)
	=>
	(assert
		(resultado (* ?x 2))
	)
)
