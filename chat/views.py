import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from agents import Runner
from .router import triage
from django.shortcuts import render

def index_view(request):
    return render(request, 'chat/chat.html')
@csrf_exempt
async def chat_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    data = json.loads(request.body)
    message = data.get("message", "")

    result = await Runner.run(triage, input=message)

    return JsonResponse({"reply": result.final_output})
