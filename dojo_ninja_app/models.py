from django.db import models


# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    desc = models.TextField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #list_of_book 

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Name: {self.name} | Descripción:{self.desc} | Ciudad:{self.city} | Estado:{self.state}>"


class Ninja(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    def __repr__(self):
        return f"<First_name: {self.first_name} | Last_name: {self.last_name} Dojo: {self.dojo}>"


    # Dojo.objects.create(name="pata_en_el_culo", city="Changay", state="chanchan")
    # Dojo.objects.create(name="pata_en_la_laja", city="Changay", state="chinchan")
    # Dojo.objects.create(name="pata_enel_ojo", city="Changay", state="chancian")
    #>>> dojo_del=Dojo.objects.get(name="pata_en_el_culo")
    #>>> dojo_del.name
    #'pata_en_el_culo'
    #>>> dojo_del=Dojo.objects.get(name="pata_en_la_laja")               
    #>>> dojo_del.name
    #'pata_en_la_laja'
    #>>> dojo_del=Dojo.objects.get(name="pata_enel_ojo")   
    #>>> dojo_del.name
    #'pata_enel_ojo'
    #>>> new_dojo=Dojo.objects.create(name="pata_fua", city="barrio rojo", state="chuchan")               
    #>>> new_dojo.save()
    #>>> new_dojo=Dojo.objects.create(name="charchazo", city="Gotika", state="chin chin")     
    #>>> new_dojo.save()
    #>>> new_dojo=Dojo.objects.create(name="EL_cornete", city="barrio_wan", state="chouuchan") 
    #>>> new_dojo.save()
    #new_ninja=Ninja.objects.create(first_name="jaki", last_name="chan", dojo=this_dojo)  
    #>>> new_ninja.save()
    #>>> new_ninja=Ninja.objects.create(first_name="bruce", last_name="lee", dojo=this_dojo)   
    #>>> new_ninja.save()
    
    #>> new_ninja=Ninja.objects.create(first_name="Tom", last_name="Po", dojo=this_dojo) 
    #>>> new_ninja.save()
    #this_dojo=Dojo.objects.get(name="EL_cornete") 
    #>>> this_dojo.name
    #'EL_cornete'
    #>>> new_ninja=Ninja.objects.create(first_name="chechu", last_name="chompa", dojo=this_dojo)
    #>>> new_ninja.save()   
    #>>> new_ninja=Ninja.objects.create(first_name="chaco", last_name="lucas", dojo=this_dojo)  
    #>>> new_ninja.save()
    #>>> new_ninja=Ninja.objects.create(first_name="luanhu", last_name="loa", dojo=this_dojo)    
    #>>> new_ninja.save()
    #>>> Dojo.objects.get(name="pata_fua")
    #<Name: pata_fua>
    #>>> Dojo.objects.filter(name="pata_fua")
    #<QuerySet [<Name: pata_fua>]>
    #>>> Ninja.objects.filter(dojo=this_dojo)
    #<QuerySet [<First_name: jaki | Last_name: chan Dojo: pata_fua>, <First_name: bruce | Last_name: lee Dojo: pata_fua>, <First_name: Tom | Last_name: Po Dojo: pata_fua>, <First_name: jaki | Last_name: chan Dojo: pata_fua>]>  
    #>>> this_dojo=Dojo.objects.last()              
    #>>> this_dojo.name
    #'EL_cornete'
    #Ninja.objects.filter(dojo=this_dojo)
    #last_ninja=Ninja.objects.last()
    #last_ninja.first_name
    #Ninja.objects.filter(first_name=last_ninja)
    #<QuerySet [<First_name: luanhu | Last_name: loa Dojo: EL_cornete>]>
    #python manage.py makemigrations
    #python manage.py migrate
    #new_dojo=Dojo.objects.create(name="chingon", city="Changay", state="chanchan")                        
    #>>> new_dojo.save()
    #Dojo.objects.all()