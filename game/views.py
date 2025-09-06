from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import GameSave
import json
import random

def generate_array(difficulty, length):
    """Generate array based on difficulty and length"""
    arr = list(range(1, length + 1))
    
    
    if difficulty == 'easy':
        for _ in range(length // 4):
            i, j = random.sample(range(length), 2)
            arr[i], arr[j] = arr[j], arr[i]
    elif difficulty == 'medium':
        for _ in range(length // 2):
            i, j = random.sample(range(length), 2)
            arr[i], arr[j] = arr[j], arr[i]
    else: 
        random.shuffle(arr)
    
    return arr

def validate_move(algorithm, arr, move_from, move_to, step):
    """Validate if move follows algorithm rules"""
    if algorithm == 'bubble':
        return abs(move_from - move_to) == 1 and arr[move_from] > arr[move_to]
    
    elif algorithm == 'selection':
        if step >= len(arr):
            return False
        if move_from != step:
            return False
        min_idx = step
        for i in range(step + 1, len(arr)):
            if arr[i] < arr[min_idx]:
                min_idx = i
        return move_to == min_idx and move_from != move_to
    
    elif algorithm == 'insertion':
        if step >= len(arr) - 1:
            return False
        if move_from != step + 1:
            return False
        element = arr[move_from]
        correct_pos = 0
        for i in range(step + 1):
            if arr[i] <= element:
                correct_pos = i + 1
        return move_to == correct_pos
    
    return False

def get_hint(algorithm, arr, step):
    """Generate hint for next move"""
    if algorithm == 'bubble':
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return f"Swap elements at positions {i} and {i + 1} ({arr[i]} and {arr[i + 1]})"
        return "Array is already sorted!"
    
    elif algorithm == 'selection':
        if step >= len(arr):
            return "Array is already sorted!"
        min_idx = step
        for i in range(step + 1, len(arr)):
            if arr[i] < arr[min_idx]:
                min_idx = i
        if min_idx == step:
            return f"Position {step} already has the minimum value ({arr[step]})"
        return f"Find minimum in unsorted portion: swap {arr[min_idx]} at position {min_idx} with position {step}"
    
    elif algorithm == 'insertion':
        if step >= len(arr) - 1:
            return "Array is already sorted!"
        element = arr[step + 1]
        correct_pos = 0
        for i in range(step + 1):
            if arr[i] <= element:
                correct_pos = i + 1
        return f"Insert element {element} from position {step + 1} to position {correct_pos}"
    
    return "No hint available"

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import GameSave
import json
import random

def home(request):
    return render(request, 'game/home.html')

def learn(request):
    return render(request, 'game/learn.html')
def game(request):
    load_id = request.GET.get('load')
    context = {'load_game_id': load_id} if load_id else {}
    return render(request, 'game/index.html', context)

def resume(request):
    if request.method == 'POST' and 'delete_game' in request.POST:
        game_id = request.POST['delete_game']
        GameSave.objects.filter(id=game_id).delete()
    
    saved_games = GameSave.objects.all().order_by('-updated_at')
    return render(request, 'game/resume.html', {'saved_games': saved_games})

@csrf_exempt
def new_game(request):
    data = json.loads(request.body)
    difficulty = data['difficulty']
    algorithm = data['algorithm']
    player_name = data.get('playerName', 'Player1')
    
    lengths = {'easy': (5, 15), 'medium': (16, 30), 'hard': (31, 50)}
    min_len, max_len = lengths[difficulty]
    length = random.randint(min_len, max_len)
    
    arr = generate_array(difficulty, length)
    
    game_save = GameSave.objects.create(
        player_name=player_name,
        algorithm=algorithm,
        difficulty=difficulty,
        score=0,
        moves=0,
        step=0
    )
    game_save.set_current_array(arr)
    game_save.set_original_array(arr)
    game_save.save()
    
    return JsonResponse({
        'array': arr,
        'algorithm': algorithm,
        'difficulty': difficulty,
        'length': length,
        'gameId': game_save.id
    })

@csrf_exempt
def validate_move_api(request):
    data = json.loads(request.body)
    algorithm = data['algorithm']
    arr = data['array']
    move_from = data['moveFrom']
    move_to = data['moveTo']
    step = data['step']
    game_id = data.get('gameId')
    
    is_valid = validate_move(algorithm, arr, move_from, move_to, step)
    
    if game_id:
        try:
            game_save = GameSave.objects.get(id=game_id)
            game_save.set_current_array(arr)
            game_save.score = data.get('score', game_save.score)
            game_save.moves = data.get('moves', game_save.moves)
            game_save.step = step
            game_save.hints_used = data.get('hintsUsed', game_save.hints_used)
            if data.get('isCompleted'):
                game_save.is_completed = True
            game_save.save()
        except GameSave.DoesNotExist:
            pass
    
    return JsonResponse({
        'valid': is_valid,
        'points': 1 if is_valid else -1
    })

@csrf_exempt
def get_hint_api(request):
    data = json.loads(request.body)
    algorithm = data['algorithm']
    arr = data['array']
    step = data['step']
    
    hint = get_hint(algorithm, arr, step)
    
    return JsonResponse({'hint': hint})

@csrf_exempt
def load_game(request):
    data = json.loads(request.body)
    game_id = data['gameId']
    
    try:
        game_save = GameSave.objects.get(id=game_id)
        return JsonResponse({
            'array': game_save.get_current_array(),
            'originalArray': game_save.get_original_array(),
            'algorithm': game_save.algorithm,
            'difficulty': game_save.difficulty,
            'score': game_save.score,
            'moves': game_save.moves,
            'step': game_save.step,
            'hintsUsed': game_save.hints_used,
            'playerName': game_save.player_name,
            'gameId': game_save.id
        })
    except GameSave.DoesNotExist:
        return JsonResponse({'error': 'Game not found'}, status=404)