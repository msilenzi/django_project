from django.db import models


class Project(models.Model):
    """
    Creamos una clase `Project` que hereda del modelo provisto por Django.
    Cuando hagamos las migraciones, esta clase se convertira en una tabla.
    Dentro de esta clase podemos colocar atributos que nos van a permitir
    especificar las columnas (los datos) que vamos a guardar en una tabla.
    """
    # `name` es el nombre del campo y le asignamos un tipo de dato SQL.
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.name)


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title + ' - ' + self.project.name
