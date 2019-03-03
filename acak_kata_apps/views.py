from django.shortcuts import render
import random
from acak_kata_apps.models import Kata
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import redirect
from acak_kata_apps.DifficultyStrategy import Difficulty, Easy, Medium, Hard

def get_kata_random():
	# <view logic>
		id_kata_terpilih = random.randint(1,28526)
		list_kata_random_terpilih = list(Kata.objects.get(pk=id_kata_terpilih).kata)

		hasil_permutasi_kata = "".join(random.sample(list_kata_random_terpilih,len(list_kata_random_terpilih)))
		kata_random_terpilih = "".join(list_kata_random_terpilih)

		dict_kata = {"hasil_permutasi_kata" : hasil_permutasi_kata, "kata_asli" : kata_random_terpilih, "id_kata" : id_kata_terpilih}
		return dict_kata

class GameView(View):
	def get(self, request, selected_difficulty):
		dict_kata = get_kata_random()
		if selected_difficulty == "easy":
			difficulty = Difficulty(Easy())
		elif selected_difficulty == "medium":
			difficulty = Difficulty(Medium())
		else:
			difficulty = Difficulty(Hard())

		dict_kata['difficulty'] = difficulty
		dict_kata['selected_difficulty'] = selected_difficulty
		return render(request,'acak_kata_apps/game.html',dict_kata)

	def post(self,request,selected_difficulty):
		tebakan = request.POST['tebakan']
		id_kata = request.POST['id_kata']
		jawaban_benar = Kata.objects.get(pk=id_kata).kata
		if(tebakan == jawaban_benar):
			output = "Selamat! jawaban anda benar. Point anda : "
			result = True
		else:
			output = "Maaf, jawaban anda salah. Silahkan coba lagi"
			result = False

		kesempatan_menjawab = request.POST['kesempatan_menjawab']
		if(result or int(kesempatan_menjawab) == 0):
			dict_kata = get_kata_random()
			dict_kata['result'] = result
			dict_kata['jawaban_benar'] = jawaban_benar;
			response = JsonResponse(dict_kata)
			return response

		else:
			response = JsonResponse({'output' : output, 
			'result' : result, 'jawaban_benar' : jawaban_benar});
			return response

	@csrf_exempt
	def dispatch(self, request, *args, **kwargs):
		return super(GameView, self).dispatch(request, *args, **kwargs)

class IndexView(View):
	def get(self, request):
		return render(request,'acak_kata_apps/index.html')

class SelectDifficultyView(View):
	def get(self, request):
		return render(request,'acak_kata_apps/select_difficulty.html')

	def post(self,request):
		selected_difficulty = request.POST.get('difficulty_option')
		return redirect('game',selected_difficulty=selected_difficulty)

