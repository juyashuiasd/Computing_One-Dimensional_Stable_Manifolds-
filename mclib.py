from math import *
from vector import *
from point import *
from plot import *

d = dict()

def initialize():
    functions = ["Ikeda","Henon","Mira","Input"]
    
    l = [
        "alpha_min", "alpha_max", "delta_alpha_min",
        "delta_alpha_max", "delta_min",
        "convergence", "bisection_error", "iteration_max"
        ]
    values = [
            0.2, 0.3, 10**-6,
            10**-5, 10**-4,
            10, 10**-6, 10
            ]
    print("The parameters with the default values are:")
    print("Parameter\t   Default Value")
    
    for p in l:
        print("{}\t   {}".format(p,values[l.index(p)]))
    
    option = input("Do you want to change the values? (Y/N)\n")
    while not (option == 'Y'    or option == 'N'
               or option == 'y' or option == 'n'):
        option = input("Error, enter Y for change values and N for use the default values\n")
    if option in "yY":
        for p in l:
            while True:
                try:
                    value = input("Enter new float value for {} parameter:\n".format(p))
                    d[p] = float(value)
                except ValueError:
                    print("ERROR: not valid value {} parameter\n".format(p))
                    continue
                break
        print("The parameters have been initilized")
        print("Parameter\t   Default Value")
        for p in l:
            print("{}\t   {}".format(p,d[p]))
    else:
        for p in l:
            j = l.index(p)
            try:
                d[p] = float(values[j])
            except ValueError:
                print("ERROR: not valid value {} parameter\n".format(p))
                continue

    function, it = 0, 0
    while True:
        try:
            it = it + 1
            if it > 1:
                function = int(input("Please, enter a correct int value in the following range: [1,{}]\n".format(len(functions))))
            else:
                print("Select one of the following functions:")
                for i in range(len(functions)):
                    print("{}. {}".format(i + 1,functions[i]))
                function = int(input())
            if function > 0 and function <= len(functions):
                break
        except ValueError:
            continue
        
    print("Function selected: {}".format(functions[function - 1]))
    
    return d, functions[function - 1]

def initialize2():
    l = [
        "alpha_min", "alpha_max", "delta_alpha_min",
        "delta_alpha_max", "delta_min", "epsilon",
        "convergence", "bisection_error", "iteration_max"
        ]
    values = [
            0.2, 0.3, 10**-6,
            10**-5, 10**-4, 10,
            10, 10**-6, 10
            ]
    
    
    for p in l:
        #s = "Enter {}:\n".format(p)
        #while True:
        for i in range(1):
            j = l.index(p)
            try:
                #d[p] = float(input(s))
                d[p] = values[j]
            except ValueError:
                print("ERROR: not valid value {} parameter".format(p))
                continue
            break
    return d

def grow_manifold(d,p0,p1,A):
    def alpha_calculator(pk_m1,pk,pk_p1):
        praya = pk + (pk.distance(pk_m1)/pk_p1.distance(pk))*(pk-pk_p1)
        #resultado1 = 2*asin(praya.distance(pk_m1)/(2*pk.distance(pk_m1)))
        resultado2 = praya.distance(pk_m1)/pk.distance(pk_m1)
        return resultado2
        
        
    d["M"] = [p0,p1] #Añadimos al diccionario p0 y p1
    d["p_left"]  = p0 #Empezamos el algoritmo con el punto p0 y p1
    d["p_right"] = p1 
    arc_length = p0.distance(p1) #Calculamos la distancia entre p1 y p0
    
    while(arc_length < A): #Mientras que la longitud que calculamos sea menor que la que queremos
        pk = d["M"][-1] #Punto para calcular ángulo
        pk_m1 = d["M"][-2] #Punto para calcular ángulo
        p_candidate = search_circle(d) #Buscamos el nuevo p_candidato
        if p_candidate == "None":
            return "None"
        
        
        alpha_k = alpha_calculator(pk_m1,pk,p_candidate) #Ángulo entre pk_m1, p_k y p_candidato
        if ((alpha_k < d["alpha_max"]
            and d["delta_k"]*alpha_k < d["delta_alpha_max"])
            or  d["delta_k"] < d["delta_min"]): #Dos condiciones generales
            
            d["M"].append(p_candidate) #Añadimos el punto a M
            arc_length = arc_length + d["delta_k"] #Aumentamos la longitud
            print("Longitud: {}".format(arc_length))

            if (alpha_k < d["alpha_min"]
                and d["delta_k"]*alpha_k < d["delta_alpha_min"]): #Condición para aumentar delta_k
            
                d["delta_k"] = 2 * d["delta_k"] #Si se cumple se aumenta delta_k en 2
        else: #Si no se cumple ninguna de las condiciones
            d["delta_k"] = d["delta_k"]/2 #Se divide delta_k entre 2
    return d["M"] #Al terminar el bucle y sin fallos se devuelve d["M"]

def search_circle(d):
    def move(tau):
        if tau < 0: #Si tau < 0, retrocedemos hacia atras
            i = d["M"].index(d["p_right"])
            if i - 1 == 0: #Condición de fallo
                return "None"
            i = d["M"].index(d["p_left"]) #Index del punto en M
            d["p_right"] = d["p_left"] #p_rigth es p_left
            d["p_left"]  = d["M"][i-1] #p_left es p_left-1
            return tau
        elif tau > 1: #Si tau > 1, avanzamos hacia adelante
            i = d["M"].index(d["p_right"]) #index del punto en M
            if i + 1 == len(d["M"]): #Condición de fallo
                return "None"
                
            d["p_left"] = d["p_right"] #p_left es p_rigth
            d["p_right"]  = d["M"][i+1] #p_rigth es p_rigth+1
            return tau
            
            
    
    p_candidate, tau = find_point_on_line(d) #Buscamos el p_candidato y el tau respecto al segmento
    d["tau_a"] = tau #Comprobar que no se produce bucle
    if tau == "None":
        return "None"
        
    
    while tau < 0 or tau > 1: #Si el tau es < 0 o > 1 entonces no se encuentra en la recta calculada
        tau = move(tau) #Rutina para moverse entre los puntos
        if tau == "None":
            return "None"
        
        p_candidate, tau = find_point_on_line(d) #Nueva búsqueda de p_candidato y tau para cumplir condicón
        
        if tau == "None":
            return "None"
        if (d["tau_a"] < 0 and tau > 1) or (d["tau_a"] > 1 and tau < 0):
            return "None"
        d["tau_a"] = tau
    return p_candidate #Cuando el tau cumple las condiciones, se devuelve el p_candidato
        
def find_point_on_line(d):
    
    def find_ps_pe(sigma, O_start, O_end):
        beta = sigma+O_start #Ángulo respecto a X más alpha_max
        gamma = sigma + O_end #Ángulo respecto a X menos alpha_max
        betax,gammax = round(beta,10),round(gamma+2*pi,10)
        if betax == gammax: #Condición general de salida de bucle
            return "None","None","None","None"
        p_start = d["M"][-1]+ movimiento(d["delta_k"],beta) #Punto calculado con pk añadiendo vector rotado hacia beta
        p_end = d["M"][-1] + movimiento(d["delta_k"],gamma) #Punto calculado con pk añadiendo vector rotado hacia gamma
        
        return p_start, p_end, beta, gamma
    
    def find_Vs_Ve(p_start, p_end):
        V_start = Vector(f(p_start), d["p_right"]) #Vector de la imagen de p_Start con p_right
        V_end   = Vector(f(p_end)  , d["p_right"]) #Vector con al imagen de p_end con p_right
        return V_start, V_end    
    
    def find_p_try(O_try):
            return d["M"][-1] + movimiento(d["delta_k"],O_try)
    
    def find_all(sigma, O_start, O_end):
        p_start, p_end, beta, gamma = find_ps_pe(sigma, O_start, O_end) #Búsqueda de los puntos límite y ángulos
        if beta == "None":
            return "None","None","None","None","None","None","None"
        V_start, V_end = find_Vs_Ve(p_start, p_end) #Cálculo de vectores
        W              = Vector(d["p_left"], d["p_right"]) #Vector de p_left y p_right
        W              = Vector(-W.y, W.x) #Vector nromal de p_left y p_right
        return p_start, p_end, beta, gamma, V_start, V_end, W 
    
    def calc_tau(cut_point): #Esta función cálculo el punto de corte
        p1 = d["p_left"]
        p2 = d["p_right"]
        if p1.x == p2.x:
            return (cut_point.y - p1.y)/(p2.y - p1.y)
        return (cut_point.x - p1.x)/(p2.x - p1.x)
    
    def calc_AB(vector, point): #Cálculo del a,b de la recta con la forma y = ax+b
        if vector.x == 0:
            return point.x,"NR"
        a = vector.y/vector.x
        b = point.y - a*point.x
        return a, b
    
    def dist_line_point(a,b,point): #Distancia de un punto respecto a una línea
        if b == "NR":
            return abs(point.x-a)
        return abs(a * point.x - point.y + b)/sqrt(a**2 + 1)
    
    def dist_line_point_sign(a, b, point): #Signo respecto a distancia del punto a una línea
        # y = a*x + b
        if b == "NR":
            return point.x-a
        y = a*point.x + b
        dist = point.y - y
        return dist
        
        
    def calc_error(p_try): #Se calcula el error
        # Una línea reta se define por y = a * x + b
        p_left, p_right = d["p_left"],d["p_right"]
        V         = Vector(p_left, p_right)
        a, b      = calc_AB(V, p_left)
        f_p_try   = f(p_try)
        error = dist_line_point(a,b, f_p_try)
        return error
    
    def calc_cut_point(a1,b1,a2,b2): #Se calculo el punto de corte respecto a dos rectas de la forma y = ax+b
            # punto de corte entre
            # r1: y = a1 * x + b1
            # r2: y = a2 * x + b2
            if b1 == "NR":
                x = a1
                y = b2
                return Point(x,y)
            if b2 == "NR":
                x = a2
            else:
                x = (b2-b1)/(a1-a2)
            y = a1*x+b1
            return Point(x,y)
    def diferencia(puntoR,vector,puntof): #Cálculo para discernir a que lado de una recta está un punto
        a,b = calc_AB(vector,puntoR)
        return puntof.y - a*puntof.x - b
    
    def calc_dist1_dist2(p_start, p_end): #Cálculo del signo respecto a la distancia de un punto a una recta
            f_p_end   = f(p_end)
            f_p_start = f(p_start)
            a, b      = calc_AB(Vector(d["p_left"], d["p_right"]),d["p_left"])
            dist1     = dist_line_point_sign(a,b, f_p_end)
            dist2     = dist_line_point_sign(a,b, f_p_start)
            return dist1, dist2

    def evalua(number):
        return number - d["bisection_error"] < 0
    
    O_start, O_end = d["alpha_max"], -d["alpha_max"] #Ángulos de la circunferencia a analizar
    pk    = d["M"][-1] #pk es el punto del que haremos un círculo
    pk_m1 = d["M"][-2] #pk_m1 sirve para calcular el vector de pk,pk_m1 y ángulo respecto al vector(1,0)
    v     = Vector(pk_m1,pk) #Vector entre pk_m1 y pk
    vn    = v.normalize()
    sigma = anguloX(v) #Ángulo del vector pk_m1 y pk respecto al vector (1,0)
    p_start, p_end, beta, gamma, V_start, V_end, W = find_all(sigma, O_start, O_end) #Búsqueda de diferentes parámetros
    if p_start == "None":
        return "None","None"
    
    dist1, dist2 = calc_dist1_dist2(p_start, p_end) #Condición para calcular si las imágenes están en diferentes lugares
    while dist1 * dist2 > 0: #Si la imagen de p_start y p_end están en la misma zona se aumenta el ángulo de búsqueda
        O_start    = O_start + (pi - O_start) * 0.001 #Aumento de o_start
        O_end      = O_end   - (pi + O_end  ) * 0.001 #Aumento de o_end
        p_start, p_end, beta, gamma, V_start, V_end, W = find_all(sigma, O_start, O_end) #Nueva búsqueda de parámetros
        if p_start == "None":
            return "None","None"
        dist1, dist2 = calc_dist1_dist2(p_start, p_end) #Nuevo calculo de condición
        
    def acota(a1,a2):
        while 1: #Hasta que no se encuentre el p_try
            O_try = (a1+a2)/2. #Ángulo medio
            p_try = find_p_try(O_try) #Búsqueda del punto medio entre p_start y p_end
            V = Vector(f(p_try), d["p_right"]) #Vector entre la iamgen de p_try y p_right
            if V_end.dotProduct(W) * V.dotProduct(W) > 0: #Condición para variar ángulo
                a2   = O_try #el ángulo a2 pasa a ser o_try
            else:
                a1 = O_try #el ángulo a1 pasa a ser o_try
            condition = evalua(calc_error(p_try)) #evalúa si el punto cumple las condiciones
            if condition: #Si la cumple se devuelve
                return p_try
        
    p_try = acota(beta,gamma) #Búsqueda del p_try
    a1,b1 = calc_AB(Vector(d["p_left"], d["p_right"]),d["p_left"]) #Calculamos a,b de y = ax+b del vector entre p_left y p_rigth con el punto p_left
    a2,b2 = calc_AB(W,f(p_try)) #Calculamos a,b de y =ab+x del vector W (el normaliado) y punto que es la imagen de p_Try
    corte = calc_cut_point(a1,b1,a2,b2) #Se calcula el punto de corte
    tau = calc_tau(corte) #Se calcula el tau con el punto de corte
    return p_try, tau  #Se devuelve el p_try y tau
    

def f(punto): #Llama a funciones para calcular la imagen de un punto con una función especificada
    return funciones(punto,d["mode"])

def funciones(punto,mode): #Simplemente calcula las imágenes dada una función
    if mode == "Ikeda":
        A, b, e, phi, q = 1, 0.9, 1, 0.4, 6
        m = phi - q/(1+punto.x**2 + punto.y**2)
        x = A + b * punto.x * cos(m) - e*punto.y * sin(m)
        y = b * punto.y * cos(m) + e * x * sin(m)
        return Point(x,y)
    if mode == "Mira":
        a,b = -0.8,0.1
        x = punto.y
        y = a*punto.x+b*punto.x**2+punto.y**2
        return Point(x,y)
    if mode == "Henon":
        x = punto.x/2
        y = 2*punto.y-7*punto.x**2
        return Point(x,y)
    if mode == "Input":
        x = 0
        y = 0
        return Point(x,y)
    
def movimiento(modulo,angulo): #Matriz de rotación
    punto = Point(modulo,0)
    x = punto.x*cos(angulo) - punto.y*sin(angulo)
    y = punto.x*sin(angulo) + punto.y*cos(angulo)
    return Point(x,y)

def anguloX(vector): #Ángulo entre vector(1,0) y vector (pk_m1,pk)
    v1 = Vector(1,0)
    v2 = vector
    escalar = v1.dotProduct(v2)
    return acos(escalar/(v1.module()*v2.module()))

def ejecucion(d,mode):
    option = input("Do you want to change the delta_k value? Default Value is 0.001 (Y/N)\n")
    while not (option == 'Y'    or option == 'N'
               or option == 'y' or option == 'n'):
        option = input("Error, enter Y for change values and N for use the default values\n")
    if option in "yY":
        while True:
            try:
                value = input("Enter new float value for {} parameter:\n".format("delta_k"))
                d["delta_k"] = float(value)
            except ValueError:
                print("ERROR: not valid value {} parameter\n".format("delta_k"))
                continue
            break
        print("The value has been initilized")
        print("Parameter\t   Default Value")
        print("{}\t   {}".format("delta_k",d["delta_k"]))
    else:
        d["delta_k"] = 10**-3
        print("The value has been initilized")
        print("Parameter\t   Default Value")
        print("{}\t   {}".format("delta_k",d["delta_k"]))
    
    stableMode = input("What manifold do you want to compute (if possible)? S: Stable U:Unstable B:Both (S/U/B)\n")
    while not (stableMode == 'S'    or stableMode == 's'
               or stableMode == 'U' or stableMode == 'u'
               or stableMode == 'B' or stableMode == 'b'):
        stableMode = input("ERROR, enter S for Stable, U for Unstable or B for Both\n")
    array = []
    if mode == "Ikeda":
        array = ikedaCalc(stableMode)
    if mode == "Henon":
        array = henonCalc(stableMode)
    if mode == "Mira":
        array = miraCalc(stableMode)
    if mode == "Input":
        array = inputCalc(stableMode)
    printManifold(array,mode)    
        
    
def henonCalc(mode):
    if mode in "Bb":
        M = []
        M = M+henonCalc("S")+henonCalc("U")
        print(M)
        return M
    if mode in "Ss":
        deltaCopy = d["delta_k"]
        p0 = Point(0,0)
        p1d = p0 + movimiento(d["delta_k"],0)
        p1i = p0 + movimiento(d["delta_k"],pi)
        d["delta_k"] = d["delta_k"]*1/2
        A = 100
        M1 = grow_manifold(d,p0,p1d,A)
        d["delta_k"] = deltaCopy
        d["delta_k"] = d["delta_k"]*1/2
        M2 = grow_manifold(d,p0,p1i,A)
        d["delta_k"] = deltaCopy
        M2.reverse()
        MID = M2+M1
        return [MID]
    if mode in "Uu":
        deltaCopy = d["delta_k"]
        p0 = Point(0,0)
        p1d = p0 + movimiento(d["delta_k"],0)
        p1i = p0 + movimiento(d["delta_k"],pi)
        d["delta_k"] = d["delta_k"]*1/2
        A = 100
        M1 = grow_manifold(d,p0,p1d,A)
        d["delta_k"] = deltaCopy
        d["delta_k"] = d["delta_k"]*1/2
        M2 = grow_manifold(d,p0,p1i,A)
        d["delta_k"] = deltaCopy
        M2.reverse()
        MID = M2+M1
        return [MID]
    
def ikedaCalc(mode):
    if mode in "Bb":
        M = []
        M = M+ikedaCalc("S")+ikedaCalc("U")
        return M
    if mode in "Ss":
        deltaCopy = d["delta_k"]
        p0 = Point(1.08332,-2.40796)
        d["delta_k"] = 10**(-3)
        p1 = p0 + movimiento(d["delta_k"],0.7)
        d["delta_k"] = d["delta_k"]*(1.1)*(0.5)
        A = 30
        M1 = grow_manifold(d,p0,p1,A)
        d["delta_k"] = deltaCopy
        return [M1]
    if mode in "Uu":
        deltaCopy = d["delta_k"]
        p0 = Point(1.08332,-2.40796)
        p1 = p0 + movimiento(d["delta_k"],3.9)
        d["delta_k"] = d["delta_k"]*(1.1)*(0.5)
        A = 30
        M1 = grow_manifold(d,p0,p1,A)
        d["delta_k"] = deltaCopy
        return [M1]
    
def miraCalc(mode):
    if mode in "Bb":
        M = []
        M = M+miraCalc("S")+miraCalc("U")
        return M
    if mode in "Ss":
        deltaCopy = d["delta_k"]
        p0 = Point(1.8/1.1,1.8/1.1)
        d["delta_k"] = 10**(-3)
        p1 = p0 + movimiento(d["delta_k"],3.241)
        d["delta_k"] = d["delta_k"]*(5.6)*(0.5)
        A = 5.9
        M1 = grow_manifold(d,p0,p1,A)
        d["delta_k"] = deltaCopy
        return [M1]
    if mode in "Uu":
        deltaCopy = d["delta_k"]
        p0 = Point(1.8/1.1,1.8/1.1)
        p1 = p0 + movimiento(d["delta_k"],0.1)
        d["delta_k"] = d["delta_k"]*(5.6)*(0.5)
        A = 4.735
        M1 = grow_manifold(d,p0,p1,A)
        d["delta_k"] = deltaCopy
        return [M1]
    
def inputCalc(mode):
    if mode in "Bb":
        M = []
        M = M+inputCalc("S")+inputCalc("U")
        return M
    if mode in "Ss":
        return ["None"]
    if mode in "Uu":
        return ["None"]
    
    

        
    
    




