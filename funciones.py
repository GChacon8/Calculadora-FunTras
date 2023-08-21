from mpmath import *
tolerancia= 1e-8
iteraciones= 2500

def div_t(a, iterMax, tol):
    sk = 2.2204e-16

    if a == 0:
        return "La división entre 0 no esta definida"
    elif abs(a) >= fac(100):
        return 0
    elif fac(80) < abs(a):
        sk **= 15
    elif fac(60) < abs(a):
        sk **= 11
    elif fac(40) < abs(a):
        sk **= 8
    elif fac(20) < abs(a):
        sk **= 4
    else:
        sk **= 2
    
    for i in range(iterMax):
        sk_n = sk*(2 - a * sk)
        err = abs(sk_n - sk)
        sk = sk_n
        if err < tol*sk:
            return (float(sk), float(err), i)
    return (float(sk), float(err), iterMax)
   


def exp_t(a, iterMax, tol):
    """
    La funcion exp_t aproxima el valor de e^a
    Sintaxis de la funcion: [sk,error,n]=exp_t(a,iterMax,tol)
    Parometros de entrada:
            a = nomero real
            iterMax = nomero entero positivo, que representa la cantidad de iteraciones moximas del motodo
            tol =  nomero real positivo, que es el criterio de parada del error, donde |S_(k+1)-S_(k)|<tol
    Parometros de salida:
            sk = aproximacion del valor e^a
            er = error dado por la formula |S_(k+1)-S_(k)|
            k = cantidad de iteraciones realizadas
    """
    sk = 0
    for i in range(iterMax):
        div= div_t(fac(i), iterMax, tolerancia)
        if isinstance(div, tuple):
            div= div[0]
        sk_n = sk + a**(i) * div
        err = abs(sk_n-sk)
        sk = sk_n
        if err < tol:
            return (float(sk), float(err), i)
    return (float(sk), float(err), iterMax)


def sin_t(a, iterMax, tol):
    """
    La función sin_t aproxima el valor de sin(a)
    Sintaxis de la función: sin_t(a, iterMax, tol)
    Parametros de entrada: 
               a = numero real
               iterMax= numero entero positivo, que representa la cantida de itereaciones maximas del metodo
               tol= numero real positivo, que es el criterio de parada del error, donde S_(k+1)-S_(k)|<tol
    Parametros de salida:
               sk= aproximación del valor sin(a)
               err= error dado por la formula S_(k+1)-S_(k)|<tol
               k= cantidad de iteraciones
    """
    if a>2*pi:
        while a>2*pi:
            a-=2*pi
    elif a<-(2*pi):
        while a<-(2*pi):
            a+=2*pi
    sk= 0

    for i in range(iterMax):
        div= div_t(fac(2*i+1), iterMax, tol)
        if isinstance(div, tuple):
            div= div[0]
        sk_n= sk + ((-1)**i) * (a**(2*i+1)) * div
        err = abs(sk_n-sk)
        sk = sk_n
        if err < tol:
            return (float(sk), float(err), i)
    return (float(sk), float(err), iterMax)



def cos_t(a, iterMax, tol):
    """
    La función cos_t aproxima el valor de cos(a)
    Sintaxis de la función: (sk, err, n)=cos_t(a, iterMax, tol)
    Parametros de entrada: 
               a = numero real
               iterMax= numero entero positivo, que representa la cantida de itereaciones maximas del metodo
               tol= numero real positivo, que es el criterio de parada del error, donde S_(k+1)-S_(k)|<tol
    Parametros de salida:
               sk= aproximación del valor cos(a)
               err= error dado por la formula S_(k+1)-S_(k)|<tol
               k= cantidad de iteraciones
    """
    if a>2*pi:
        while a>2*pi:
            a-=2*pi
    elif a<-(2*pi):
        while a<-(2*pi):
            a+=2*pi
    sk=0

    for i in range(iterMax):
        div= div_t(fac(2*i), iterMax, tol)
        if isinstance(div, tuple):
            div= div[0]
        sk_n =  sk + ((-1)**i) * (a**(2*i)) * div
        err = abs(sk_n-sk)
        sk = sk_n
        if err < tol:
            return (float(sk), float(err), i)
    return (float(sk), float(err), iterMax)

def tan_t(a, iterMax, tol):
    """
    La función tan_t aproxima el valor de tan(a)
    Sintaxis de la función: (sk, err, n)=tan_t(a, iterMax, tol)
    Parametros de entrada: 
               a = numero real
               iterMax= numero entero positivo, que representa la cantida de itereaciones maximas del metodo
               tol= numero real positivo, que es el criterio de parada del error, donde S_(k+1)-S_(k)|<tol
    Parametros de salida:
               sk= aproximación del valor tan(a)
               err= error dado por la formula S_(k+1)-S_(k)|<tol
               k= cantidad de iteraciones
    """
    numerador= sin_t(a, iterMax, tol)
    denominador= cos_t(a, iterMax, tol)
    div= div_t(denominador[0], iterMax, tol)
    sk= numerador[0]*div[0]
    list_err= [numerador[1], denominador[1], div[1]]
    err= max(list_err)
    k= numerador[2] + denominador[2] + div[2]

    return (sk, err, k) 

def in_t(a, iterMax, tol):
    """
    La función in_t aproxima el valor de In(a)
    Sintaxis de la función: (sk, err, n)=in_t(a, iterMax, tol)
    Parametros de entrada: 
               a = numero real
               iterMax= numero entero positivo, que representa la cantida de itereaciones maximas del metodo
               tol= numero real positivo, que es el criterio de parada del error, donde S_(k+1)-S_(k)|<tol
    Parametros de salida:
               sk= aproximación del valor In(a)
               err= error dado por la formula S_(k+1)-S_(k)|<tol
               k= cantidad de iteraciones
    """
    if a<=0:
        return "Error de Calculo"
    sk=0
    const= (2*(a-1))/(a+1)

    for i in range(iterMax):
        div1= div_t((2*i+1), iterMax, tol)
        if isinstance(div1, tuple):
            div1= div1[0]
        div2= div_t(a+1, iterMax, tol)
        
        if isinstance(div2, tuple):
            div2= div2[0]

        sk_n = sk + 1* div1 * ((a-1)*div2)**(2*i)
        err = abs(sk_n - sk)
        sk = sk_n
        if err < tol:
            sk=sk_n*const
            return (float(sk), float(err), i)
            
    sk= sk_n*const

    return (float(sk), float(err), iterMax)

def log_t(a, b, iterMax, tol):
    """
    La función log_t aproxima el valor de logb(a)
    Sintaxis de la función: (sk, err, n)=log_t(a, b, iterMax, tol)
    Parametros de entrada: 
               a = numero real
               b = numero real
               iterMax= numero entero positivo, que representa la cantida de itereaciones maximas del metodo
               tol= numero real positivo, que es el criterio de parada del error, donde S_(k+1)-S_(k)|<tol
    Parametros de salida:
               sk= aproximación del valor logb(a)
               err= error dado por la formula S_(k+1)-S_(k)|<tol
               k= cantidad de iteraciones
    """
    if a <= 0 or b <= 0 or b == 1:
        return "Error de Calculo"

    numerador= in_t(a, iterMax, tol)
    denominador= in_t(b, iterMax, tol)
    div= div_t(denominador[0], iterMax, tol)
    sk= numerador[0]*div[0]
    list_err= [numerador[1], denominador[1], div[1]]
    err= max(list_err)
    k= numerador[2] + denominador[2] + div[2]

    return (sk, err, k) 


def sinh_t(a, iterMax, tol):
    """
    La función sinh_t aproxima el valor de sinh(a)
    Sintaxis de la función: (sk, err, n)=sinh_t(a, iterMax, tol)
    Parametros de entrada: 
               a = numero real
               iterMax= numero entero positivo, que representa la cantida de itereaciones maximas del metodo
               tol= numero real positivo, que es el criterio de parada del error, donde S_(k+1)-S_(k)|<tol
    Parametros de salida:
               sk= aproximación del valor sinh(a)
               err= error dado por la formula S_(k+1)-S_(k)|<tol
               k= cantidad de iteraciones
    """
    sk=0

    for i in range(iterMax):
        div= div_t(fac(2*i+1), iterMax, tol)
        if isinstance(div, tuple):
            div= div[0]
        sk_n = sk + (a**(2*i+1)) * div
        err = abs(sk_n - sk)
        sk = sk_n
        if err < tol:
            return (float(sk), float(err), i)
    return (float(sk), float(err), iterMax)


def cosh_t(a, iterMax, tol):
    """
    La función cosh_t aproxima el valor de cosh(a)
    Sintaxis de la función: (sk, err, n)=cosh_t(a, iterMax, tol)
    Parametros de entrada: 
               a = numero real
               iterMax= numero entero positivo, que representa la cantida de itereaciones maximas del metodo
               tol= numero real positivo, que es el criterio de parada del error, donde S_(k+1)-S_(k)|<tol
    Parametros de salida:
               sk= aproximación del valor cosh(a)
               err= error dado por la formula S_(k+1)-S_(k)|<tol
               k= cantidad de iteraciones
    """
    sk=0

    for i in range(iterMax):
        div= div_t(fac(2*i), iterMax, tol)
        if isinstance(div, tuple):
            div= div[0]
        sk_n = sk + (a**(2*i)) * div
        err = abs(sk_n - sk)
        sk = sk_n
        if err < tol:
            return (float(sk), float(err), i)
    return (float(sk), float(err), iterMax)

def tanh_t(a, iterMax, tol):
    """
    La función tanh_t aproxima el valor de tanh(a)
    Sintaxis de la función: (sk, err, n)=tanh_t(a, iterMax, tol)
    Parametros de entrada: 
               a = numero real
               iterMax= numero entero positivo, que representa la cantida de itereaciones maximas del metodo
               tol= numero real positivo, que es el criterio de parada del error, donde S_(k+1)-S_(k)|<tol
    Parametros de salida:
               sk= aproximación del valor tanh(a)
               err= error dado por la formula S_(k+1)-S_(k)|<tol
               k= cantidad de iteraciones
    """
    numerador= sinh_t(a, iterMax, tol)
    denominador= cosh_t(a, iterMax, tol)
    div= div_t(denominador[0], iterMax, tol)
    sk= numerador[0]* div[0]
    list_err= [numerador[1], denominador[1], div[1]]
    err= max(list_err)
    k= numerador[2] + denominador[2] + div[2]

    return (sk, err, k) 


def asin_t(a, iterMax, tol):
    """
    La función asin_t aproxima el valor de sin^-1(a)
    Sintaxis de la función: asin_t(a, iterMax, tol)
    Parametros de entrada: 
               a = numero real
               iterMax= numero entero positivo, que representa la cantida de itereaciones maximas del metodo
               tol= numero real positivo, que es el criterio de parada del error, donde S_(k+1)-S_(k)|<tol
    Parametros de salida:
               sk= aproximación del valor sin^-1(a)
               err= error dado por la formula S_(k+1)-S_(k)|<tol
               k= cantidad de iteraciones
    """
    if not(-1<=a<=1):
        return "Error de Calculo"
        
    sk=0

    for i in range(iterMax):
        numerador= fac(2*i)*(a**(2*i+1))
        denominador= (4**i)*(fac(i)**2)*(2*i+1)
        div= div_t(denominador, iterMax, tol)
        if isinstance(div, tuple):
            div= div[0]
        sk_n = sk + numerador * div
        err = abs(sk_n - sk)
        sk = sk_n
        if err < tol:
            return (float(sk), float(err), i)
    return (float(sk), float(err), iterMax)

def acos_t(a, iterMax, tol):
    """
    La función acos_t aproxima el valor de cos^-1(a)
    Sintaxis de la función: acos_t(a, iterMax, tol)
    Parametros de entrada: 
               a = numero real
               iterMax= numero entero positivo, que representa la cantida de itereaciones maximas del metodo
               tol= numero real positivo, que es el criterio de parada del error, donde S_(k+1)-S_(k)|<tol
    Parametros de salida:
               sk= aproximación del valor cos^-1(a)
               err= error dado por la formula S_(k+1)-S_(k)|<tol
               k= cantidad de iteraciones
    """
 
    if not(-1<=a<=1):
        return "Error de Calculo"
    resultados= asin_t(a, iterMax, tol)
    sk= pi*div_t(2, iterMax, tol)[0] - resultados[0]
    err= resultados[1]
    i= resultados[2]
    return (float(sk), err, i)

def atan_t(a, iterMax, tol):
    """
    La función atan_t aproxima el valor de tan^-1(a)
    Sintaxis de la función: atan_t(a, iterMax, tol)
    Parametros de entrada: 
               a = numero real
               iterMax= numero entero positivo, que representa la cantida de itereaciones maximas del metodo
               tol= numero real positivo, que es el criterio de parada del error, donde S_(k+1)-S_(k)|<tol
    Parametros de salida:
               sk= aproximación del valor tan^-1(a)
               err= error dado por la formula S_(k+1)-S_(k)|<tol
               k= cantidad de iteraciones
    """
    sk=0
    const= pi*div_t(2, iterMax, tol)
    if -1<=a<=1:
        for i in range(iterMax):
            numerador= ((-1)**i) * (a**(2*i+1))
            denominador= div_t(2*i+1, iterMax, tol)[0]
            sk_n = sk + numerador * denominador 
            err = abs(sk_n - sk)
            sk = sk_n
            if err < tol:
                return (float(sk), float(err), i)
        return (float(sk), float(err), iterMax)
    else:
        i= 0
        temp = abs(a)
        for i in range(iterMax):
            numerador= ((-1)**i)
            denominador= (2*i+1)*(temp**(2*i+1))
            sk_n = sk +  numerador * div_t(denominador, iterMax, tol)[0]
            err = abs(sk_n - sk)
            sk = sk_n
            if err < tol:
                break
            
        if a<-1:
            sk= (const - sk_n)*-1
            return (float(sk), float(err), i+1)
        else:
            sk= const - sk_n
            return (float(sk), float(err), i+1)

def root_t(a, p, iterMax, tol):
    """
    La función root_t aproxima el valor de a^(1/p)
    Sintaxis de la función: root_t(a, p, iterMax, tol)
    Parametros de entrada: 
               a = numero real positvo
               p= numero entero positivo
               iterMax= numero entero positivo, que representa la cantida de itereaciones maximas del metodo
               tol= numero real positivo, que es el criterio de parada del error, donde S_(k+1)-S_(k)|<tol
    Parametros de salida:
               sk= aproximación del valor a^(1/p)
               err= error dado por la formula S_(k+1)-S_(k)|<tol
               k= cantidad de iteraciones
    """
    sk= a * div_t(2, iterMax, tol)[0]

    if a<0 and p%2==0:
        return "Error de Calculo"

    for i in range(iterMax):
        numerador= sk**p - a
        denomidaor= div_t(p * (sk**(p-1)), iterMax, tol)[0]
        sk_n = sk - numerador * denomidaor
        err = abs(sk_n -sk )
        sk = sk_n
        if err < tol:
            return (float(sk), float(err), i)
    return (float(sk), float(err), iterMax)

def sec_t(a, iterMax, tol):
    """
    La función sec_t aproxima el valor de sec(a)
    Sintaxis de la función: (sk, err, n)=sec_t(a, iterMax, tol)
    Parametros de entrada: 
               a = numero real
               iterMax= numero entero positivo, que representa la cantida de itereaciones maximas del metodo
               tol= numero real positivo, que es el criterio de parada del error, donde S_(k+1)-S_(k)|<tol
    Parametros de salida:
               sk= aproximación del valor sec(a)
               err= error dado por la formula S_(k+1)-S_(k)|<tol
               k= cantidad de iteraciones
    """
    denominador= cos_t(a, iterMax, tol)
    if denominador[0] == 0:
        return "Error de calculo"
    div= div_t(denominador[0], iterMax, tol)
    sk= div[0]
    list_err= [denominador[1], div[1]]
    err= max(list_err)
    k= denominador[2] + div[2]
    return (sk, err, k)

def csc_t(a, iterMax, tol):
    """
    La función csc_t aproxima el valor de csc(a)
    Sintaxis de la función: (sk, err, n)=csc_t(a, iterMax, tol)
    Parametros de entrada: 
               a = numero real
               iterMax= numero entero positivo, que representa la cantida de itereaciones maximas del metodo
               tol= numero real positivo, que es el criterio de parada del error, donde S_(k+1)-S_(k)|<tol
    Parametros de salida:
               sk= aproximación del valor csc(a)
               err= error dado por la formula S_(k+1)-S_(k)|<tol
               k= cantidad de iteraciones
    """
    denominador= sin_t(a, iterMax, tol)
    if denominador[0] == 0:
        return "Error de calculo"
    div= div_t(denominador[0], iterMax, tol)
    sk= div[0]
    list_err= [denominador[1], div[1]]
    err= max(list_err)
    k= denominador[2] + div[2]
    return (sk, err, k)

def cot_t(a, iterMax, tol):
    """
    La función sec_t aproxima el valor de sec(a)
    Sintaxis de la función: (sk, err, n)=sec_t(a, iterMax, tol)
    Parametros de entrada: 
               a = numero real
               iterMax= numero entero positivo, que representa la cantida de itereaciones maximas del metodo
               tol= numero real positivo, que es el criterio de parada del error, donde S_(k+1)-S_(k)|<tol
    Parametros de salida:
               sk= aproximación del valor sec(a)
               err= error dado por la formula S_(k+1)-S_(k)|<tol
               k= cantidad de iteraciones
    """
    denominador= tan_t(a, iterMax, tol)
    if denominador[0] == 0:
        return "Error de calculo"
    div= div_t(denominador[0], iterMax, tol)
    sk= div[0]
    list_err= [denominador[1], div[1]]
    err= max(list_err)
    k= denominador[2] + div[2]
    return (sk, err, k)

def power_t(a, b):
    """
    La función power_t calcula el valor de a^b
    Sintaxis de la función: power_t(a, b)
    Parametros de entrada: 
               a = numero real
               b = numero entero
    Parametros de salida:
               sk= valor de a^b
            
    """
    if (a==0 and b==0) or a <= 0 and not isinstance(b, int):
        return "Error de Calculo"
    sk=1

    for i in range(int(b)):
        sk*=a
    return sk

def sqrt_t(a, iterMax, tol):
    """
    La función sqrt_t aproxima el valor de a^(1/2)
    Sintaxis de la función: sqrt_t(a, iterMax, tol)
    Parametros de entrada: 
               a = numero real
               iterMax= numero entero positivo, que representa la cantida de itereaciones maximas del metodo
               tol= numero real positivo, que es el criterio de parada del error, donde S_(k+1)-S_(k)|<tol
    Parametros de salida:
               sk= aproximación del valor a^(1/2)
               err= error dado por la formula S_(k+1)-S_(k)|<tol
               k= cantidad de iteraciones
    """
    resultado= root_t(a, 2, iterMax, tol)
    if isinstance(resultado, tuple):
            sk= resultado[0]
    else:
        sk= resultado
    err= resultado[1]
    k= resultado[2]

    return (sk, err, k)

print(cos_t(-120, iteraciones, tolerancia))
