(deffacts initial-fact-pers
	(dato 1)
	(dato 2)
	(dato azul)
	(dato "saludos")
	(new)
)


(defrule init
	(new)
	?f1 <- (new)
	=>
	(retract ?f1)
	(facts)
	(printout t "test" crlf)
)

(defrule recopilar-datos
	($?f2 $?f1)
	=>
	(assert (todos-los-datos $?f1))
	(printout t "datos: " $?f1 crlf)
)
