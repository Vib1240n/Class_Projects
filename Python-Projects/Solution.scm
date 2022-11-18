(define (incn e)
(Lambda (x)
(+ x e)))

((incn 3)2)