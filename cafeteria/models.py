from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    description = models.TextField(blank=True, verbose_name="Descripción")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio")
    image = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Archivo de Imagen",
        help_text="Nombre del archivo en static/images (ej: latte.webp)"
    )

    def __str__(self):
        return self.name


## Car model removed as it's not required for runtime


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título del Evento")
    date = models.DateTimeField(verbose_name="Fecha y Hora")
    description = models.TextField(blank=True, verbose_name="Descripción")

    def __str__(self):
        return f"{self.title} - {self.date.strftime('%d/%m/%Y')}"


class Branch(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre de la Sucursal")
    address = models.CharField(max_length=300, verbose_name="Dirección")
    phone = models.CharField(max_length=50, blank=True, verbose_name="Teléfono")

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.CharField(max_length=150, verbose_name="Autor")
    email = models.EmailField(blank=True, verbose_name="Correo Electrónico")
    content = models.TextField(verbose_name="Comentario")

    def __str__(self):
        return f"{self.author}: {self.content[:40]}..."
