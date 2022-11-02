from django.shortcuts import render
from submission.models import Track, Submission
from django.http import HttpResponse
from django.core import serializers

def show_submission(request):
    track_data = Track.objects.all()
    submission_data = Submission.objects.all()
    submission_filter = SubmissionFilter(request.GET, queryset=submission_data)
    context = {'track' : track_data,
                'submission_filter' : submission_filter}
    return render(request, "submission.html", context)

def show_details_by_id(request, id):
    track_data = Track.objects.filter(id=id)
    submission_data = Submission.objects.filter(id=id)
    context = {'track' : track_data,
                'submission' : submission_data}
    return render(request, "details.html", context)

def show_json(request):
    submission_data = Submission.objects.all()
    submission_filter = SubmissionFilter(request.GET, queryset=submission_data)
    return HttpResponse(serializers.serialize("json", submission_filter.qs), content_type="application/json")