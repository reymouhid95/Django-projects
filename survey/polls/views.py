from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django import forms

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "Choix invalide! Il faut faire un choix avant de soumettre.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text"]


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["choice_text"]


ChoiceFormSet = forms.inlineformset_factory(
    Question, Choice, form=ChoiceForm, extra=1, can_delete=True
)


def create_poll(request):
    if request.method == "POST":
        question_form = QuestionForm(request.POST)
        choice_forms = [
            ChoiceForm(request.POST, prefix=str(x))
            for x in range(int(request.POST.get("choice_count", 0)))
        ]

        if question_form.is_valid() and all([cf.is_valid() for cf in choice_forms]):
            question = Question.objects.create(
                question_text=question_form.cleaned_data["question_text"],
                pub_date=timezone.now(),
            )
            for cf in choice_forms:
                Choice.objects.create(
                    question=question, choice_text=cf.cleaned_data["choice_text"]
                )
            return redirect("polls:index")
    else:
        question_form = QuestionForm()
        choice_forms = [ChoiceForm(prefix="0")]

    return render(
        request,
        "polls/create.html",
        {"question_form": question_form, "choice_forms": choice_forms},
    )


def update_poll(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        formset = ChoiceFormSet(request.POST, instance=question)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect("polls:detail", pk=question.id)
    else:
        form = QuestionForm(instance=question)
        formset = ChoiceFormSet(instance=question)
    return render(
        request,
        "polls/update.html",
        {"form": form, "formset": formset, "question": question},
    )


def delete_poll(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        question.delete()
        return redirect("polls:index")
    return render(request, "polls/delete.html", {"question": question})
