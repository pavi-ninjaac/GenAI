import React, { useState } from 'react';
import axios from 'axios';

const AskQuestionZone = () => {
    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
          const response = await axios.post("http://localhost:8000/ask-question/", {"question": question}
          );
          setAnswer(response.data.answer);
        } catch (error) {
          setAnswer("Error generating answer. Please try again.");
        }
    };

    return (
        <>
        <form onSubmit={handleSubmit} className="question-form">
            <div className="form-container">
              <div className="question-container">
                <input
                  type="text"
                  value={question}
                  onChange={(e) => setQuestion(e.target.value)}
                  placeholder="Type your question here..."
                  required
                  className="question-input"
                />
                <button type="submit" className="submit-button">Submit</button>
              </div>
              <textarea
                value={answer}
                placeholder="Generated answer will appear here..."
                readOnly
                className="answer-area"
              />
            </div>
          </form>
        </>
    )
}

export default AskQuestionZone;