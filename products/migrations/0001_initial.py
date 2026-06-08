from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='Product',
                    fields=[
                        ('id', models.BigAutoField(auto_created=True,
                         primary_key=True, serialize=False, verbose_name='ID')),
                        ('name', models.CharField(max_length=255)),
                        ('description', models.TextField(blank=True)),
                        ('price', models.DecimalField(
                            max_digits=10, decimal_places=2)),
                        ('created_at', models.DateTimeField(auto_now_add=True)),
                    ],
                    options={
                        'db_table': 'apis_product',
                    },
                ),
            ],
            database_operations=[],
        ),
    ]
