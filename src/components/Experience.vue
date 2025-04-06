<template>
    <section>
      <h2 class="section-heading" data-aos="fade-right">Experience</h2>
      <div class="experience-section">
        <div class="experience-list">
          <div
            v-for="element in Experience"
            :key="element.id"
            data-aos="fade-right"
            class="experience-card"
          >
            <div class="icon-container">
              <img src="https://img.icons8.com/ios-filled/100/lawyer.png" alt="lawyer" />
            </div>
            <div class="details">
              <h3 class="title">{{ element.title }}</h3>
              <p class="company">{{ element.company }}</p>
              <p class="duration">{{ element.duration }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const Experience = ref([
    {
      id: 1,
      title: 'Software Engineer',
      company: 'Microsoft',
      duration: 'Mar 2023 - Sep 2024',
    },
    {
      id: 2,
      title: 'Backend Developer',
      company: 'Google',
      duration: 'Jan 2022 - Feb 2023',
    },
    {
      id: 3,
      title: 'Intern',
      company: 'Amazon',
      duration: 'Jun 2021 - Dec 2021',
    },
  ])
  </script>
  <style scoped>
  /* Experience.css */

.section-heading {
  text-align: center;
  font-size: 2.25rem; /* Tailwind's text-4xl */
  font-weight: 700;   /* Tailwind's font-bold */
  margin-bottom: 1rem; /* Tailwind's mb-4 */
}

.experience-section {
  padding-top: 3.5rem; /* Tailwind's py-14 */
  padding-bottom: 3.5rem;
}

.experience-list {
  display: flex;
  flex-direction: column;
  gap: 4rem; /* Tailwind's space-y-16 */
}

.experience-card {
  display: flex;
  align-items: center;
  background-color: rgba(255, 255, 255, 0.75);
  border-radius: 0.75rem; /* Tailwind's rounded-xl */
  padding: 1rem; /* Tailwind's p-4 */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05); /* Tailwind's shadow-md */
}

.icon-container {
  width: 25%; /* Tailwind's w-1/4 */
  padding: 20px;
}

.details {
  width: 75%; /* Tailwind's w-3/4 */
  padding-left: 1rem; /* Tailwind's pl-4 */
}

.title {
  text-transform: uppercase;
  font-weight: 600;
  color: #0CA7FF; /* Primary blue */
  font-size: 1rem;
}

.company,
.duration {
  color: #6B7280; /* Tailwind's text-gray-500 */
}

  </style>
  