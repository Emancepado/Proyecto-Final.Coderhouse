# Generated by Django 4.2.2 on 2023-07-14 02:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_user', '0006_remove_producto_usuario_alter_producto_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
