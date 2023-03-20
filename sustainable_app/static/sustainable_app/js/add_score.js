/**To add a score to a DailyGoalStatus add scripts
{% csrf_token %}
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="{% static 'sustainable_app/js/add_score.js' %}"></script>
And then add add_score() to appropriate place in javascript for minigame
*/
function add_score(score,goal) {
    $.ajax({
        type: 'POST',
        url: '/update_daily_goal_status/',
    
        data: {"csrfmiddlewaretoken" : document.querySelector('input[name="csrfmiddlewaretoken"]').value,
        "score": score,
        "goal" : goal},

        success: function() {
            console.log("Success!");
        } 
 
    })
}