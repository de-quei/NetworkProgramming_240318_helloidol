from django.shortcuts import render

# Create your views here.

group = {
    'members':[
        {
            'group_name': 'mrs.greenapple',
            'name': 'omori',
            'img_src': 'mrsgreenapple/images/me.jpg'
            # 'img_src': 'https://i.pinimg.com/564x/7e/ed/07/7eed071c0b6809f13c6e2ff14038b520.jpg',
        },
        {
            'group_name': 'mrs.greenapple',
            'name': 'wakai',
            'img_src': 'mrsgreenapple/images/me.jpg'
            #'img_src': 'https://i.pinimg.com/736x/43/2c/ec/432cec0441b89f90af0c9c9917173188.jpg',
        },
    ]
}

def show_omori_html(request):
    context = list(filter(lambda member: 'omori' in member['name'], group['members']))[0]
    #context = group['members'][0]
    return render(request, 'mrsgreenapple/member.html', context=context)

def show_wakai_html(request):
    context = list(filter(lambda member: 'wakai' in member['name'], group['members']))[0]
    #context = group['members'][1]
    return render(request, 'mrsgreenapple/member.html', context=context)

def show_member(request, member_):
    context = list(filter(lambda member: member_ in member['name'], group['members']))[0]
    return render(request, 'mrsgreenapple/member.html', context=context)

def show_member_list(request):
    context = group #{'members':[{member1}, {member2}, ]}
    return render(request, 'mrsgreenapple/member_list.html', context=context)