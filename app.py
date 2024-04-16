from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for quizzes and answers
quizzes = {
    1: {'question': 'Which of the following is NOT a genre of Broadway shows?', 'options': ['Musicals', 'Plays (Drama)', 'Opera', 'Comedy'], 'answer': 'Opera'},
    2: {'question': 'Which Broadway show is known for blending hip-hop, jazz, R&B, and Broadway styles to tell the story of American Founding Father Alexander Hamilton?', 'options': ['Hamilton', 'The Phantom of the Opera', 'Chicago', 'West Side Story'], 'answer': 'Hamilton'},
    3: {'question': 'What are Rush Tickets?', 'options': ['Tickets sold at a discount for students only', 'Tickets offered at the day of the performance, usually when the box office opens, at a discount', 'Expensive tickets for premium seats', 'Tickets you can win through a lottery'], 'answer': 'Tickets offered at the day of the performance, usually when the box office opens, at a discount'},
    4: {'question': 'Which of the following is a primary ticket seller for many Broadway shows?', 'options': ['StubHub', 'SeatGeek', 'Telecharge', 'Vivid Seats'], 'answer': 'Telecharge'},
    5: {'question': 'To avoid overpaying for tickets, what should you check first?', 'options': ['TKTS Booths in Times Square', 'Secondary market platforms like StubHub', 'The box office and official show website', 'Digital lotteries'], 'answer': 'The box office and official show website'}
}

# In-memory storage for user responses
user_responses = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz/<int:quiz_id>', methods=['GET', 'POST'])
def quiz(quiz_id):
    if request.method == 'POST':
        # Save user response
        user_response = request.form.get('option')
        user_responses[quiz_id] = user_response

    quiz = quizzes.get(quiz_id)
    if quiz is None:
        return redirect(url_for('home'))  # Redirect to home if the quiz does not exist

    # Retrieve previous response if it exists
    previous_response = user_responses.get(quiz_id)

    return render_template('quiz.html', quiz=quiz, quiz_id=quiz_id, total_quizzes=len(quizzes), response=previous_response)


@app.route('/results')
def results():
    results_data = []
    for quiz_id, user_response in user_responses.items():
        question_data = quizzes[quiz_id]
        results_data.append({
            'question': question_data['question'],
            'user_answer': user_response,
            'correct_answer': question_data['answer'],
            'is_correct': user_response == question_data['answer']
        })
    return render_template('quiz_results.html', results=results_data)


if __name__ == '__main__':
    app.run(debug=True)
