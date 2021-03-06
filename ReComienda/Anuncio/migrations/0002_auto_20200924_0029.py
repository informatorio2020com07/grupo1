# Generated by Django 3.1.1 on 2020-09-24 03:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Anuncio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalificacionPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(-5)])),
                ('anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calificacion', to='Anuncio.anuncio_trans')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle_calificacion', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('anuncio', 'usuario')},
            },
        ),
        migrations.AddField(
            model_name='anuncio_trans',
            name='puntuadores',
            field=models.ManyToManyField(blank=True, related_name='post_calificados', through='Anuncio.CalificacionPost', to=settings.AUTH_USER_MODEL),
        ),
    ]
