<template>
  <header class="header-container">
    <nav class="nav-bar">
      <!-- Center Logo -->
      <div class="logo">LOGO</div>

      <!-- Right Navigation Links -->
      <ul class="nav-links">
        <li v-for="item in menuItems" :key="item.name">
          <a :href="item.href" class="nav-item">{{ item.name }}</a>
        </li>
      </ul>
    </nav>
  </header>
</template>

<script setup>
import { ref } from 'vue';

const menuItems = ref([
  { name: 'Services', href: '#services' },
  { name: 'Projects', href: '#projects' },
  { name: 'Contact', href: '#contact' }
]);
</script>

<style>
/* Header Container */
.header-container {
  width: 100%;
  background-color: #E3F2FD; /* Light blue background */
  padding: 12px;
}

/* Navigation Bar */
.nav-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: auto;
  padding: 10px;
  border-radius: 10px;
  background-color: white;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
}

/* Logo */
.logo {
  font-size: 24px;
  font-weight: bold;
  color: #0CA7FF; /* Primary blue */
}

/* Navigation Links */
/* .nav-links {
  display: flex;
  gap: 15px;
} */
/* Default (Mobile) */
ul{
  list-style: none;
}
.nav-links {
  display: flex;
  flex-direction: column; /* Stack items vertically by default */
  gap: 20px; /* Equivalent to space-y-5 */
}

/* Medium Screens and Above (md) */
@media (min-width: 768px) {
  .nav-links {
    flex-direction: row; /* Align items in a row */
    gap: 20px; /* Equivalent to space-x-5 */
  }
}


.nav-item {
  text-decoration: none;
  color: black;
  font-size: 18px;
  transition: color 0.3s;
}

.nav-item:hover {
  color: #0CA7FF;
}

/* Optional Left & Right Boxes */
.box {
  width: 120px;
  height: 50px;
  background-color: #E3F2FD;
  border-radius: 10px;
}
</style>
