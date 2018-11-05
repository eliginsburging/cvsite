from django.shortcuts import render
from .models import Quotation

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
    quotes = Quotation.objects.all()
    pics = ['portrait.jpg', 'ACT.jpg', 'greeksoy2.png', 'me.jpg']
    return render(request, 'home.html', locals())
