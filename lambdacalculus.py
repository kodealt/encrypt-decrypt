#FUCK LAMBDA CALCULUS (ive never taken calculus before)

#BOOLEAN
TRUE = lambda x: lambda y: x
FALSE = lambda x: lambda y: y

#IF/ELSE
IF = lambda cond: lambda x: lambda y: cond(x)(y)

#LOGIC
AND = lambda p: lambda q: p(q)(FALSE)
OR = lambda p: lambda q: p(TRUE)(q)
NOT = lambda p: p(FALSE)(TRUE)

#NUMBERS (CHURCH ENCODING)
ZERO = lambda f: lambda x: x
ONE = lambda f: lambda x: f(x)
TWO = lambda f: lambda x: f(f(x))

  #SUCCESSOR (n+1)
SUCC = lambda n: lambda f: lambda x: f(n(f)(x))

#RECURSIVE
Y = lambda f: (lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y)))

  #FACTORIAL WITH 'Y'
FACT = Y(lambda f: lambda n: IF(n == 0)(lambda: 1)(lambda: n * f(n - 1))())


"##FUN = FUNCTION"

"##IF"

#       bools are of the [AND]
#           ▼
#   cond;<bool;                    if cond wrong
#   ▼     ▼                              ▼
#IF(AND(TRUE)(FALSE))("TRUE & FALSE")("FALSE")
#▲              ▲           ▲
#fuction;     bool>;  condition met


##AND, with help of [IF]


#AND(TRUE)(FALSE)
