**Use Case:** AI Deck Generator
**Actors:** User, GPT
1. User types a prompt in the chat box.
2. The backend calls the OpenAI API with the prompt and a system prompt.
3. The API returns JSON with the slides.
4. The frontend renders the slides with React.
5. If the user doesn't like the result, he clicks "Regenerate".
6. User exports the deck to PowerPoint.
