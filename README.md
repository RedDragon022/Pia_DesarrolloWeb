# Proyecto Cafetería (Versión Mínima)

Este proyecto es una versión simplificada de una aplicación Django para una cafetería universitaria.

## Ejecutar
1. Activar entorno virtual:
```bash
source .venv/Scripts/activate
```
2. Migraciones (solo si cambias modelos):
```bash
python manage.py makemigrations
python manage.py migrate
```
3. Iniciar servidor:
```bash
python manage.py runserver
```

## Estructura clave
- Plantillas: `templates/cafeteria/` (`inicio.html`, `menu.html`, `eventos.html`, `sucursales.html`, `acerca.html`, `comentario.html`)
- Estilos: `static/css/style.css`
- Modelos: `cafeteria/models.py`
- Vistas: `cafeteria/views.py`
- Rutas: `cafeteria/urls.py`

## Para cambiar el contenido
- Texto/HTML: edita la plantilla correspondiente.
- Navegación: actualizar el bloque `<nav>` en cada plantilla (están duplicadas a propósito para ser simples).
- Productos/Eventos/Sucursales: agregar/editar desde el admin (`python manage.py createsuperuser`) o vía shell.
- Mensaje de éxito comentario: lógica en `views.py` función `comment` y lectura del parámetro `?ok=1` en `home`.

## Añadir un nuevo campo a un modelo
1. Agrega el campo en `models.py`.
2. Ejecuta migraciones (ver arriba).
3. Si quieres mostrarlo en una plantilla, agrega `{{ objeto.campo }}` donde necesites.

## CSS
Modificar `static/css/style.css`. Cambios reflejan al recargar la página.

## Limpieza
Se eliminaron archivos no esenciales (PDFs, documentación extensa y comandos de gestión). Esta es la base mínima.

