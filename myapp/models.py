from django.db import models

# Create your models here.

# Creamos una clase `Project` que hereda del modelo provisto por Django.
# Cuando hagamos las migraciones, esta clase se convertira en una tabla.
# Dentro de esta clase podemos colocar atributos que nos van a permitir
# especificar las columnas (los datos) que vamos a guardar en una tabla.
class Project(models.Model):
    # `name` es el nombre del campo y le asignamos un tipo de dato SQL.
    name = models.CharField(max_length=255)
