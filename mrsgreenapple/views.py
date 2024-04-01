from django.shortcuts import render

# Create your views here.

group = {
    'members':[
        {
            'group_name': 'mrs.greenapple',
            'name': 'omori motoki',
            'img_src': 'https://i.pinimg.com/564x/7e/ed/07/7eed071c0b6809f13c6e2ff14038b520.jpg',
        },
        {
            'group_name': 'mrs.greenapple',
            'name': 'wakai hiroto',
            'img_src': 'https://i.pinimg.com/564x/7e/ed/07/7eed071c0b6809f13c6e2ff14038b520.jpg',
        },
    ]
}

def show_omori_html(request):
    context = list(filter(lambda member: 'omori motoki' in member['name'], group['members']))[0]
    #context = group['members'][0]
    return render(request, 'mrsgreenapple/member.html', context=context)

def show_wakai_html(request):
    context = list(filter(lambda member: 'wakai hiroto' in member['name'], group['members']))[0]
    #context = group['members'][1]
    return render(request, 'mrsgreenapple/member.html', context=context)


