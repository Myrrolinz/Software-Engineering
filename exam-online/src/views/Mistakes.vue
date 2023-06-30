<template>
  <div>
    <h1>错题本</h1>
    <ul>
      <li v-for="question in questions" :key="question.id">
        <h2>{{ question.title }}</h2>
        <p>{{ question.content }}</p>
        <ol>
          <li v-for="option in question.options" :key="option">
            {{ option }}
          </li>
        </ol>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      questions: [
        {
          id: 1,
          title: '英语单项选择题1',
          content: 'What is the capital of the United States?',
          options: ['New York', 'Washington D.C.', 'Los Angeles', 'Chicago']
        },
        {
          id: 2,
          title: '英语单项选择题2',
          content: 'Who wrote the novel "Pride and Prejudice"?',
          options: ['Jane Austen', 'Emily Bronte', 'Charlotte Bronte', 'Virginia Woolf']
        },
        {
          id: 3,
          title: '英语单项选择题3',
          content: 'What is the largest ocean in the world?',
          options: ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean']
        },
        {
          id: 4,
          title: '英语单项选择题4',
          content: 'What is the smallest planet in our solar system?',
          options: ['Mercury', 'Venus', 'Earth', 'Mars']
        },
        {
          id: 5,
          title: '英语单项选择题5',
          content: 'What is the chemical symbol for gold?',
          options: ['Gd', 'Au', 'Ag', 'Fe']
        },
        {
          id: 6,
          title: '英语单项选择题6',
          content: 'What is the highest mountain in the world?',
          options: ['Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse']
        },
        {
          id: 7,
          title: '英语单项选择题7',
          content: 'Who painted the Mona Lisa?',
          options: ['Leonardo da Vinci', 'Michelangelo', 'Raphael', 'Donatello']
        },
        {
          id: 8,
          title: '英语单项选择题8',
          content: 'What is the capital of Australia?',
          options: ['Sydney', 'Melbourne', 'Canberra', 'Brisbane']
        },
        {
          id: 9,
          title: '英语单项选择题9',
          content: "What is the world's longest river?",
          options: ['Nile River', 'Amazon River', '<EUGPSCoordinates> River', '<EUGPSCoordinates> River']
        },
        {
          id: 10,
          title: "英语单项选择题10",
          content:"Which planet is known as the Red Planet?",
           options:['Mars','Jupiter','Saturn','Venus']
         }
      ]
    };
  }
};
</script>
