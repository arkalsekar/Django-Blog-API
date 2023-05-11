from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import Blog

# Home View
def home(request):
    data = {"Endpoints": "Below are the Endpoints for the usage of this API", 
            "/getAll": "Returns all the Existing Objects from the Database",
            "/get/id": "Returns Specific Object based on the Id", 
            "/drop/id": "Drops/Deletes Specific object from the Database",
            "/update": "Updates the Existing Post from the Database",
            "/insert": "Takes a POST request and inserts data into the Database",
            "/search?query=": "Returns Blogs based on the Searh Query"}
    return JsonResponse(data)

# Get All Objects from the Database
def getAll(request):
    all_blogs = Blog.objects.all()
    data = {"results": list(all_blogs.values("id", "author", "title", "content", "tags"))}
    print(data)
    return JsonResponse(data)

# Get Specific Objects from the Database
def get(request, id):
    blog = get_object_or_404(Blog, id=id)
    data = {"results": {
        "id": blog.id,
        "author": blog.author,
        "title": blog.title,
        "content": blog.content,
    }}
    return JsonResponse(data)
    
# Insert / PUT data into the Database
@csrf_exempt
def insert(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        content = request.POST['content']
        if len(title) > 5 and len(author) > 2 and len(content) >3:
            blog = Blog(title=title, author=author, content=content)
            blog.save()
            return JsonResponse({"Success": "Blog has been Added Successfully got the Data"})
        else:
            return JsonResponse({"Invalid Length": "Length of all the Fields must be greater than 5"})
            
    else:
        return JsonResponse({"Invalid Request Type": "Request Type POST Expected."})
    
# Delete / Drop Specific Data
def drop(request, id):
    blog = get_object_or_404(Blog, id=id)
    if blog:
        blog.delete()
        return JsonResponse({"Success": f"Data with the {id} was deleted Successfully"})
    else:
        return JsonResponse({"Failure": "Data with the Specific Id was not Found"})

# Searchs Through the Fields and Returns Blogs based on that        
def search(request):
    query = request.GET['query']
    blog = Blog.objects.filter(title__icontains=query) or Blog.objects.filter(author__icontains=query) or Blog.objects.filter(content__icontains=query)
    data = {"results" : list(blog.values("id", "author", "title", "content", "tags"))} 
    return JsonResponse(data)

   
@csrf_exempt
def update(request):

    if request.method == "POST":
        id = request.POST['id']
        title = request.POST['title']
        author = request.POST['author']
        content = request.POST['content']
        if len(title) > 5 and len(author) > 2 and len(content) >3:
            blog = Blog.objects.filter(id=id)
            blog.update(title=title, author=author, content=content)
            print("Udpated Successfully")
            return JsonResponse({"Success": f"Blog with id {id} has been Updated Successfully"})
        else:
            return JsonResponse({"Invalid Length": "Length of all the Fields must be greater than 5"})
            
    else:
        return JsonResponse({"Invalid Request Type": "Request Type POST Expected."})
