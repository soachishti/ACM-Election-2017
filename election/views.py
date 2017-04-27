from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import VoteForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth import logout
from .models import Profile, Vote

members = {
    "shaleem": {
        "id": "shaleem",
        "name" : "Shaleem John",
        "url": "/static/shaleem.jpg"
    },
    "owais": {
        "id": "owais",
        "name" : "Syed Owais Ali Chishti",
        "url": "/static/owais.jpg"
    },
    "haris": {
        "id": "haris",
        "name" : "Haris Jabbar",
        "url": "/static/haris.jpg"
    },
    "saad": {
        "id": "saad",
        "name" : "Saad Mansoor",
        "url": "/static/saad.jpg"
    },
    "aziz": {
        "id": "aziz",
        "name" : "Aziz Ullah",
        "url": "/static/aziz.jpg"
    },
    "asjad": {
        "id": "asjad",
        "name" : "Asjad Khan",
        "url": "/static/asjad.jpg"
    },
    "ahmad": {
        "id": "ahmad",
        "name" : "Muhammad Ahmad",
        "url": "/static/ahmad.jpg"
    },
    "najeeb": {
        "id": "najeeb",
        "name" : "Najeeb Khan",
        "url": "/static/najeeb.jpg"
    },
    "hanzaila": {
        "id": "hanzaila",
        "name" : "CH Hanzaila Maqsood",
        "url": "/static/hanzaila.jpg"
    },
    "rizwan": {
        "id": "rizwan",
        "name" : "Rizwan Muhammad",
        "url": "/static/rizwan.jpg"
    },
    "moiz": {
        "id": "moiz",
        "name" : "Abdul Moiz Rana",
        "url": "/static/moiz.jpg"
    },
    "afraz": {
        "id": "afraz",
        "name" : "Sayyed Afraz Hassan",
        "url": "/static/afraz.jpg"
    }
}

elected = [
    ({"Chairperson" :            [members["shaleem"]]}),
    ({"Vice Chairperson" :       [members["haris"], members["saad"], members["asjad"], members["aziz"]]}),
    ({"Asst. Vice Chairperson" : [members["saad"], members["owais"], members["najeeb"], members["asjad"]]}),
    ({"General Secretary" :      [members["owais"], members["ahmad"]]}),
    ({"Asst. General Secretary" :[members["najeeb"], members["hanzaila"]]}),
    ({"Treasurer" :              [members["rizwan"], members["moiz"], members["afraz"]]}),
    ({"Event Coordinator" :      [members["ahmad"], members["aziz"], members["hanzaila"]]})
]

def index(request):
    return redirect("login")

def thank(request):
    return render(request, 'thank.html')

def result(request):
    vote_casted = Vote.objects.values('position').order_by().annotate(position_count=Count('position')).distinct()
    casted_vote = 0
    try:
    	casted_vote = vote_casted[0]['position_count'] 
    except Exception:
    	casted_vote = 0

    result = Vote.objects.values('vote', 'position').order_by().annotate(vote_count=Count('vote'),position_count=Count('position')).order_by('-vote_count')
    return render(request, 'result.html', {'result': result, 'members': members, 'vote_casted': casted_vote})

@login_required
def vote(request):
    profile = Profile.objects.get(user_id=request.user.id)
    voted = profile.voted

    if request.method == 'POST' and not voted:        
        for position, candidates in request.POST.items():
            if position.find("csrf") != -1:
                continue

            voted_candidate = request.POST[position]
            
            v = Vote(position=position, vote=voted_candidate)
            v.save()

        profile = Profile.objects.get(user_id=request.user.id)
        profile.voted = True
        profile.save()

        logout(request)

        return redirect("thank")
       
    return render(request, 'vote.html', {'voted': voted, 'elected': elected, "members": members, "username": request.user.username})

def init(request):
    data = [('acm100', '@tji13'), ('acm101', '@biq88'), ('acm102', '@zpr14'), ('acm103', '@znd80'), ('acm104', '@crj41'), ('acm105', '@lfq65'), ('acm106', '@fiv72'), ('acm107', '@njp63'), ('acm108', '@jum93'), ('acm109', '@ple68'), ('acm110', '@jzp85'), ('acm111', '@imi42'), ('acm112', '@urv59'), ('acm113', '@emf98'), ('acm114', '@stp21'), ('acm115', '@pmz17'), ('acm116', '@wje24'), ('acm117', '@ojn48'), ('acm118', '@whn24'), ('acm119', '@vsi10'), ('acm120', '@kup88'), ('acm121', '@gak71'), ('acm122', '@mfe50'), ('acm123', '@psw45'), ('acm124', '@idc88'), ('acm125', '@jpa71'), ('acm126', '@qpl83'), ('acm127', '@ovq97'), ('acm128', '@kqx84'), ('acm129', '@iul82'), ('acm130', '@xkz67'), ('acm131', '@grs45'), ('acm132', '@tcz37'), ('acm133', '@lkt36'), ('acm134', '@bjz61'), ('acm135', '@zlz85'), ('acm136', '@pia40'), ('acm137', '@jdr88'), ('acm138', '@fbx86'), ('acm139', '@gmd44'), ('acm140', '@ees46'), ('acm141', '@sim46'), ('acm142', '@ldg39'), ('acm143', '@dxr35'), ('acm144', '@dqj68'), ('acm145', '@iox49'), ('acm146', '@acp90'), ('acm147', '@epn78'), ('acm148', '@kfp92'), ('acm149', '@fov59')];
    
    for value in data:
        user = User(username=value[0])
        user.set_password(value[1])
        user.save()
        profile = Profile(user=user)
        profile.save()

    return redirect("login")