import django.http
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EntryForm, TopicForm
from .models import Entry, Topic


# Check topic owner.
def check_topic_owner(topic, request):
    if topic.owner != request.user:
        raise django.http.Http404


# Create your views here.
def index(request):
    """The home page for Learning logs."""
    return render(request, "learning_logs/index.html")


@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)


@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = get_object_or_404(
        Topic, id=topic_id
    )  # lấy object Topic từ database (đã có sẵn field id)
    # Make sure the topic belongs to the current user.
    check_topic_owner(topic, request)

    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}  # đóng gói gửi qua template
    return render(request, "learning_logs/topic.html", context)


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect("learning_logs:topics")

    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)


@login_required
def edit_topic(request, topic_id):
    """Edit an existing entry."""
    topic = get_object_or_404(Topic, id=topic_id)

    check_topic_owner(topic, request)

    if request.method != "POST":
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=topic)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topics")  # quay về trang topics
    context = {"topic": topic, "form": form}
    return render(request, "learning_logs/edit_topic.html", context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = get_object_or_404(Topic, id=topic_id)

    check_topic_owner(topic, request)

    if request.method != "POST":
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(request.POST)  # nhét dữ liệu user nhập vào form
        if form.is_valid():  # kiểm tra hợp lệ
            new_entry = form.save(
                commit=False
            )  # tạo Entry (có text), chưa ghi database
            new_entry.topic = topic  # gán topic (lấy từ topic_id trên URL)
            new_entry.save()  # ghi vào database
            return redirect(
                "learning_logs:topic", topic_id=topic_id
            )  # quay về trang topic

    context = {"topic": topic, "form": form}
    return render(request, "learning_logs/new_entry.html", context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    check_topic_owner(topic, request)

    if request.method != "POST":
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "learning_logs:topic", topic_id=topic.id
            )  # quay về trang topic
    context = {"entry": entry, "topic": topic, "form": form}
    return render(request, "learning_logs/edit_entry.html", context)


@login_required
def delete_topic(request, topic_id):
    """Confirm and delete a topic."""
    topic = get_object_or_404(Topic, id=topic_id)
    check_topic_owner(topic, request)

    if request.method == "POST":
        topic.delete()
        return redirect("learning_logs:topics")

    context = {"topic": topic}
    return render(request, "learning_logs/delete_topic.html", context)


@login_required
def delete_entry(request, entry_id):
    """Confirm and delete an entry."""
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic

    check_topic_owner(topic, request)

    if request.method == "POST":
        entry.delete()
        return redirect("learning_logs:topic", topic_id=topic.id)
    context = {"entry": entry, "topic": topic}
    return render(request, "learning_logs/delete_entry.html", context)
