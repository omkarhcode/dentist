from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html', {})

def patients(request):
	return render(request, 'patients.html', {})

def news(request):
	return render(request, 'news.html', {})

def services(request):
	return render(request, 'services.html', {})

def contact(request):
	if request.method == "POST":
		user_name = request.POST['fullname']
		user_email = request.POST['email']
		user_message = request.POST['message']

		# Send an email
		send_mail('Email from '+user_name,user_message, user_email, ['omkarhcode@gmail.com'])

		return render(request, 'contact.html', {'user_name': user_name})
	else:
		return render(request, 'contact.html', {})


def appointment(request):
	if request.method == "POST":
		firstname = request.POST['fname']
		lastname = request.POST['lname']
		dateofvisit = request.POST['date']
		customeremail = request.POST['email']
		treatment = request.POST['treatment']
		additionalnote = request.POST['note']

		# Send an email
		# send_mail('Email from '+user_name,user_message, user_email, ['omkarhcode@gmail.com'])

		return render(request, 'appointment.html', {			
			'firstname': firstname,
			'lastname': lastname,
			'dateofvisit': dateofvisit,
			'customeremail': customeremail,
			'treatment': treatment,
			'additionalnote': additionalnote,
			})
	else:
		return render(request, 'home.html', {})

