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
- Inicio: muestra productos (menú resumido), sucursales y bloque acerca breve.
- Menú: listado completo de productos con imágenes.
- Acerca: información institucional y una imagen decorativa.
- Eventos: editar datos en admin o directamente en modelo `Event`.
- Comentarios: formulario en `comentario.html` y creación en vista `comment`.
- Mensaje de éxito comentario: lógica en `views.py` función `comment` y lectura del parámetro `?ok=1` en `home`.
- Imágenes de productos: en el admin (modelo Product) llenar el campo "Archivo de Imagen" SOLO con el nombre (ej: `latte.webp`). La plantilla construye la ruta.

## Añadir un nuevo campo a un modelo
1. Agrega el campo en `models.py`.
2. Ejecuta migraciones (ver arriba).
3. Si quieres mostrarlo en una plantilla, agrega `{{ objeto.campo }}` donde necesites.
 4. Para imágenes estáticas: en este proyecto el campo `image` guarda solo el nombre (ej: `latte.webp`). La plantilla construye la ruta con `{% static 'images/' %}{{ p.image }}`.

## CSS
Modificar `static/css/style.css`. Cambios reflejan al recargar la página.


