from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.
def get_todo_list(request):
    results = Item.objects.all()
    return render(request, "todo_list.html", {'items': results})

""" New way
"""
def create_an_item(request):
    # POST object will be a dictionnary 
    if request.method=="POST":
        # FILES is usually used to make sure if there's any files being uploaded
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    # if the request is not a post request then we just want to return an empty form so we say form is equal to ItemForm.
    else:
        form = ItemForm()

    return render(request, "item_form.html", {'form': form})

""" Old way
def create_an_item(request):
    # POST object will be a dictionnary 
    if request.method=="POST":
        new_item = Item()
        new_item.name = request.POST.get("name")
        # we need to say new_item.done is equal to done in request.post so if done is present in the request.post then it will be true otherwise it will be false
        new_item.done = 'done' in request.POST
        new_item.save()

        return redirect(get_todo_list)
    return render(request, "item_form.html")
    """

def edit_an_item(request, id):
    """I'm going to say get_object_or_404 and inside of that 
    I'm going to say item I want to get the object from the item table model and the specific one that I want is the primary key or PK with value equal to the ID and a get_object_or_404 needs to be imported from Django
    if it cannot find the specific instance with this ID that we're passing in then it will throw a 404 error, resource not found error.
    """
    item = get_object_or_404(Item, pk=id)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    # if it's not a POST request then it will run the else statement.
    else:
        form = ItemForm(instance=item)

    return render(request, "item_form.html", {'form': form})

def toggle_status(request, id):
    """we say item done is equal to not item done so if item is done then it will set it to false
    and if the item is not done then it will set it to true
    """
    item = get_object_or_404(Item, pk=id)
    item.done = not item.done
    item.save()
    return redirect(get_todo_list)