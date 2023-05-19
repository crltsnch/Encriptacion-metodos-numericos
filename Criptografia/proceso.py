import math
import helper

class Proceso():

    def f(self, x):
        return 3.5 * x**3 + x * math.exp(x)

    def gN(self, x):
        return x - (self.f(x) / (10.5 * x**2 + x * math.exp(x) + x*math.exp(x)))

    def encriptar(self):
        print('Introduce el mensaje a desencriptar:')
        mensaje = input('>> ')  
        mensaje_encriptado = []
        
        for c in mensaje:
            valor_ascii = ord(c)
            eq = lambda x: 3.5 * x**3 + x * math.exp(x) - valor_ascii
            raiz = self.newton_raphson(eq, 2)
            mensaje_encriptado.append(str(raiz))
        
        return '|'.join(mensaje_encriptado)

    def desencriptar(self, mensaje = ''):
        if mensaje == '':
            print('Introduce el mensaje a desencriptar:')
            mensaje = input('>> ')
    
        mensaje_desencriptado = ""
        raices = mensaje.split('|')

        for raiz in raices:
            raiz = float(raiz)
            valor_ascii = round(self.f(raiz))
            mensaje_desencriptado += chr(valor_ascii)

        return mensaje_desencriptado

    def newton_raphson(self, f, x0, epsilon=1e-8, max_iterations=100):
        x = x0
        
        for _ in range(max_iterations):
            fx = f(x)
            f_prime_x = (f(x + epsilon) - fx) / epsilon
            x = x - fx / f_prime_x
            
            if abs(fx) < epsilon:
                return x
    
        return x