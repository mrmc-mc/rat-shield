from django.shortcuts import render,redirect , HttpResponse
from django.views import View
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.core.paginator import Paginator


class Index(View):
        

        def get(self,request):
                context={}
                obj = models.PostData.objects.all().order_by("-id")

                p = Paginator(obj, 100)  # creating a paginator object
                # getting the desired page number from url
                page_number = request.GET.get('page')
                try:
                        page_obj = p.get_page(page_number)  # returns the desired page object
                except PageNotAnInteger:
                        # if page_number is not an integer then assign the first page
                        page_obj = p.page(1)
                except EmptyPage:
                        # if page is empty then return last page
                        page_obj = p.page(p.num_pages)
                context = {'msg': page_obj}

                return render(request,"technical/index.html",context)


        @csrf_exempt
        def post(self, request):
                print(request.POST)
                db = models.PostData()
                db.data = request.POST
                if request.FILES:
                        db.file = request.FILES
                db.save()


                return HttpResponse("OK",status=201)

