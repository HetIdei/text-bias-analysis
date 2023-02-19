from django.shortcuts import render
from myapp1.models import Text
from myapp1.models import Answer
import random

# Create your views here.


def index_page(request):


    #new_worker = Worker(name='Ivan', second_name='Ivanov', salary=110)
    #new_worker.save()

    '''person = Worker.objects.get(id=5)
    person.second_name='Petrov'
    person.save()


    all_workers = Worker.objects.all()

    for i in all_workers:
        print(i.name,' --- ', i.salary, ' --- ', i.pk)


    workers_filtered = Worker.objects.filter(salary=500)'''

    text = Text.objects.get(id=random.randint(1,4))

    ans = request.GET.get('name')
    text_new = Text()
    text_new.text = text.text



    text_new.asnwers = Answer.objects.get(id = 1)
    text_new.save()


    #text = "SERTFGAWSRTR"
    

    return render(request, 'index.html', {'text': text})