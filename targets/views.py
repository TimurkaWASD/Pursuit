from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import *

@login_required
def create_target(request):
    if request.method == 'POST':
        form = CreateTargetForm(request.POST, request.FILES)
        if form.is_valid():
            target = form.save(commit=False)
            target.user = request.user
            target.save()
            return redirect('profile')
    else:
        form = CreateTargetForm()
    return render(request, 'create_targets.html', {'form': form})

@login_required
def targets_list(request):
    targets = Target.objects.filter(user=request.user)
    return render(request, 'targets_list.html', {'targets': targets})


@require_POST
def change_favorite(request, target_id):
    target = Target.objects.get(id=target_id)
    target.favorite = not target.favorite  # Инвертируем текущее значение
    target.save()
    return redirect('targets_list')

@require_POST
def change_status(request, target_id):
    target = Target.objects.get(id=target_id)
    target.status = not target.status  # Инвертируем текущее значение
    target.save()
    return redirect('targets_list')

@require_POST
def change_rating(request, target_id):
    target = Target.objects.get(id=target_id)
    new_rating = int(request.POST.get('rating', 0))  # Получаем новое значение рейтинга из POST-запроса
    target.rating = max(0, min(5, new_rating))  # Ограничиваем рейтинг в пределах от 0 до 5
    target.save()
    return redirect('targets_list')