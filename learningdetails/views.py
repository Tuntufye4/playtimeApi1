import os
import uuid

from gtts import gTTS

from django.conf import settings

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import LearningDetails
from .serializers import LearningDetailsSerializer   


class LearningDetailsViewSet(viewsets.ModelViewSet):

    queryset = LearningDetails.objects.all()   
    serializer_class = LearningDetailsSerializer

    @action(
        detail=True,
        methods=["post"],
        url_path="tts"
    )
    def text_to_speech(self, request, pk=None):

        # Get lesson
        lesson = self.get_object()

        # Get text
        input_text = lesson.input

        if not input_text:
            return Response(
                {
                    "error": "No text available for speech"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create speech directory
        speech_dir = os.path.join(
            settings.MEDIA_ROOT,
            "speech"
        )

        os.makedirs(
            speech_dir,
            exist_ok=True
        )

        # Create unique filename
        filename = f"{uuid.uuid4()}.mp3"

        filepath = os.path.join(
            speech_dir,
            filename
        )

        try:

            # Generate speech using Google TTS
            tts = gTTS(
                text=input_text,
                lang="en",
                slow=False
            )

            # Save MP3
            tts.save(filepath)

        except Exception as e:

            return Response(
                {
                    "error": f"Text-to-speech generation failed: {str(e)}"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # Public URL
        audio_url = request.build_absolute_uri(
            settings.MEDIA_URL
            + "speech/"
            + filename
        )

        # Save audio URL
        lesson.con_audio = audio_url
        lesson.save(update_fields=["con_audio"])

        return Response(
            {
                "id": lesson.id,
                "title": lesson.title,
                "text": input_text,
                "audio": lesson.con_audio
            },
            status=status.HTTP_200_OK
        )