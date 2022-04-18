from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

from hosapp.models import*



# Create your views here.



def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def services(request):
	return render(request,'services.html')

def patient(request):
	if request.method =='POST':
		Name=request.POST['Name']
		email=request.POST['email']
		location=request.POST['locations']
		number=request.POST['Phoneno']
		time=request.POST['time']
		about=request.POST['problem']
		query=patient_tb(Name=Name,email=email,location=location,number=number,time=time,about=about)
		query.save()
	return render(request,'patient.html')


def patientlogin(request):
	if request.method=='POST':
		Name=request.POST['Name1']
		email=request.POST['email1']
		number=request.POST['Phoneno1']
		check= patient_tb.objects.all().filter(Name=Name,email=email,number=number)
		if check:
			for x in check:
				request.session['userid']=x.id
			return render(request,'about.html')
		else:
			return render(request,'patientlogin.html')
	else:
		return render(request,'patientlogin.html')
			

def logout(request):
	if request.session.has_key('userid'):
		del request.session['userid']
	return render(request,'patientlogin.html')	





def doctors(request):
	if request.method=='POST':
		dname=request.POST['drname']
		specailised=request.POST['special']
		available=request.POST['times']
		password=request.POST['password']
		query=Doctors_tb(dname=dname,specailised=specailised,available=available,password=password)
		query.save()
	return render(request,'doctor.html')


def drlogin(request):
	if request.method=='POST':
		Name=request.POST['drname1']
		password=request.POST['password1']
		check=Doctors_tb.objects.all().filter(dname=Name,password=password)
		if check:
			for x in check:
				request.session['userid']=x.id
			return render(request,'services.html')
		else:
			return render(request,'drlogin.html')
	else:
		return render(request,'drlogin.html')




def booking(request):
	if request.session.has_key('userid'):
		if request.method=='POST':
			drids=request.POST['drn']
			time=request.POST['time2']
			date=request.POST['date']
			problems=request.POST['des1']
			pid=request.session['userid']
			drid=Doctors_tb.objects.get(id=drids)
			paid=patient_tb.objects.get(id=pid)
			query=token_tb(time=time,date=date,problems=problems,pid=paid,drid=drid)
			query.save()
		viewquery=Doctors_tb.objects.all()
		return render(request,'booking.html',{'viewquery':viewquery})
	else:
		return render(request,'patientlogin.html')



def view(request):
	viewquery=Doctors_tb.objects.all()
	return render(request,'viewajas.html',{'viewquery':viewquery})



def viewajas(request):
	print("xxxxxxxxxxxxxxxxxxxxxxxx")
	doct=request.GET.get('docid')
	doid=Doctors_tb.objects.all().filter(id=doct)
	print(doid)
	for x in doid:
		doname=x.Name
		dospecial=x.specailised
		dotime=x.time
	doctr={"dname":doname,"dspecial":dospecial,"dtime":dotime}
	print(doctr)
	return JsonResponse(doctr)
			
