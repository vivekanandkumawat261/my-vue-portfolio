<template>
    <section id="projects">
      <h2 class="section-title" data-aos="fade-up">My Projects</h2>
      <div class="projects-grid">
        <div
          data-aos="fade-in"
          v-for="element in projects"
          :key="element.id"
          class="project-card"
        >
          <img :src="element.image" alt="project img" class="project-image" />
          <div class="project-content">
            <span class="project-category">{{ element.category }}</span>
            <h3 class="project-title">{{ element.title }}</h3>
            <p class="project-description">{{ element.description }}</p>
            <div class="project-buttons">
              <button class="hire-button">
                <a :href="element.webURL" target="_blank">Live Preview</a>
              </button>
              <button class="download-button">
                <a :href="element.gitURL" target="_blank" class="code-link">Code Source</a>
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  const projects = ref([
    {
      id: 1,
      image:'/image_1_for_my_wesite.png',
      title: 'Project 1',
      category: 'Web App',
      description: "I designed and developed a fully responsive personal portfolio website using HTML, Tailwind CSS, and Vue.js. The site showcases my professional skills, services, and project work in a clean and modern layout. It includes smooth animations, mobile-first responsiveness, and a dark/light theme toggle. The project also integrates AOS (Animate on Scroll) for subtle animations and a contact form for visitor inquiries. It's optimized for performance and SEO, ensuring fast load times and better visibility on search engines.",
      gitURL: '',
      webURL: ''
    },
    {
      id: 2,
      image:'/image_2_for_my_wesite.png',
      title: 'Project 2',
      category: 'Web App',
      description: "I designed and developed a fully responsive personal portfolio website using HTML, Tailwind CSS, and Vue.js. The site showcases my professional skills, services, and project work in a clean and modern layout. It includes smooth animations, mobile-first responsiveness, and a dark/light theme toggle. The project also integrates AOS (Animate on Scroll) for subtle animations and a contact form for visitor inquiries. It's optimized for performance and SEO, ensuring fast load times and better visibility on search engines.",
      gitURL: '',
      webURL: ''
    },
    {
      id: 3,
      image:'/image_3_for_my_wesite.png',
      title: 'Project 3',
      category: 'Web App',
      description: "I designed and developed a fully responsive personal portfolio website using HTML, Tailwind CSS, and Vue.js. The site showcases my professional skills, services, and project work in a clean and modern layout. It includes smooth animations, mobile-first responsiveness, and a dark/light theme toggle. The project also integrates AOS (Animate on Scroll) for subtle animations and a contact form for visitor inquiries. It's optimized for performance and SEO, ensuring fast load times and better visibility on search engines.",
      gitURL: '',
      webURL: ''
    },
    {
      id: 4,
      image:'/image_4_for_my_wesite.png',
      title: 'Project 4',
      category: 'Web App',
      description: "I designed and developed a fully responsive personal portfolio website using HTML, Tailwind CSS, and Vue.js. The site showcases my professional skills, services, and project work in a clean and modern layout. It includes smooth animations, mobile-first responsiveness, and a dark/light theme toggle. The project also integrates AOS (Animate on Scroll) for subtle animations and a contact form for visitor inquiries. It's optimized for performance and SEO, ensuring fast load times and better visibility on search engines.",
      gitURL: '',
      webURL: ''
    }
  ]);
  </script>
  
  <style scoped>
  /* Section Title */
  .section-title {
    font-size: 2.25rem;
    font-weight: bold;
    color: black;
    margin-bottom: 1rem;
    text-align: center;
  }
  
  /* Projects Grid */
  .projects-grid {
    padding: 2rem 1rem;
    display: grid;
    grid-template-columns: 1fr;
    gap: 3rem;
    margin-top: 2.5rem;
  }
  
  /* Project Card */
  .project-card {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background-color: white;
    border-radius: 1.5rem;
    margin-bottom: 1.5rem;
  }
  
  @media (min-width: 1109px) {
    .project-card {
      flex-direction: row;
    }
  }
  
  /* Project Image */
  .project-image {
    width: 75%;
    object-fit: cover;
    border-radius: 1rem;
  }
  
  /* Project Content */
  .project-content {
    display: flex;
    width: 22%;
    height: 57%;
    align-items: center;
    flex-direction: column;
    justify-content: center;
    padding: 1.5rem;
    gap: 3rem;
  }
  
  /* Project Category Badge */
  .project-category {
    background-color: #ffd700;
    width: 5rem;
    text-align: center;
    padding: 0.5rem;
    border-radius: 1.5rem;
    color: black;
    font-weight: bold;
  }
  
  /* Title */
  .project-title {
    text-transform: uppercase;
    font-weight: 600;
    color: #007bff;
    font-size: 1rem;
  }
  
  /* Description */
  .project-description {
    font-size: 0.875rem;
    line-height: 1.25rem;
    color: #6b7280;
    letter-spacing: 0.03rem;
  }
  
  /* Buttons */
  .project-buttons {
    display: flex;
    gap: 1rem;
    padding-top: 2rem;
    flex-direction: column;
    align-items: center;
  }
  
  @media (min-width: 640px) {
    .project-buttons {  
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
    }
  
    @media (min-width: 1024px) {
      .project-buttons {
        margin-left: 0;
      }
    }
  }
  
  /* Button Styles */
  .hire-button,
  .download-button {
    background-color: #007bff;
    border: none;
    color: white;
    padding: 0.6rem 1.2rem;
    font-size: 0.875rem;
    border-radius: 0.5rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .hire-button:hover,
  .download-button:hover {
    background-color: #0056b3;
  }
  
  .code-link {
    padding-left: 0.5rem;
    color: #007bff;
    text-decoration: none;
  }
  </style>
  