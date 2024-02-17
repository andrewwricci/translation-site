from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect

from .models import Original_Text

from .forms import OriginalTextForm


def index(request):
    original_text_form = OriginalTextForm

    # allow users to change the status of original text while in 受付待ち or 下書き state
    original_text_list = Original_Text.objects.filter(user_id=request.user)
    latest_original_text_list = original_text_list.order_by("-last_updated_datetime")
    paginator = Paginator(latest_original_text_list, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'original_text_form': original_text_form, 
        'latest_original_text_list': latest_original_text_list,
        "page_obj": page_obj
        }
    return render(request, "translations/index.html", context)

def detail(request, original_text_id):
    original_text = get_object_or_404(Original_Text, pk=original_text_id, user_id=request.user)
    return render(request, "translations/detail.html", {"original_text": original_text})

def addOriginalText(request):
    form = OriginalTextForm

    if request.method == 'POST':
        form = OriginalTextForm(request.POST)
        if form.is_valid():
            form.instance.user_id = request.user
            form.save()
    return redirect('translations:index')

# def results(request, original_text_id):
#     response = "You're looking at the translation results of original_text %s."
#     return HttpResponse(response % original_text_id)
