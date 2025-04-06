<template>
    <section id="services" class="services-section">
      <h2 class="services-title" data-aos="fade-up">My Services</h2>
      <div class="services-grid">
        <div class="service-card-wrapper" data-aos="fade-up" v-for="element in services" :key="element.id">
          <div class="service-card">
            <div class="service-icon-wrapper">
                <span class="service-icon-border">
                   <img :src="element.icon" alt="services" class="service-icon" />
                </span>
            </div>

             

            <div class="service-content">
              <h3 class="service-name">{{ element.name }}</h3>
              <p class="service-description">{{ element.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const services = ref([
    {
      id: 1,
      icon: 'https://img.icons8.com/ios-filled/100/google-code.png',
      name: 'Web Development',
      description:
        'Lorem ipsum dolor sit amet consectetur adipisicing elit. Laudantium ullam repellendus saepe rerum cum soluta dolore esse magnam reiciendis cumque! Fugit molestiae eligendi cumque reprehenderit vel nostrum, itaque at tempore.',
    },
    {
      id: 2,
      icon: 'https://img.icons8.com/ios-filled/100/python.png',
      name: 'Python in DSA',
      description:
    'Master Data Structures and Algorithms using Python. Learn how to solve real-world problems efficiently with in-depth understanding of arrays, linked lists, stacks, queues, trees, graphs, and more. Perfect for coding interviews and competitive programming.',
    },
    {
      id: 3,
      icon: 'https://img.icons8.com/ios-filled/100/windows10-personalization.png',
      name: 'Graphic Design',
      description:
        'Lorem ipsum dolor sit amet consectetur adipisicing elit. Laudantium ullam repellendus saepe rerum cum soluta dolore esse magnam reiciendis cumque! Fugit molestiae eligendi cumque reprehenderit vel nostrum, itaque at tempore.',
    },
    {
     id: 4,
     icon: 'https://img.icons8.com/ios-filled/100/java-coffee-cup-logo.png',
     name: 'Java',
     description:
    'Master Data Structures and Algorithms using Java. Build strong problem-solving skills with deep understanding of arrays, linked lists, stacks, queues, trees, graphs, and more. Perfect for coding interviews, competitive programming, and real-world applications.',
   }

  ]);
  </script>
  
  <style scoped>
  .services-section {
    color: white;
    margin-top: 5rem;
  }
  
  .services-title {
    font-size: 2.25rem;
    font-weight: bold;
    color: black;
    margin-bottom: 1rem;
    text-align: center;
  }
  
  .services-grid {
    padding-top: 2.5rem;
    padding-bottom: 2rem;
    padding-left: 1rem;
    padding-right: 1rem;
    display: grid;
    grid-template-columns: repeat(1, 1fr);
    gap: 1.5rem;
  }
  
  @media (min-width: 640px) {
    .services-grid {
      grid-template-columns: repeat(2, 1fr);
      padding-top: 3rem;
      padding-left: 4rem;
      padding-right: 4rem;
    }
  }
  
  @media (min-width: 768px) {
    .services-grid {
      gap: 2.5rem;
      padding-top: 3rem;
    }
  }
  
  .service-card-wrapper {
    padding: 0.75rem;
    margin-bottom: 1.5rem;
  }
  
  .service-card {
    margin-top: 1.875rem;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    border-radius: 30px;
    background-color: white;
  }

  .service-icon-wrapper {
  margin-top: -7px;
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.service-icon-border {
  height: 60px;
  width: 60px;
  border: 1px solid #111a24;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #fff;
  z-index: 5;
}

.service-icon {
  height: 30px;
  width: 30px;
}

  /* .service-icon-wrapper {
    margin-top: -7px;
    padding: 20px;
    position: relative;
    background-color: #fff;
    border-radius: 50%;
     
  }
  
  .service-icon-border {
    height: 60px;
    width: 60px;
    position: absolute;
    top: 8px;
    left: 8px;
    margin: auto;
    border: 1px solid #111a24;
    border-radius: 50%;
    z-index: 5;
    display: inline-block;
  }
  
  .service-icon {
    height: 35px;
    width: 35px;
    position: relative;
    z-index: 1;
  } */
  
  .service-content {
    padding: 30px;
  }
  
  .service-name {
    text-transform: uppercase;
    font-weight: 600;
    color: #08a4a7;
    font-size: 1rem;
  }
  
  .service-description {
    font-size: 14px;
    line-height: 20px;
    color: #6b7280;
    letter-spacing: 0.03rem;
  }
  </style>
  