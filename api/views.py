from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseForbidden
from django.http import HttpResponseServerError
from .models import Submission


class Apply_song(View):
    def get(self, request):
        return render(request, 'apply.html')

    def post(self, request):
        submitter = request.POST.get('submitter')
        submitterID = request.POST.get('submitterID')
        song_name = request.POST.get('song_name')
        song_singer = request.POST.get('song_singer')
        if submitterID == '' or submitter == '' or song_name == '':  # 未輸入
            return HttpResponseForbidden("未填寫完成")
        try:
            Submission(submitter=submitter, submitterID=submitterID,
                       song_name=song_name, song_singer=song_singer
                       ).save()
        except expression:
            return HttpResponseServerError(expression)
        print("Success")
        return render(request, 'success.html')


class homepage(View):
    def get(self, request):
        return render(request, 'home.html', {
            'songs': Submission.objects.all()
        })
