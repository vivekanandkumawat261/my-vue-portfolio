<template>
   <section class="hero-section">
     <div class="hero-grid">
       <!-- Left Box -->
       <div class="hero-box">
         <!-- Content Here -->
          <Experience/>
       </div>
 
       <!-- Center Box -->
       <div class="hero-box hero-center">
         <MainHero />
         
       </div>
 
       <!-- Right Box -->
       <div class="hero-box">
         <!-- Content Here -->
           <Education/>
       </div>
     </div>
   </section>
 </template>
 
 <script setup>
 import { defineAsyncComponent } from 'vue';
 
 const MainHero = defineAsyncComponent(() => import('./MainHero.vue'));
 const Experience = defineAsyncComponent(() => import('./Experience.vue'));
 const Education = defineAsyncComponent(() => import('./Education.vue'));
 </script>
 
 <style>
 .hero-section {
   position: relative;
   padding: 12px;
   background-color: var(--primary2);
 }
 
 .hero-grid {
   display: grid;
   grid-template-columns: repeat(1, 1fr);
   gap: 16px;
 }
 
 @media (min-width: 768px) {
   .hero-grid {
     grid-template-columns: repeat(2, 1fr);
   }
 }
 
 @media (min-width: 1024px) {
   .hero-grid {
     grid-template-columns: repeat(4, 1fr);
   }
 }
 
 .hero-box {
   border-radius: 24px;
   padding: 20px;
   background-color: white;
   display: flex;
   align-items: center;
   justify-content: center;
 }
 
 .hero-center {
   grid-column: span 2;
 }
 </style>
 