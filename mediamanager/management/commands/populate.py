from django.core.management.base import BaseCommand
from mediamanager.models import UrlResource, DefaultResource, AssoeLevel, AgeBracket, AssoePathway, AssoeSubjects
import random, csv

class Command(BaseCommand):
	help ='populate the URLfield Model with data'

	def handle(self,*args, **options):
		with open ('data.csv','rU') as csvfile:
			reader = csv.reader(csvfile)
			data=[]
			for row in reader:
				data.append(row)
		n=0
		all_tags = ['cheese','apple','europe','local politics','local government','torrens council','relief','end of term']
		for x in range(25):
			for row in data:
				for url in row:
					level = random.choice(AssoeLevel.objects.all())
					age = random.choice(AgeBracket.objects.all())
					pathway = random.choice(AssoePathway.objects.all())
					subject = random.choice(AssoeSubjects.objects.all())
					tag = random.choice(all_tags)
					print tag
					n=n+1
					print n
					title = "test run " +str(n) + str(subject)
					p = UrlResource(title=title,url=url)
					p.save()
					p.level.add(level.pk)
					p.agebracket.add(age.pk)
					p.pathway.add(pathway.pk)
					p.subject.add(subject.pk)
					p.tags.add(tag)
					level = random.choice(AssoeLevel.objects.all())
					age = random.choice(AgeBracket.objects.all())
					pathway = random.choice(AssoePathway.objects.all())
					subject = random.choice(AssoeSubjects.objects.all())
					tag = random.choice(all_tags)
					p.level.add(level.pk)
					p.agebracket.add(age.pk)
					p.pathway.add(pathway.pk)
					p.subject.add(subject.pk)
					p.tags.add(tag)
					p.save()
