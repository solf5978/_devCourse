import React from 'react';
import ReactDOM from 'react-dom';
import styled from 'styled-components/macro';

function FrequentlyAskedQuestion ( {
    question,
    answer,
}) {
    return (
        <details className="faq">
            <summary>{question}</summary>
            <div className="answer">
                {answer}
            </div>
        </details>
    );
}

ReactDOM.render(
    <FrequentlyAskedQuestion
    question="What does “CSS” stand for?"
    answer="Cool Styling Strategy"
    />
)