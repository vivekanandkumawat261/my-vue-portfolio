<template>
    <section>
      <div class="skills-wrapper">
        <div data-aos="zoom-in-up" v-for="element in skills" :key="element.id">
          <figure class="skill-icon-container">
            <img :src="element.icon" alt="skill icon" class="skill-icon" />
          </figure>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const skills = ref([
    {
      id: 1,
      icon: 'https://img.icons8.com/plasticine/100/087ea4/react.png',
    },
    {
      id: 2,
      icon: 'https://img.icons8.com/fluency/48/087ea4/vuejs.png',
    },
    {
      id: 3,
      icon: 'https://img.icons8.com/fluency/48/angularjs.png',
    },
    {
      id: 4,
      icon: 'https://img.icons8.com/color/48/tailwindcss.png',
    },
    {
      id: 5,
      icon: 'https://img.icons8.com/fluency/48/figma.png',
    },
    {
      id: 6,
      icon: 'https://img.icons8.com/fluency/48/html-5.png',
    },
    {
      id: 7,
      icon: 'https://img.icons8.com/fluency/48/javascript--v1.png',
    },
  ]);
  </script>
  
  <style scoped>
  .skills-wrapper {
    width: 100%;
    background-color: white;
    border-top: 4px solid #08a4a7; /* Primary2 equivalent */
    border-bottom: 5px solid #08a4a7;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    /* padding: 0.5rem; */
    gap: 0;
  }
  
  .skill-icon-container {
    width: 5rem;
    height: 5rem;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 9999px;
    margin-left: 0.5rem;
    margin-top: 0.5rem;
    position: relative;
  }
  
  .skill-icon {
    width: 2.5rem;
    height: 3rem;
    position: absolute;
    z-index: 10;
  }
  </style>
  