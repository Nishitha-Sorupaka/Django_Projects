from django.shortcuts import render

# Create your views here.
def news_info(request):
    return  render(request,'testapp/index.html')

def movies_view(request):
    head_msg = 'Movies Information'
    sub_msg1 = 'Jailer is very good movie'
    sub_msg2 = 'Upcoming pawan kalyan movie is OG'
    sub_msg3 = 'RRR movie won Oscars'
    type = 'movies'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def sports_view(request):
    head_msg = 'Sports Information'
    sub_msg1 = 'India will won next world cup'
    sub_msg2 = 'Tomorrow there is no matches'
    sub_msg3 = 'Next year T20 world cup'
    type = 'sports'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def politics_view(request):
    head_msg = 'Politics Information'
    sub_msg1 = 'India PM was and is Modi Ji'
    sub_msg2 = 'Nov-30 Telangana elections....'
    sub_msg3 = 'Who is nect CM for AP?'
    type = 'politics'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)


    