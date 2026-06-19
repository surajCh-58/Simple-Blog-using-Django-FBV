from django.shortcuts import *
from . models import *
from . forms import *
def InsertEdit(request,pk=None):
    instance=get_object_or_404(blog_db,id=pk) if pk else None
    if (request.method=="POST"):
        form=Post_Form(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect("allpost")
    else:
        form=Post_Form(instance=instance)
        return render(request,"insertedit.html",{'form':form})
def AllPost(request):
    post=blog_db.objects.all()
    return render(request,"allpost.html",{'post':post})
def DeletePost(request,pk):
    post=get_object_or_404(blog_db,id=pk)
    if request.method=="POST":
        post.delete()
        return redirect("allpost")
    return render(request,"postdelete.html",{'post':post})
def ViewPost(request,pk):
    post=get_object_or_404(blog_db,id=pk)
    return render(request,"viewpost.html",{'post':post})