from django.shortcuts import render

# Create your views here.
def logNewIssue(request):
    if request.method=='POST':
        partNoV=request.POST['partNo']
        typeV = request.POST['type']
        descriptionV = request.POST['description']
        loggedByV = request.POST['loggedBy']

        x=User.objects.create_user(partNo=partNoV,type=typeV,description=descriptionV,loggedBy=loggedByV)
        x.save()
        print("user created")
        return redirect('/')
    else:
        return render(request, 'newIssue.html')