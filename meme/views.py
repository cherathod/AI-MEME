from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .services.caption_generator import generate_caption
from .services.image_processor import add_caption


