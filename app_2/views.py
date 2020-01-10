from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
# Create your views here.

#FBV
def userPanel(request):
	usernames = User.objects.all().values("username")
	return render(request, "user.html", {"usernames": usernames})


def form_create_view(request,  *args, **kwargs):
	if request.method == 'POST' and request.is_ajax():
		temperatura = request.POST.get["temperatura"]
	temperatura = request.POST.get["temperatura"]
	print(temperatura)





def getUserInfo(request, *args, **kwargs):
	if request.method == 'POST' and request.is_ajax():
		temperatura = request.POST.get["temperatura"]
	temperatura = request.POST.get["temperatura"]
	print(temperatura)
	# if request.method == 'POST' and request.is_ajax():
	# 	temperatura = request.POST['temperatura']
	# 	print(temperatura)
	if request.method == "GET" and request.is_ajax():
		username = request.GET.get("username")
		print(username)
		# temperatura = request.GET.get("temperatura")
		# print(temperatura)
		try:
			user = User.objects.get(username = username)
		except:
			return JsonResponse({"success":False}, status=400)
		
		# temperatura = request.GET.get("temperatura")
		# try:
		# 	temperatura = request.POST.get("temperatura")
		# except:
		# 	return JsonResponse({"success":False}, status=400)

		user_info = {
			"first_name": user.first_name,
			"last_name": user.last_name,
			"email": user.email + str(" ciao"),
			# "temperatura": user.temperatura,
			"is_active": user.is_active,
			"joined": user.date_joined,
			# "temperatura": temperatura
		}
		return JsonResponse({"user_info":user_info}, status=200)
	return JsonResponse({"success":False}, status=400)