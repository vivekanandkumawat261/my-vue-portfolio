<template>
    <section class="relative w-full" data-aos="zoom-in-up">
      <NavBar />
      <div class="container">
         <div class="grid-container">
            <div class="text-section">
              <div class="text-content">
                <h1>
                  Hi, I'm <br>
                  <span class="highlight-text">Vivekanand</span>
                </h1>
              </div>
              <p class="description">
                Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quam laborum
                repellat, cum provident illum qui eum architecto mollitia vel, incidunt
                sit inventore accusantium nostrum rerum neque perferendis tempore
                exercitationem consectetur?
              </p>
              <div class="buttons-container">
                <button class="hire-button">
                  <span>Hire Me</span>
                </button>
                <button class="download-button">
                  <div class="download-wrapper">
                    <svg class="download-icon" width="18" height="22" viewBox="0 0 18 22" fill="none"
                      xmlns="http://www.w3.org/2000/svg">
                      <path class="download-arrow" d="M13 9L9 13M9 13L5 9M9 13V1" stroke="#0CA7FF" stroke-width="2"
                        stroke-linecap="round" stroke-linejoin="round"></path>
                      <path
                        d="M1 17V18C1 18.7956 1.31607 19.5587 1.878768 20.1213C2.4129 20.6839 3.20435 21 4 21H14C14.7956 21 15.5587 20.6839 16.1213 20.1213C16.6939 19.5587 17 18.7956 17 18V17"
                        stroke="#0CA7FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                    </svg>
                    <a href="/resume.pdf" download="resume.pdf" class="download-link">Download resume</a>
                  </div>
                </button>
              </div>
            </div>
            <div class="hero-container">
                <figure class="hero-figure">
                  <img src="/for_portfolio_logo.webp" alt="Hero Picture" class="hero-image">
                      <!-- Top-left clipped corner -->
                      <div class="corner-top-left"></div>

                      <!-- Bottom-right clipped corner -->
                      <div class="corner-bottom-right"></div>
                      <figcaption class="card-caption">
                      <div>
                             <h5 class="card-title">FullStack Developer</h5>
                      </div>

  
</figcaption>

                </figure>
            </div>

         </div>
      </div>
      
    </section>
  </template>                                                
  
  <script setup>
  import { defineAsyncComponent } from 'vue';
  
  const NavBar = defineAsyncComponent(() => import('./NavBar.vue'));
  </script>
  
<style scoped>


.card-caption {
  position: absolute;
  bottom: 4rem; /* bottom-16 */
  left: 50%;    /* left-2/4 */
  display: flex;
  width: calc(70% - 5rem);
  transform: translateX(-50%);
  justify-content: space-between;
  border-radius: 0.75rem; /* rounded-xl */
  border: 1px solid var(--color-primary2); /* border-primary2 */
  background-color: rgba(237, 241, 231, 0.75); /* bg-white/75 */
  padding: 0.7rem 1.5rem; /* py-4 px-6 */
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05); /* shadow-lg + shadow-black/5 */
  filter: saturate(2);
  backdrop-filter: blur(4px); /* backdrop-blur-sm */
}

.card-title {
  text-transform: uppercase;
  font-weight: 800;         /* font-semibold */
  /* color: var(--color-primary); text-primary */
  color: rgb(29, 125, 170);
  
  font-size: 1rem;          /* text-base */
}

.corner-top-left {
  position: absolute;
  top: 0;
  left: 0;
  width: 3.5rem;
  height: 3.5rem;
  background-color: white;

  /* Curved inward from top-left */
  clip-path: path("M 100% 0 Q 50% 0, 0 50% Q 0 100%, 0 100% L 100% 100% Z");
}

.corner-bottom-right {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 3.5rem;
  height: 3.5rem;
  background-color: white;

  /* Curved inward from bottom-right */
  clip-path: path("M 0 0 L 100% 0 Q 100% 50%, 50% 100% Q 0 100%, 0 100% Z");
}

  
  .header-container {
    width: 100%;
    background-color: #E3F2FD;
    padding: 2px;
     /* Centers content vertically */
}

 

.container {
  width: 100%;
  padding-left: 20px;
  padding-right: 20px;
  max-width: 1024px;
  margin-left: auto;
  margin-right: auto;
  position: relative;
}

@media (min-width: 640px) {
  .container {
    padding-left: 32px;
    padding-right: 32px;
  }
}

@media (min-width: 768px) {
  .container {
    padding-left: 48px;
    padding-right: 48px;
  }
}

@media (min-width: 1024px) {
  .container {
    padding-left: 32px;
    padding-right: 32px;
    max-width: 1280px;
  }
}

/* Grid Layout */
.grid-container {
  display: grid;
  gap: 40px;
  padding-top: 8px;
  max-width: 640px;
  margin-left: auto;
  margin-right: auto;
  position: relative;
}

@media (min-width: 768px) {
  .grid-container {
    max-width: 768px;
  }
}

@media (min-width: 1024px) {
  .grid-container {
    grid-template-columns: 1fr 1fr;
    max-width: none;
  }
}

@media (min-width: 1280px) {
  .grid-container {
    gap: 56px;
  }
}

/* Text Section */
.text-section {
  padding-top: 24px;
}

@media (min-width: 1024px) {
  .text-section {
    padding-top: 48px;
  }
}

.text-content {
  text-align: center;
}

@media (min-width: 1024px) {
  .text-content {
    text-align: left;
  }
}

/* Heading */
h1 {
  font-size: 2.25rem;
  font-weight: bold;
  padding-top: 16px;
}

@media (min-width: 768px) {
  h1 {
    font-size: 3rem;
  }
}

@media (min-width: 1024px) {
  h1 {
    font-size: 3.75rem;
  }
}

/* Highlighted Text */
.highlight-text {
  color: #0CA7FF;
}

/* Description */
.description {
  color: #6B7280;
  font-size: 1rem;
  padding-top: 32px;
  max-width: 40rem;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
}

@media (min-width: 1024px) {
  .description {
    text-align: left;
    margin-left: 0;
  }
}

/* Buttons */
.buttons-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  padding-top: 36px;
}

@media (min-width: 640px) {
  .buttons-container {
    flex-direction: row;
    justify-content: center;
  }
}

@media (min-width: 1024px) {
  .buttons-container {
    justify-content: flex-start;
  }
}

/* Hire Me Button */
.hire-button {
  padding: 12px 24px;
  border-radius: 999px;
  font-size: 1rem;
  font-weight: bold;
  background-color: #0CA7FF;
  color: white;
  border: none;
  cursor: pointer;
  transition: transform 0.2s ease-in-out;
  width: 100%;
  display: flex;
  justify-content: center;
}

@media (min-width: 640px) {
  .hire-button {
    width: auto;
  }
}

.hire-button:hover {
  transform: scale(1.05);
}

/* Download Button */
.download-button {
  display: flex;
  align-items: center;
  border: 2px solid #0CA7FF;
  padding: 12px 24px;
  border-radius: 999px;
  cursor: pointer;
  transition: transform 0.2s ease-in-out;
  width: 100%;
  justify-content: center;
}

@media (min-width: 640px) {
  .download-button {
    width: auto;
  }
}

.download-button:hover {
  transform: scale(1.05);
}

/* Download Wrapper */
.download-wrapper {
  display: flex;
  align-items: center;
  gap: 8px;
}

/* Download Icon */
.download-icon {
  width: 18px;
  height: 22px;
}

.download-arrow {
  stroke: #0CA7FF;
}

/* Download Link */
.download-link {
  color: #0CA7FF;
  text-decoration: none;
  font-weight: bold;
}

.hero-container {
    height: 100%;
  }

  @media (min-width: 768px) {
    .hero-container {
      display: flex;
    }
  }

  .hero-figure {
    position: relative;
    overflow: hidden;
    border-radius: 0.5rem; /* rounded-lg */
  }

  .hero-image {
    /* width: 100%;
    height: auto;
    object-fit: cover; */
    width: 100%;
    height: 600px; /* or any desired height */
    object-fit: cover;
  }

  .hero-overlay {
    /* You can style this overlay as needed */
  }
  </style>
  