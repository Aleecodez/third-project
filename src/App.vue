<script setup>
import Navbar from './components/Navbar.vue';
import HeroSection from './components/HeroSection.vue';
import MissionSection from './components/MissionSection.vue';
import ZainpaySection from './components/ZainpaySection.vue';
import ZainmoniSection from './components/ZainmoniSection.vue';
import ZainmfbSection from './components/ZainmfbSection.vue'; 
import ZainposSection from './components/ZainposSection.vue';
import ServicesSection from './components/ServicesSection.vue';
import AboutSection from './components/AboutSection.vue';
import FooterSection from './components/FooterSection.vue';
</script>
<!-- // Setup on Dell 7300 -->
<template>
  <div class="app-container">
    <Navbar />

    <div id="home">
      <HeroSection />
      <MissionSection />
    </div>

    <div id="products">
      <ZainpaySection />
      
      <ZainmoniSection />
      
      <ZainmfbSection />

      <ZainposSection />
      
     
      <AboutSection />
    </div>

    <div id="about">
     <ServicesSection />
    </div>

    <div id="contact">
      <FooterSection />
    </div>

  </div>
</template>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Poppins', sans-serif;
  overflow-x: hidden;
  scroll-behavior: smooth; 
}
</style>