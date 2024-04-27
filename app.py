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
    return render_template('index.html')

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

@app.route('/discover_your_show')
def discover_your_show():
    return render_template('discover_your_show.html')


@app.route('/discover_your_show/drama')
def explore_drama():
    return render_template('drama.html')

@app.route('/discover_your_show/revival')
def explore_revival():
    return render_template('revival.html')

@app.route('/discover_your_show/musicals')
def explore_musicals():
    return render_template('musicals.html')

@app.route('/discover_your_show/musical/intro')
def explore_musical_intro():
    return render_template('musical_intro.html')

@app.route('/discover_your_show/musicals/hamilton')
def explore_hamilton():
    return render_template('hamilton.html')

@app.route('/discover_your_show/musicals/wicked')
def explore_wicked():
    return render_template('wicked.html')

@app.route('/discover_your_show/musicals/hadestown')
def explore_hadestown():
    return render_template('hadestown.html')

@app.route('/discover_your_show/comedy')
def explore_comedy():
    return render_template('comedy.html')

@app.route('/discover_your_show/comedy/intro')
def explore_comedy_intro():
    return render_template('comedy_intro.html')

@app.route('/discover_your_show/comedy/heathers')
def explore_heathers():
    return render_template('heathers.html')

@app.route('/discover_your_show/comedy/shucked')
def explore_shucked():
    return render_template('shucked.html')

@app.route('/discover_your_show/comedy/book')
def explore_book():
    return render_template('book.html')

@app.route('/discover_your_show/drama/intro')
def explore_drama_intro():
    return render_template('drama_intro.html')

@app.route('/discover_your_show/revival/intro')
def explore_revival_intro():
    return render_template('revival_intro.html')

@app.route('/find_tickets')
def find_tickets():
    return render_template('/find_tickets.html')

@app.route('/discover_your_show/dramas/death_of_a_salesman')
def explore_death():
    return render_template('death.html')

@app.route('/discover_your_show/dramas/an_enemy_of_the_people')
def explore_enemy():
    return render_template('enemy.html')

@app.route('/discover_your_show/dramas/doubt')
def explore_doubt():
    return render_template('doubt.html')

@app.route('/discover_your_show/revivals/the_wiz')
def explore_wiz():
    return render_template('the_wiz.html')

@app.route('/discover_your_show/revivals/my_fair_lady')
def explore_lady():
    return render_template('my_fair_lady.html')

@app.route('/discover_your_show/revivals/cabaret')
def explore_cabaret():
    return render_template('cabaret.html')

if __name__ == '__main__':
    app.run(debug=True)
