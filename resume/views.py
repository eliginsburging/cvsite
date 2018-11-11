from django.shortcuts import render
from .models import Quotation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuotationSerializer

# Create your views here.


def index_page(request):
    welcome_text = ("My name is Eli Ginsburg-Marcy, and I would like to "
                    "welcome you to my personal website. The original idea "
                    "behind this site was to provide an extended version of "
                    "my resume, but during my third rebuild, I decided to "
                    "showcase more than just my work and educational history. "
                    "I hope that in looking over the site, you can get a"
                    " better sense of who I am, professionally and on a more "
                    "human level.")
    quote_list = Quotation.objects.only('author')
    starting_quote = Quotation.objects.get(pk=1)
    pics = ['portrait.jpg', 'ACT.jpg', 'greeksoy2.png', 'me.jpg']
    return render(request, 'home.html', locals())


@api_view(['GET'])
def quote_detail(request, author):
    """
    retrieve quote text and details by author namm
    """
    try:
        quote = Quotation.objects.get(author=author)
    except Quotation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = QuotationSerializer(quote)
    return Response(serializer.data)
