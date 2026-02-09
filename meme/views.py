import hashlib
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status

from .models import Meme
from .serializers import MemeSerializer
from meme.services.image_processor import overlay_caption
from meme.services.caption_generator import generate_caption


class MemeGeneratorView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        prompt = request.data.get("prompt")
        image = request.FILES.get("image")

        if not prompt or not image:
            return Response(
                {
                    "error": "Prompt and Image required",
                    "debug": {
                        "data": request.data,
                        "files": list(request.FILES.keys())
                    }
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        cache_key = hashlib.md5(prompt.encode()).hexdigest()
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response({**cached_data, "cached": True})

        image_path = f"media/uploads/{image.name}"
        with open(image_path, "wb+") as f:
            for chunk in image.chunks():
                f.write(chunk)

        caption = generate_caption(prompt)
        meme_path = overlay_caption(image_path, caption)

        meme = Meme.objects.create(
            prompt=prompt,
            caption=caption,
            image_path=meme_path
        )

        response_data = MemeSerializer(meme).data
        cache.set(cache_key, response_data, timeout=3600)

        return Response({**response_data, "cached": False})
