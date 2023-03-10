from django.shortcuts import render,redirect
from django.http import HttpResponse
from core.models import Gallary
from django.contrib.auth.decorators import login_required
from gallery.forms import UploadImageForm
from django.core.paginator import Paginator

@login_required(login_url="/users/signin")
def home(request):
  if request.method == "POST":
    upload_form = UploadImageForm(request.POST,request.FILES)
    data={
      'upload_form':upload_form,
      'page_number':1,
      'total_pages':200,
    }
    if(upload_form.is_valid()):
      
      user = upload_form.save(commit=False)
      user.user_id  =request.user
      user.save()
      return redirect('/')
    else:
      return render(request,'gallary/index.html',{"data":data})
  else:
    upload_form = UploadImageForm()
    page_number = request.GET.get('page')
    user_images = Gallary.objects.all()
    p = Paginator(user_images, 5)
    user_images = p.get_page(page_number)
    try:
      user_images = p.get_page(page_number)
    except :
      user_images = p.page(p.num_pages)

    data={
      'upload_form':upload_form,
      'images' : user_images,
      'page_number':page_number,
    }
    
    return render(request,'gallary/index.html',{"data":data})
