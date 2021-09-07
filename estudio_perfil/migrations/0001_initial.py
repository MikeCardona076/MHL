# Generated by Django 3.2.6 on 2021-09-07 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudio_perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Clave', models.IntegerField(unique=True)),
                ('Nombre', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('Precio1', models.CharField(blank=True, max_length=10, null=True)),
                ('Precio2', models.CharField(blank=True, max_length=10, null=True)),
                ('Precio3', models.CharField(blank=True, max_length=10, null=True)),
                ('Precio4', models.CharField(blank=True, max_length=10, null=True)),
                ('Precio5', models.CharField(blank=True, max_length=10, null=True)),
                ('Prupo', models.CharField(blank=True, max_length=50, null=True)),
                ('Tipo', models.CharField(blank=True, max_length=50, null=True)),
                ('Sinonimo1', models.CharField(blank=True, max_length=50, null=True)),
                ('Sinonimo2', models.CharField(blank=True, max_length=50, null=True)),
                ('Tubo', models.CharField(blank=True, max_length=50, null=True)),
                ('Unidades', models.CharField(blank=True, max_length=50, null=True)),
                ('Metodo', models.CharField(blank=True, max_length=50, null=True)),
                ('TipoMuestra', models.CharField(blank=True, max_length=50, null=True)),
                ('Catalogo', models.CharField(blank=True, max_length=50, null=True)),
                ('Tiempo', models.CharField(blank=True, max_length=50, null=True)),
                ('Costo', models.CharField(blank=True, max_length=10, null=True)),
                ('Especiales', models.CharField(blank=True, max_length=50, null=True)),
                ('SexoPrueba', models.CharField(blank=True, max_length=50, null=True)),
                ('Clasifica', models.CharField(blank=True, max_length=50, null=True)),
                ('EstLaboratorio', models.CharField(blank=True, max_length=50, null=True)),
                ('EstGabinete', models.CharField(blank=True, max_length=50, null=True)),
                ('Factor', models.CharField(blank=True, max_length=10, null=True)),
                ('UnidadesInt', models.CharField(blank=True, max_length=50, null=True)),
                ('TdContenedor', models.CharField(blank=True, max_length=50, null=True)),
                ('Equipo', models.CharField(blank=True, max_length=50, null=True)),
                ('Maquilador', models.CharField(blank=True, max_length=50, null=True)),
                ('Indicaciones', models.CharField(blank=True, max_length=50, null=True)),
                ('Area', models.CharField(blank=True, max_length=50, null=True)),
                ('usoClinico', models.CharField(blank=True, max_length=50, null=True)),
                ('nivelBase', models.CharField(blank=True, max_length=50, null=True)),
                ('tProceso', models.CharField(blank=True, max_length=50, null=True)),
                ('CodigoSAT', models.CharField(blank=True, max_length=50, null=True)),
                ('UnidadSAT', models.CharField(blank=True, max_length=50, null=True)),
                ('ImpConsent', models.CharField(blank=True, max_length=50, null=True)),
                ('GpoRecep', models.CharField(blank=True, max_length=50, null=True)),
                ('ClaveExt', models.CharField(blank=True, max_length=50, null=True)),
                ('Moneda', models.CharField(blank=True, max_length=50, null=True)),
                ('impSep', models.CharField(blank=True, max_length=50, null=True)),
                ('impNombreP', models.CharField(blank=True, max_length=50, null=True)),
                ('IdTipoMuestra', models.CharField(blank=True, max_length=50, null=True)),
                ('IdGrupo', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'estudio_perfil',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Condiciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('Grupo', models.CharField(blank=True, max_length=50, null=True)),
                ('Condicion', models.CharField(blank=True, max_length=50, null=True)),
                ('Descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('Clave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudio_perfil.estudio_perfil')),
            ],
            options={
                'db_table': 'Condiciones',
                'managed': True,
            },
        ),
    ]
