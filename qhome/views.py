from django.shortcuts import render, redirect
from .forms import *
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def index(request):
    quiz = Quiz.objects.all()
    return render(request, "index.html", {'quiz' : quiz})

def quiz(request, myid):
    quiz = Quiz.objects.get(id=myid)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.answer)
        questions.append({str(q): answers})

    ob = {'quiz':quiz, "qs":questions}
    return render(request, "quiz.html", {"ob":ob})

def SubmitAttempt(request, sid):
    user = request.POST
    quests = request.POST.getlist('question')
    questions = []
    answers = []
    score = 0

    for k in quests:
        question = Question.objects.get(question=k)
        questions.append(question)
        ans = request.POST.get(k, "")
        answers.append(ans)

    for q, ans in zip(questions, answers):
        question_answers = Answer.objects.filter(question=q)

        for a in question_answers:
            # print(ans, a.answer, a.correct)
            if ans == a.answer:
                if a.correct:
                    score += 1
    print(score)
    total_questions = len(questions)
    incorrect = total_questions - score
    per = score/total_questions
    per = per * 100
    q = {'score': str(score),
         "total": str(total_questions),
         "wrong": str(incorrect),
         "per": str(per)}

    return render(request, "score.html", q)


def add_quiz(request):
    if request.method=="POST":
        form = QuizForm(data=request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.save()
            alert = True
            return render(request, "adminview.html", {'alert': alert, 'message':'Quiz added successfully'})

    else:
        form=QuizForm()
    return render(request, "add_quiz.html", {'form':form})

def add_question(request):
    questions = Question.objects.filter().order_by('-id')
    if request.method=="POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            alert = True
            return render(request, "adminview.html", {'alert': alert, 'message': 'Question added successfully'})
    else:
        form=QuestionForm()
    return render(request, "add_question.html", {'form':form, 'questions':questions})

def delete_question(request, myid):
    question = Question.objects.get(id=myid)
    if request.method == "POST":
        question.delete()
        return redirect('/add_question')
    return render(request, "delete_question.html", {'question':question})

def add_options(request, myid):
    question = Question.objects.get(id=myid)
    QuestionFormSet = inlineformset_factory(Question, Answer, fields=('answer','correct', 'question'), extra=4)
    if request.method=="POST":
        formset = QuestionFormSet(request.POST, instance=question)
        if formset.is_valid():
            formset.save()
            alert = True
            return render(request, "adminview.html", {'alert': alert, 'message': 'Answers added successfully'})
    else:
        formset=QuestionFormSet(instance=question)
    return render(request, "add_answers.html", {'formset':formset, 'question':question})

def admin_view(request):
    return render(request, "adminview.html")

def choose_question(request):
    questions = Question.objects.filter().order_by('-id')
    if request.method == "POST":
        q_id = request.POST['program']
        return redirect("add_options", myid=int(q_id))
    return render(request, "choosequestion.html", {'questions':questions})

