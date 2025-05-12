# Proyecto PPS01 - Verificador de Palíndromos en Python

## Descripción

Este proyecto consiste en un programa que verifica si una frase o cadena de texto es un **palíndromo**, es decir, si se lee igual de izquierda a derecha que de derecha a izquierda, ignorando espacios, signos de puntuación y mayúsculas/minúsculas.

Además, incluye una batería de pruebas automatizadas usando la librería `unittest` para validar distintas entradas posibles (frases vacías, símbolos, números, etc.).

## Tecnologías utilizadas

- **Lenguaje**: Python 3
- **Framework de testing**: `unittest`

## Estructura

```
proyectopps01/
├── charfun.py           # Contiene la función principal esPalindromo()
├── Principal_test.py    # Contiene los tests unitarios
└── README.md            # Este archivo de documentación
```

## Instalación

1. Asegúrate de tener Python instalado. Puedes verificarlo con:

    python3 --version

2. Clona este repositorio o copia los archivos manualmente a una carpeta local.

3. (Opcional) crea un entorno virtual:

    python3 -m venv venv
    source venv/bin/activate

## Uso

Puedes ejecutar el script principal para probar manualmente si una frase es un palíndromo:

    python3 charfun.py

También puedes ejecutar los tests automáticos:

    python3 -m unittest Principal_test.py

##  Autor

- Nombre: Jesús Martin
- Email: Jesus@martinsevilla.es

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT. Puedes ver el archivo `LICENSE` para más detalles.
