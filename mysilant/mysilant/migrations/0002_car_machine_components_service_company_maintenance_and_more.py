# Generated by Django 4.2.5 on 2023-10-27 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_сategory'),
        ('mysilant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factory_number', models.TextField(db_index=True, max_length=17, unique=True, verbose_name='Заводской номер')),
                ('engine_number', models.TextField(max_length=17, verbose_name='Номер двигателя')),
                ('transmission_number', models.TextField(max_length=50, verbose_name='Номер трансмиссии')),
                ('drive_axle_number', models.TextField(max_length=50, verbose_name='Номер ведущего моста')),
                ('steerable_axle_number', models.TextField(max_length=50, verbose_name='Номер управляемого моста')),
                ('supply_contract', models.TextField(blank=True, max_length=50, verbose_name='Договор поставки №, дата.')),
                ('date_of_shipment_from_the_factory', models.DateField(db_index=True, verbose_name='Дата отгрузки с завода')),
                ('consignee', models.TextField(blank=True, max_length=50, verbose_name='Грузополучатель')),
                ('delivery_address', models.TextField(blank=True, max_length=300, verbose_name='Адрес поставки (эксплуатации)')),
                ('equipment', models.TextField(blank=True, verbose_name='Комплектация (доп. опции)')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.counterparty', verbose_name='Клиент')),
                ('drive_axle_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysilant.drive_axle_model', verbose_name='Модель ведущего моста')),
                ('engine_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysilant.engine_model', verbose_name='Модель двигателя')),
            ],
            options={
                'verbose_name': 'Машины',
                'verbose_name_plural': 'Машины',
                'ordering': ['date_of_shipment_from_the_factory'],
            },
        ),
        migrations.CreateModel(
            name='Machine_components',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Способ восстановления',
                'verbose_name_plural': 'Способ восстановления',
            },
        ),
        migrations.CreateModel(
            name='Service_company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.counterparty')),
            ],
            options={
                'verbose_name': 'Сервисные компании',
                'verbose_name_plural': 'Сервисные компании',
            },
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_date', models.DateField(verbose_name='Дата проведения ТО')),
                ('operating_time', models.IntegerField(verbose_name='Наработка м/часов')),
                ('order', models.TextField(max_length=50, verbose_name='Номер заказа-наряда')),
                ('order_date', models.DateField(verbose_name='Дата заказа-наряда')),
                ('company_executor', models.TextField(max_length=50, verbose_name='Компания исполнитель')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysilant.car', verbose_name='Машина')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysilant.service_company', verbose_name='Сервисная организация')),
                ('type_maintenance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysilant.type_maintenance', verbose_name='Вид ТО')),
            ],
            options={
                'verbose_name': 'ТО',
                'verbose_name_plural': 'ТО',
                'ordering': ['maintenance_date'],
            },
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_refusal', models.DateField(verbose_name='Дата отказа')),
                ('operating_time', models.IntegerField(verbose_name='Наработка м/час')),
                ('failure_node', models.TextField(verbose_name='Описание отказа отказа')),
                ('parts_used', models.TextField(blank=True, verbose_name='Используемые запасные части')),
                ('date_of_restoration', models.DateField(verbose_name='Дата восстановления')),
                ('equipment_downtime', models.TextField(verbose_name='Время простоя техники')),
                ('Machine_components', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysilant.machine_components', verbose_name='Узел отказа')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysilant.car', verbose_name='Машина')),
                ('recovery_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysilant.recovery_method', verbose_name='Способ восстановления')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysilant.service_company', verbose_name='Сервисная организация')),
            ],
            options={
                'verbose_name': 'Рекламации',
                'verbose_name_plural': 'Рекламации',
                'ordering': ['date_of_refusal'],
            },
        ),
        migrations.AddField(
            model_name='car',
            name='service_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysilant.service_company', verbose_name='Сервисная организация'),
        ),
        migrations.AddField(
            model_name='car',
            name='steerable_axle_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysilant.steerable_axle_model', verbose_name='Модель управляемого моста'),
        ),
        migrations.AddField(
            model_name='car',
            name='technique_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysilant.technique_model', verbose_name='Модель техники'),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysilant.transmission_model', verbose_name='Модель трансмиссии'),
        ),
    ]