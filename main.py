from clases.areas import area_rectangulo,area_triangulo

def main():
    while True:
        print("\n--- CÁLCULO DE ÁREAS ---")
        print("1. Área de un triángulo")
        print("2. Área de un rectángulo")
        print("3. Salir")

        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura del triángulo: "))
            area = area_triangulo(base, altura)
            print(f"El área del triángulo es: {area:.2f}")

        elif opcion == "2":
            base = float(input("Ingresa la base del rectángulo: "))
            altura = float(input("Ingresa la altura del rectángulo: "))
            area = area_rectangulo(base, altura)
            print(f"El área del rectángulo es: {area:.2f}")

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intenta nuevamente.")

if __name__ == "__main__":
    main()
