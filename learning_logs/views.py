from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """ Home page """
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ All topics """
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """ Detailed information about a single topic """
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """ Add a new topic """
    if request.method != 'POST': # If there is no data submitted
        form = TopicForm() # Create blank form
    else: # data submitted
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """ Add a new entry """
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST': # If there is no data submitted
        form = EntryForm() # Create blank form
    else: # Data submitted
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    """ Edit existing entry """
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST': # No new data subbmited yet
        form = EntryForm(instance=entry) # pre-fill form with current entry data
    else: # new data submitted
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)
