# Generated by Django 2.2.14 on 2021-10-04 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carburant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carburant', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Couleur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('couleur', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Couleur_intertieur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('couleur_intertieur', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Etat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etat', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lieu', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere_interieur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matiere_interieur', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Modele',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modele', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transmission', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('annee', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)])),
                ('prix', models.CharField(max_length=300)),
                ('kilometrage', models.IntegerField()),
                ('photo_face', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('photo_longueur1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('photo_longueur2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('photo_arriere', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('photo_tableau', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('photo_option1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('photo_option2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('photo_option3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('photo_option4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('photo_option5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('photo_moteur', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('photo_carte_grise', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('photo_assurance', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('photo_defaut1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('photo_defaut2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('photo_defaut3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('photo_defaut4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('photo_defaut5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField()),
                ('date_ajout', models.DateField()),
                ('carburant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Carburant')),
                ('couleur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Couleur')),
                ('couleur_intertieur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Couleur_intertieur')),
                ('etat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Etat')),
                ('lieu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Lieu')),
                ('marque', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Marque')),
                ('matiere_interieur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Matiere_interieur')),
                ('modele', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Modele')),
                ('transmission', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Transmission')),
            ],
        ),
    ]
