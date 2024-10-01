# Generated by Django 4.2 on 2024-05-30 23:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FormasDePago',
            fields=[
                ('id_forma_de_pago', models.AutoField(db_column='ID_Forma_de_pago', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(db_column='Descripcion', max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Formas de pago',
                'db_table': 'formas_de_pago',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.AutoField(db_column='ID_Producto', primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(db_column='Nombre_producto', max_length=45)),
                ('precio', models.FloatField(db_column='Precio')),
                ('imagen', models.CharField(blank=True, db_column='Imagen', max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Productos',
                'db_table': 'productos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Talles',
            fields=[
                ('id_talle', models.AutoField(db_column='ID_talle', primary_key=True, serialize=False)),
                ('talle', models.CharField(db_column='Talle', max_length=45)),
            ],
            options={
                'verbose_name_plural': 'Talles',
                'db_table': 'talles',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tarjetas',
            fields=[
                ('id_tarjeta', models.AutoField(db_column='ID_Tarjeta', primary_key=True, serialize=False)),
                ('nombre_tarjeta', models.CharField(db_column='Nombre_tarjeta', max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Tarjetas',
                'db_table': 'tarjetas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductosTalles',
            fields=[
                ('id_producto_talle', models.AutoField(db_column='ID_producto_talle', primary_key=True, serialize=False)),
                ('stock', models.IntegerField(db_column='Stock', validators=[django.core.validators.MinValueValidator(0)])),
                ('productos', models.ForeignKey(db_column='ID_producto', on_delete=django.db.models.deletion.DO_NOTHING, to='web.productos')),
                ('talles', models.ForeignKey(db_column='ID_talle', on_delete=django.db.models.deletion.DO_NOTHING, to='web.talles')),
            ],
            options={
                'verbose_name_plural': 'Productos-Talles',
                'db_table': 'productos_talles',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id_pedido', models.AutoField(db_column='ID_pedido', primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('total', models.FloatField(db_column='Total')),
                ('estado', models.CharField(choices=[('ACEPTADO', 'Aceptado'), ('CANCELADO', 'Cancelado'), ('ENVIADO', 'Enviado')], db_column='Estado', max_length=9)),
                ('usuarios', models.ForeignKey(db_column='ID_usuario', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Pedidos',
                'db_table': 'pedidos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FormasDepagoPedidos',
            fields=[
                ('id_forma_depago_pedidos', models.AutoField(db_column='ID_Forma_depago_Pedidos', primary_key=True, serialize=False)),
                ('formasdepago', models.ForeignKey(db_column='ID_forma_de_pago', on_delete=django.db.models.deletion.DO_NOTHING, to='web.formasdepago')),
                ('pedidos', models.ForeignKey(db_column='ID_pedido', on_delete=django.db.models.deletion.DO_NOTHING, to='web.pedidos')),
                ('tarjeta', models.ForeignKey(blank=True, db_column='ID_tarjeta', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='web.tarjetas')),
            ],
            options={
                'verbose_name_plural': 'Formas de pago de pedidos',
                'db_table': 'formas_depago_pedidos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DetallesPedido',
            fields=[
                ('id_detalle', models.AutoField(db_column='ID_detalle', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(db_column='Cantidad')),
                ('subtotal', models.FloatField(db_column='Subtotal')),
                ('pedidos', models.ForeignKey(db_column='ID_pedido', on_delete=django.db.models.deletion.DO_NOTHING, to='web.pedidos')),
                ('productos', models.ForeignKey(db_column='ID_producto', on_delete=django.db.models.deletion.DO_NOTHING, to='web.productos')),
                ('talles', models.ForeignKey(db_column='ID_talle', on_delete=django.db.models.deletion.DO_NOTHING, to='web.talles')),
            ],
            options={
                'verbose_name_plural': 'Detalles de pedidos',
                'db_table': 'detalles_pedido',
                'managed': True,
            },
        ),
    ]
