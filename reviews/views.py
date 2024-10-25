from django.shortcuts import render, redirect
from django.http import JsonResponse

def index(request):
    """Main page for rating submission."""
    return render(request, 'reviews/index.html')

def thank_you(request):
    """Thank you page for 4-5 star ratings."""
    return render(request, 'reviews/thank_you.html')

def feedback(request):
    """Feedback page for 1-3 star ratings."""
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback')
        # Save feedback_text to the database or process it as required
        return redirect('index')  # Redirect to home after feedback submission
    return render(request, 'reviews/feedback.html')
