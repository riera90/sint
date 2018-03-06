(deffacts initial-fact-pers
	(dato 1)
	(dato 2)
	(dato azul)
	(dato "saludos")
	(new)
	(all_datos)
)


(defrule init_
	(new)
	?f1 <- (new)
	=>
	(retract ?f1)
	(facts)
	(printout t "test" crlf)
)

(defrule recopilar-datos
	?f1 <- (dato ?var1)
	?f2 <- (all_datos $?var2)
	=>
	(retract ?f1)
	(retract ?f2)
	(printout t "inserting: " ?var1 crlf)
	(assert (all_datos $?var2 ?var1))
)
