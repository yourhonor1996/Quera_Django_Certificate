import json

from django.conf import settings
from django.db import migrations, models
from django.db.migrations.operations.fields import AddField, AlterField
from django.db.models import F, Value, CharField
from django.db.models.functions import Concat, Replace

from people.models import Person

def insert_bad_data(apps, _):
    Person = apps.get_model('people', 'Person')
    with open(settings.BASE_DIR / 'people/fixtures/people.json', 'r') as f:
        people = json.load(f)
    for person in people:
        Person.objects.create(
            fullname=person['fields']['fullname'],
            information=person['fields']['information']
        )

def ammend_the_data(apps, _):
    Person = apps.get_model('people', 'Person')
    people = Person.objects.all()
    
    for person in people:
        fullnamesplit = str(person.fullname).split(';')
        first_name = fullnamesplit[0].split(':')[1]
        last_name = fullnamesplit[1].split(':')[1]

        informationsplit = str(person.information).split(';')
        info2 = {}
        for info in informationsplit:
            info3 = info.split(':')
            info2.update({info3[0] : info3[1]})
        
        # person.update(first_name= first_name, last_name= last_name, id_code= info2.get('id_code'), born_in= info2.get('born_in'), birth_year= info2.get('birth_year'))
        person.first_name = first_name
        person.last_name = last_name
        person.id_code = info2.get('id_code')
        person.born_in = info2.get('born_in')
        person.birth_year = info2.get('birth_year')



    # fullname_split = (F('fullname')).split(';')
    # first_name, last_name = 
    
    # Person.objects.update(first_name= )

    

    # Cake.objects.annotate(new_sauce_name=Concat(
    #     F('sauce'), Value(' Sauce'), output_field=CharField())).update(sauce=F('new_sauce_name'))
    


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=250, null=True)),
                ('information', models.CharField(max_length=350, null=True)),
            ],
        ),
        migrations.RunPython(
            code=insert_bad_data,
            reverse_code=migrations.RunPython.noop
        ),

        migrations.AddField(
            model_name= 'Person', 
            name= 'first_name',
            field= models.CharField(max_length= 30, null= True)),
        migrations.AddField(
            model_name= 'Person', 
            name= 'last_name',
            field= models.CharField(max_length= 50, null= True)),
        migrations.AddField(
            model_name= 'Person', 
            name= 'id_code',
            field= models.CharField(max_length= 10, null= True)),
        migrations.AddField(
            model_name= 'Person', 
            name= 'born_in',
            field= models.CharField(max_length= 30, null= True)),
        migrations.AddField(
            model_name= 'Person', 
            name= 'first_name',
            field= models.PositiveSmallIntegerField(null= True)),
        
        
        migrations.RunPython(code= ammend_the_data),
        
        # migrations.RemoveField(
        #     model_name= 'Person',
        #     name= 'fullname'),
        # migrations.RemoveField(
        #     model_name= 'Person',
        #     name= 'information'),
        
        
    ]
