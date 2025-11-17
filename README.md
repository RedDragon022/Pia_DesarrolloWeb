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
- Plantillas: `templates/cafeteria/` (`inicio.html`, `menu.html`, `eventos.html`, `acerca.html`, `comentario.html`)
- Estilos: `static/css/style.css`
- Modelos: `cafeteria/models.py`
- Vistas: `cafeteria/views.py`
- Rutas: `cafeteria/urls.py`
 - Imágenes estáticas: `static/images/` (ej: `latte.webp`, `cafeamericano.webp`)

## Para cambiar el contenido
- Texto/HTML: edita la plantilla correspondiente.
- Navegación: actualizar el bloque `<nav>` en cada plantilla (se repite en 5 archivos para simplicidad).
- Inicio: muestra 3 productos destacados y un botón para ir al Menú.
- Menú: listado completo de productos con imágenes.
- Acerca: información institucional y una imagen decorativa.
- Eventos: editar datos en admin o directamente en modelo `Event`.
- Comentarios: formulario en `comentario.html` y creación en vista `comment`.
- Mensaje de éxito comentario: lógica en `views.py` función `comment` y lectura del parámetro `?ok=1` en `home`.
- Imágenes de productos: en el admin (modelo Product) llenar el campo "Archivo de Imagen" con la ruta relativa incluyendo la carpeta, por ejemplo: `images/latte.webp`. En las plantillas se usa `{% static p.image %}`.

## Añadir un nuevo campo a un modelo
1. Agrega el campo en `models.py`.
2. Ejecuta migraciones (ver arriba).
3. Si quieres mostrarlo en una plantilla, agrega `{{ objeto.campo }}` donde necesites.
 4. Para imágenes estáticas: el campo `image` guarda `images/<archivo>` (ej: `images/latte.webp`). En las plantillas se referencia con `{% static p.image %}`.

## CSS
Modificar `static/css/style.css`. Cambios reflejan al recargar la página.


