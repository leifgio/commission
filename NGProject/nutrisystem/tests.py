from django.test import TestCase
from nutrisystem.views import MainPage
from .models import Info 

class HomePageTest(TestCase):
	
	'''
	def test_root_url_resolves_to_MainPage_view(self):
		found = resolve('/')
		self.assertEqual(found.func,MainPage)
		
	def test_MainPage_returns_correct_view(self):
		request = HttpRequest()
		response = MainPage(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<!DOCTYPE html>'))
		self.assertIn('<title>NutriGeek System</title>', html)
		self.assertTrue(html.endswith(''))
		
		stringPage = render_to_string('mainpage.html') '''

	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')
	
	#def test_responding_post_request(self):
	#	resp = self.client.post('/', data={'NewName' : 'name' 'NewE_Add' : 'E_Add' 'NewEMessage' : 'EMessage''NewFName' :'fname' 'NewRB': 'gender2'},
	#		'email':'newEmail' 'age1':'NewAge' 'NewEAdd' : 'EAdd' 'NewEHeight':'EHeight' 'NewEWeight':'EWeight' 'NewAllergen6', 'NewAllergen10', 'NewAllergen13')
	#	self.assertIn('NewName','NewE_Add', 'NewEMessage', 'NewFName','NewRB', 'NewAge', 'NewEAdd', 'NewEHeight', 'NewEWeight', 'NewAllergen6', 'NewAllergen10', 'NewAllergen13' resp.content.decode())
	#	self.assertTemplateUsed(resp, 'mainpage.html')

	def test_save_POST_request(self):
		response = self.client.post('/',
		{ 	'fname':'Kathleen Mae',
			'genders' : 'Female',
			'age1' : '21',
			'EAdd': 'kathleenmae.labadlabad@gsfe.tupcavite.edu.ph',
			'EHeight' : '150',
			'EWeight' : '50',
			'Allergen1' : 'Tree Nuts'})
		self.assertEqual(Info.objects.count(),1)
		NGData = Info.objects.first()
		self.assertEqual(NGData.fullname, 'Kathleen Mae')
		self.assertEqual(NGData.sex, 'Female')
		self.assertEqual(NGData.age, '21')
		self.assertEqual(NGData.email, 'kathleenmae.labadlabad@gsfe.tupcavite.edu.ph')
		self.assertEqual(NGData.height, '150')
		self.assertEqual(NGData.weight, '50')
		self.assertEqual(NGData.foodallergens, 'Tree Nuts')

	def test_only_save_items_if_necessary (self):
		self.client.get('/')
		self.assertEqual(Info.objects.count(),0)

class ORMTEST(TestCase):
	def test_saving_retrieve(self):
		copy_of_Info =  Info()
		copy_of_Info.fullname = 'Kathleen Mae'
		copy_of_Info.sex = 'Female'
		copy_of_Info.age = '21'
		copy_of_Info.email = 'kathleenmae.labadlabad@gsfe.tupcavite.edu.ph'
		copy_of_Info.height = '150'
		copy_of_Info.weight = '50'
		copy_of_Info.foodallergens = 'Tree Nuts'
		copy_of_Info.save()

		copy_of_Info =  Info()
		copy_of_Info.fullname = 'Kathleen'
		copy_of_Info.sex = 'Female'
		copy_of_Info.age = '19'
		copy_of_Info.email = 'kathleenmae.labadlabad@gmail.com'
		copy_of_Info.height = '155'
		copy_of_Info.weight = '55'
		copy_of_Info.foodallergens = 'Milk'
		copy_of_Info.save()

		list_of_info = Info.objects.all()

		self.assertEqual (list_of_info.count(),2)

		info1 = list_of_info [0]
		info2 = list_of_info [1]

		self.assertEqual (info1.fullname, 'Kathleen Mae')
		self.assertEqual (info1.sex, 'Female')
		self.assertEqual (info1.age, '21')
		self.assertEqual (info1.email, 'kathleenmae.labadlabad@gsfe.tupcavite.edu.ph')
		self.assertEqual (info1.height, '150')
		self.assertEqual (info1.weight, '50')
		self.assertEqual (info1.foodallergens, 'Tree Nuts')

		self.assertEqual (info2.fullname, 'Kathleen')
		self.assertEqual (info2.sex, 'Female')
		self.assertEqual (info2.age, '19')
		self.assertEqual (info2.email, 'kathleenmae.labadlabad@gmail.com')
		self.assertEqual (info2.height, '155')
		self.assertEqual (info2.weight, '55')
		self.assertEqual (info2.foodallergens, 'Milk')

	def test_template_display_list(self):
		Info.objects.create(
			fullname='Gabriel',
			sex='Male',
			age ='2O',
			email =  'gabby@gsfe.tupcavite.edu.ph',
			height= '180',
			weight='70',
			foodallergens = 'Nuts')

		Info.objects.create(
			fullname='Symon',
			sex='Male',
			age ='22',
			email =  'syyy@gsfe.tupcavite.edu.ph',
			height= '183',
			weight='69',
			foodallergens = 'Fish')
		response = self.client.get('/')
		self.assertIn('Symon, Male, 22 years old, syyy@gsfe.tupcavite.edu.ph, 183cm, 69kg, Fish,', response.content.decode())
		self.assertIn('Gabriel, Male, 2O years old, gabby@gsfe.tupcavite.edu.ph, 180cm, 70kg, Nuts', response.content.decode())








