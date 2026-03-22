from django.shortcuts import render, get_object_or_404
from .models import Question, Choice, Submission


def submit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        selected_choice_id = request.POST.get("choice")
        selected_choice = Choice.objects.get(pk=selected_choice_id)

        Submission.objects.create(
            student_name="Student",
            question=question,
            selected_choice=selected_choice
        )

        return show_exam_result(request)

    return render(request, "submit.html", {"question": question})


def show_exam_result(request):
    submissions = Submission.objects.all()

    score = 0
    total = submissions.count()

    for s in submissions:
        if s.selected_choice.is_correct:
            score += 1

    context = {
        "score": score,
        "total": total
    }

    return render(request, "result.html", context)
