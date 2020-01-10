from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .forms import ContactForm
from django.views import View
from django.template.loader import render_to_string
# Create your views here.

#FBV
def contactPage(request):
	form = ContactForm()
	return render(request, "contact.html", {"contactForm": form})

# def postContact(request):
# 	if request.method == "POST" and request.is_ajax():
# 		form = ContactForm(request.POST)
# 		temperatura = request.POST.get("temperatura")
# 		print(temperatura)
# 		form.save()
# 		# return JsonResponse({"success":True}, status=200)
# 		# return JsonResponse({"temperatura": temperatura})
# 		return render(request, "contact.html", {"temperatura" : temperatura})
# 	temperatura = request.POST.get("temperatura")
# 	# context = {
# 	# 	"temperatura" : temperatura
# 	# }
# 	# print(temperatura)
# 	#  return HttpResponse("Any kind of HTML Here") 
# 	return render(request, "contact.html", {"temperatura" : temperatura})
# 	# return JsonResponse({"temperatura": temperatura})

def postContact(request):
	if request.method == "POST" and request.is_ajax():
		temperatura = request.POST.get("temperatura")
		umidita = request.POST.get("umidita")
		temperatura = float(temperatura)
		umidita = float(umidita)
		
		# TEMPF = temperatura * 9 / 5 + 32
		# HI = -42.379 + 2.04901523*TEMPF + 10.14333127*umidita - 0.22475541*TEMPF*umidita \
        #          - 0.00683783*TEMPF**2 - 0.05481717*umidita**2 + 0.00122874*TEMPF**2*umidita \
        #          + 0.00085282*TEMPF*umidita**2 - 0.00000199*TEMPF**2*umidita**2

		HI = -42.379 + 2.04901523*temperatura + 10.14333127*umidita - 0.22475541*temperatura*umidita \
                 - 0.00683783*temperatura**2 - 0.05481717*umidita**2 + 0.00122874*temperatura**2*umidita \
                 + 0.00085282*temperatura*umidita**2 - 0.00000199*temperatura**2*umidita**2

		result = round(float(HI),2)

		# html = render_to_string("contact.html", {'temperatura': temperatura})
	return HttpResponse(result)

#CBV
class ContactAjax(View):
	form_class = ContactForm
	template_name = "contact_cbv.html"

	def get(self, *args, **kwargs):
		form = self.form_class()
		return render(self.request, self.template_name, {"contactForm": form})

	def post(self, *args, **kwargs):
		if self.request.method == "POST" and self.request.is_ajax():
			form = self.form_class(self.request.POST)
			form.save()
			return JsonResponse({"success":True}, status=200)
		return JsonResponse({"success":False}, status=400)