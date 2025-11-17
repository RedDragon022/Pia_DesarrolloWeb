from django.core.management.base import BaseCommand
from django.utils import timezone
from cafeteria.models import Product, Branch, Event, Car, Comment


class Command(BaseCommand):
    help = 'Crea datos de ejemplo para la cafetería'

    def handle(self, *args, **options):
        self.stdout.write('Iniciando creación de datos de ejemplo...')

        products = [
            {'name': 'Café Americano', 'description': 'Café negro tradicional.', 'price': 25.00},
            {'name': 'Latte', 'description': 'Café con leche espumosa.', 'price': 35.00},
            {'name': 'Cheesecake', 'description': 'Porción de cheesecake casero.', 'price': 45.00},
        ]
        for p in products:
            obj, created = Product.objects.get_or_create(name=p['name'], defaults={'description': p['description'], 'price': p['price']})
            if created:
                self.stdout.write(f"Creado producto: {obj.name}")

        branches = [
            {'name': 'Campus Central', 'address': 'Av. Universidad 100', 'phone': '55-1234-5678'},
            {'name': 'Sucursal Norte', 'address': 'Av. Norte 200', 'phone': '55-2222-3333'},
        ]
        for b in branches:
            obj, created = Branch.objects.get_or_create(name=b['name'], defaults={'address': b['address'], 'phone': b['phone']})
            if created:
                self.stdout.write(f"Creada sucursal: {obj.name}")

        now = timezone.now()
        events = [
            {'title': 'Música en vivo', 'date': now + timezone.timedelta(days=7), 'description': 'Noche de música local.'},
            {'title': 'Taller de latte art', 'date': now + timezone.timedelta(days=14), 'description': 'Aprende a decorar tu café.'},
        ]
        for e in events:
            obj, created = Event.objects.get_or_create(title=e['title'], date=e['date'], defaults={'description': e['description']})
            if created:
                self.stdout.write(f"Creado evento: {obj.title}")

        cars = [
            {'make': 'Toyota', 'model': 'Yaris', 'plate': 'ABC-1234'},
            {'make': 'Nissan', 'model': 'March', 'plate': 'XYZ-5678'},
        ]
        for c in cars:
            obj, created = Car.objects.get_or_create(plate=c['plate'], defaults={'make': c['make'], 'model': c['model']})
            if created:
                self.stdout.write(f"Creado auto: {obj}")

        comments = [
            {'author': 'Ana', 'email': 'ana@example.com', 'content': 'Me encanta el café de la sucursal central.', 'approved': True},
            {'author': 'Luis', 'email': 'luis@example.com', 'content': 'Muy buen servicio.', 'approved': False},
        ]
        for cm in comments:
            obj, created = Comment.objects.get_or_create(author=cm['author'], content=cm['content'], defaults={'email': cm['email'], 'approved': cm['approved']})
            if created:
                self.stdout.write(f"Creado comentario de: {obj.author}")

        self.stdout.write(self.style.SUCCESS('Datos de ejemplo creados correctamente.'))
