async function generateQuestions() {

    const role = document.getElementById('role').value;

    const response = await fetch('/generate_questions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ role })
    });

    const data = await response.json();

    const container = document.getElementById('questions-container');

    container.innerHTML = '';

    data.questions.forEach((question, index) => {

        container.innerHTML += `

        <div class="question-box">
            <h3>${question}</h3>

            <textarea id="answer-${index}" placeholder="Write your answer..."></textarea>

            <button onclick="submitAnswer(${index}, '${question}')">
                Submit Answer
            </button>

            <div id="feedback-${index}" class="feedback"></div>
        </div>
        `;
    });

} // <-- THIS BRACKET WAS MISSING


async function submitAnswer(index, question) {

    const answer = document.getElementById(`answer-${index}`).value;

    const response = await fetch('/evaluate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            question,
            answer
        })
    });

    const data = await response.json();

    document.getElementById(`feedback-${index}`).innerHTML = `
        <strong>Score:</strong> ${data.feedback.score}<br>
        <strong>Feedback:</strong> ${data.feedback.message}
    `;
}