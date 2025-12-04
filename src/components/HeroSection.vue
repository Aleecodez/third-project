<script setup>
</script>

<template>
  <section class="hero-container">
    
    <img src="@/assets/frame 4.png" alt="Betastack Hero Banner" class="hero-desktop" />
    
    <img src="@/assets/hero-tablet.png" alt="Hero Tablet" class="hero-tablet" />

    <img src="@/assets/frame 16.png" alt="Hero Mobile" class="hero-mobile" />

  </section>
</template>

<style scoped>
.hero-container {
  width: 100%;
  line-height: 0; 
  
}


.hero-desktop {
  width: 100%;
  height: auto; 
  display: block; 
}

.hero-tablet {
  display: none; 
}

.hero-mobile {
  display: none; 
}



@media (max-width: 1024px) {

 
  .hero-container {
    margin-bottom: 0;
  }

  
  .hero-desktop {
    display: none;
  }

  
  .hero-tablet {
    display: block;
    width: 100%;
    height: auto;
  }

  
  .hero-mobile {
    display: none;
  }
}



@media (max-width: 768px) {

  
  .hero-tablet {
    display: none;
  }

 
  .hero-mobile {
    display: block;
    width: 100%;
    height: auto;
  }
}
</style>