from django.core.management.base import BaseCommand
from mediamanager.models import UrlResource, DefaultResource, AssoeLevel, AgeBracket, AssoePathway, AssoeSubjects
import random, csv

class Command(BaseCommand):
	help ='populate the URLfield Model with data'

	def handle(self,*args, **options):
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

		ages = ['A','B','C']
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