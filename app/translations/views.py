from django.shortcuts import get_object_or_404, render

from .models import Original_Text

from .forms import OriginalTextForm


def index(request):
    form = OriginalTextForm

    if request.method == 'POST':
        form = OriginalTextForm(request.POST)
        if form.is_valid():
            form.save()

    latest_original_text_list = Original_Text.objects.order_by("-last_updated_datetime")[:5]
    context = {'form': form, "latest_original_text_list": latest_original_text_list}
    return render(request, "translations/index.html", context)

def detail(request, original_text_id):
    original_text = get_object_or_404(Original_Text, pk=original_text_id)
    return render(request, "translations/detail.html", {"original_text": original_text})

# def results(request, original_text_id):
#     response = "You're looking at the translation results of original_text %s."
#     return HttpResponse(response % original_text_id)
