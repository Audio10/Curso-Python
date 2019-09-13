# Curso Practico de Python

## Funiciones basicas.

### Archivo Main

Todo punto de entrada o archivo principal es declarado con la sentencia.

```python
if __name__ == '__main__':
	pass
```

### Revisar el tipo de dato.

```
type($variable)
```

### Parsear Datos.

```python
int($variable)
str($variable)
bool($variable)
float($variable)
```

### Declaracion de una función.

```
suma_de_dos_numeros(x, y):
	return x + y
```

## Scope

Dentro de python el scope funciona de tal forma que una variable global no es visible para las demas funciones, amenos que esta sea invocada explicitamente.

Aunque si solo invocas la variable pero no la modificas no es necesario agregar el global.

```python
clients='pablo,ricardo,'


def create_client(client_name):
  #Llamando a la variable global clients.
    global clients
    clients+= client_name


if __name__ == '__main__':
    clients += 'david'
    print(clients)
```

