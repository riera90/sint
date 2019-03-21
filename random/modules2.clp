; ===============================================
; Uso de modulos para crear programa interactivo
;
; (C) mjmarin/2016
; ===============================================

; -----------
; Modulo MAIN
; -----------
(defmodule MAIN (export ?ALL))

(deffacts control-foco
 (secuencia-fases CAPTURAR PROCESAR REPETIR))
 
(defrule cambio-fase
 ?s <- (secuencia-fases ?siguiente $?resto)
 =>
 (retract ?s)
 (focus ?siguiente)
 (assert (secuencia-fases $?resto ?siguiente)))
 
; --------------- 
; MODULO CAPTURAR
; ---------------
(defmodule CAPTURAR (export deftemplate ?ALL) ; Que hechos hay que exportar?
   (import MAIN deftemplate initial-fact)
)

(defrule pedir-x1
   (not (x1 ?))
 =>
	(printout t "introduzca x1" crlf)
	(assert (x1 (read)))
)

(defrule pedir-x2
   (not (x2 ?))
 =>
	(printout t "introduzca x1" crlf)
	(assert (x2 (read)))   
)

; ---------------
; MODULO PROCESAR
; ---------------
(defmodule PROCESAR (import CAPTURAR deftemplate ?ALL)
)

(defrule sumar-valores
  ?fx1 <- (x1 ?x1)
  ?fx2 <- (x2 ?x2)
 =>
  (assert (resultado (+ ?x1 ?x2)))  
)

(defrule print-res
	?f1<-(resultado ?r)
	=>
	(printout t "resultado: " ?r crlf)
)

; --------------
; MODULO REPETIR
; --------------
(defmodule REPETIR (import MAIN ?ALL)
                      (import CAPTURAR deftemplate ?ALL))

(defrule pedir-repeticion
  (not (repeticion ?))
 => 
  (printout t crlf "¿Otra operacion? (s/n) ")
  (assert (repeticion (read))))
  
(defrule repetir-pedir-repeticion
  ?r <- (repeticion ~s&~n)
 =>
 (retract ?r)
 (printout t "Responda 's' o 'n'." crlf))

(defrule repeticion-si
  ?rep <- (repeticion s)
  ?x1 <- (x1 ?) 
  ?x2 <- (x2 ?)
 =>
  (retract ?rep ?x1 ?x2)
  (return))

(defrule repeticion-no
  ?rep <- (repeticion n)
  ?sec <- (secuencia-fases $?)
 =>
  (retract ?rep ?sec)
  (return))

