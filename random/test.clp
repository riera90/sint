(defmodule A)

(assert
	(dato 55)
)

(defrule busca55
	(dato 55)
	=>
	(assert
		(found true)
	)
)
