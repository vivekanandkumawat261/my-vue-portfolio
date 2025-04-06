<template>
  <div class="container">
    <Suspense>
      <!-- Wrap components in Suspense to handle loading -->
      <template #default>
        <div class="hero-section">
            <HeroSection />
             <Skills/>
             <Services/>
             <Projects/>
        </div>
      </template>
      <template #fallback>
        <div class="loading-container">
          <LoadingSpinner />
        </div>
      </template>
    </Suspense>
  </div>
</template>

<script setup>
import { defineAsyncComponent } from 'vue';
import LoadingSpinner from './components/LoadingSpinner.vue';
import AOS from 'aos';
import 'aos/dist/aos.css';
AOS.init({duration:2000 , delay:200});
// Lazy-load component (only loaded when needed)
const HeroSection = defineAsyncComponent(() =>
  import('./components/HeroSection.vue')
);
const Skills = defineAsyncComponent(()=>import('./components/Skills.vue'))
const Services = defineAsyncComponent(()=>import('./components/Services.vue'))
const Projects = defineAsyncComponent(()=>import('./components/Projects.vue'))
 
</script>

<style scoped>
.container {
  min-height: 100vh; /* Tailwind min-h-screen */
}

.hero-section {
  background-color: var(--primary2, #69d6da); /* Tailwind bg-primary2 (custom color variable) */
}

.loading-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
</style>
