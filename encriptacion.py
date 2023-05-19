import math

def f(x):
    return 3.5 * x**3 + x * math.exp(x)

def gN(x):
    return x - (f(x) / (10.5 * x**2 + x * math.exp(x) + x*math.exp(x)))

def encrypt_message(message):
    encrypted_message = []
    
    for char in message:
        ascii_value = ord(char)
        equation = lambda x: 3.5 * x**3 + x * math.exp(x) - ascii_value
        root = newton_raphson(equation, 2)
        encrypted_message.append(str(root))
    
    return '|'.join(encrypted_message)

def decrypt_message(encrypted_message):
    decrypted_message = ""
    roots = encrypted_message.split('|')

    for root in roots:
        root = float(root)
        ascii_value = round(f(root))
        decrypted_message += chr(ascii_value)

    return decrypted_message

def newton_raphson(f, x0, epsilon=1e-8, max_iterations=100):
    x = x0
    
    for _ in range(max_iterations):
        fx = f(x)
        f_prime_x = (f(x + epsilon) - fx) / epsilon
        x = x - fx / f_prime_x
        
        if abs(fx) < epsilon:
            return x
    
    return x

def main():
     # Solicitar al usuario que ingrese el mensaje
    message = input("Ingrese el mensaje a encriptar: ")

    # Encriptar el mensaje
    encrypted_message = encrypt_message(message)
    print('Mensaje encriptado:', encrypted_message)

    # Desencriptación
    decrypted_message = decrypt_message(encrypted_message)
    print('Mensaje desencriptado:', decrypted_message)


if __name__ == "__main__":
    main()