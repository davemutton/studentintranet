from django.core.management.base import BaseCommand
from mediamanager.models import UrlResource, DefaultResource, AssoeLevel, AgeBracket, AssoePathway, AssoeSubjects
import random, csv
from taggit.models import Tag

class Command(BaseCommand):
	help ='populate the URLfield Model with data'

	def handle(self,*args, **options):
		i = 1
		while 1 > 0:
			levels = AssoeLevel.objects.all()
			level = random.choice(levels)
			subjects = AssoeSubjects.objects.all()
			subject = random.choice(subjects)
			pathways = AssoePathway.objects.all()
			pathway = random.choice(pathways)
			agebrackets = AgeBracket.objects.all()
			agebracket = random.choice(agebrackets)
			description = "This is a test object inserted for testing a test"
			title = "test" + str(i)
			tags = Tag.objects.all()
			tag =random.choice(tags)
			url = "www.google.com"
			p = UrlResource(title=title,description=description,url=url)
			p.save()
			p.level.add(level)
			p.pathway.add(pathway)
			p.agebracket.add(agebracket)
			p.tags.add(tag)
			p.subject.add(subject)
			p.save()
			i=i+1
			print i





'''



		levels = ['Foundation','Intermediate','Advanced','Transition']
		order = 0
		for level in levels:
			order = order + 1
			p = AssoeLevel(level=level,order=order)
			p.save()
		pathways = ['A','B','C']
		order = 0
		for pathway in pathways:
			order = order + 1
			p = AssoePathway(pathway=pathway,order=order)
			p.save()	

		ages = ['Junior','Senior']
		order = 0
		for age in ages:
			order = order + 1
			p = AgeBracket(agebracket=age,order=order)
			p.save()	

		subjects = ['Maths','Science','EALD','PLP','PLW','Digital Technologies','Visual Art','Drama']
		order = 0
		for subject in subjects:
			order = order + 1
			p = AssoeSubjects(subject=subject,order=order)
			p.save()	
			'''