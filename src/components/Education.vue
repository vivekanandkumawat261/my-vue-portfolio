<template>
    <div class="education-container">
      <h2 class="section-heading" data-aos="fade-left">Education</h2>
      <div class="education-list">
        <div
          v-for="element in Education"
          :key="element.id"
          data-aos="fade-left"
          class="education-card"
        >
          <div class="icon-container">
            <img
              src="https://img.icons8.com/ios-glyphs/60/graduation-cap--v1.png"
              alt="graduation"
            />
          </div>
          <div class="details">
            <h3 class="title">{{ element.title }}</h3>
            <p class="school">{{ element.school }}</p>
            <p class="duration">{{ element.duration }}</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue'
  
  const Education = ref([
    {
      id: 1,
      title: 'Software Engineer',
      school: 'Microsoft',
      duration: 'Mar 2013 - Sep 2024',
    },
    {
      id: 2,
      title: 'Bachelor of Engineering',
      school: 'MIT',
      duration: 'Aug 2009 - Jun 2013',
    },
    {
      id: 3,
      title: 'High School',
      school: 'Springfield High',
      duration: '2007 - 2009',
    },
  ])
  </script>
  
  <style scoped>
  .education-container {
    width: 100%;
  }
  
  .section-heading {
    text-align: center;
    font-size: 2.25rem;
    font-weight: bold;
    margin-bottom: 1rem;
  }
  
  .education-list {
    padding-top: 3.5rem;
    padding-bottom: 3.5rem;
    display: flex;
    flex-direction: column;
    gap: 4rem;
  }
  
  .education-card {
    display: flex;
    align-items: center;
    background-color: rgba(255, 255, 255, 0.75);
    border-radius: 0.75rem;
    padding: 1rem;
  }
  
  .icon-container {
    width: 25%;
  }
  
  .details {
    width: 75%;
    padding-left: 1rem;
  }
  
  .title {
    text-transform: uppercase;
    font-weight: 600;
    color: #0ca7ff;
    font-size: 1rem;
  }
  
  .school,
  .duration {
    color: #6b7280;
  }
  </style>
  