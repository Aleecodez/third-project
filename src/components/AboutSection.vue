<script setup>
</script>

<template>
  <section class="about-section">
    <div class="container">
      
      <div class="header">
        <h2>About Us</h2>
        <p class="subtitle">
          To bridge the gap between informal and formal sectors <br />
          of businesses with excellent financial services.
        </p>
      </div>

      <div class="cards-grid">
        
        <div class="card">
          <div class="image-wrapper">
            <img src="@/assets/image.png" alt="Who We Are" />
          </div>
          <h3>Who We Are</h3>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Rhoncus, facilisi lectus nunc, felis, elementum eget eu 
            augue magna. Dapibus a imperdiet nam sed.
          </p>
        </div>

        <div class="card">
          <div class="image-wrapper">
            <img src="@/assets/image2.png" alt="What We Do" />
          </div>
          <h3>What We Do</h3>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Rhoncus, facilisi lectus nunc, felis, elementum eget eu 
            augue magna. Dapibus a imperdiet nam sed.
          </p>
        </div>

      </div>

    </div>
  </section>
</template>

<style scoped>
.about-section {
  background-color: #0B1839; 
  color: white;
  padding: 80px 20px;
  border-radius: 42px; 
  margin: 20px 70px; 
}

.container {
  max-width: 1000px;
  margin: 0 auto;
}

.header {
  text-align: center;
  margin-bottom: 60px;
}

.header h2 {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 15px;
}

.header .subtitle {
  font-size: 1rem;
  line-height: 1.5;
  color: #d1d5db; 
}

.cards-grid {
  display: grid;
  grid-template-columns: 1fr 1fr; 
  gap: 40px;
}

.image-wrapper img {
  width: 100%;
  height: 250px; 
  object-fit: cover; 
  border-radius: 10px;
  margin-bottom: 20px;
}

h3 {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 10px;
}

p {
  font-size: 0.9rem;
  color: #FFFFFFD9; 
  line-height: 1.6;
}


@media (max-width: 768px) {
  
  .about-section {
   
    margin: 20px 0; 
    
   
    padding-left: 0;
    padding-right: 0;
    
    
    border-radius: 0; 
  }

  
  .header {
    padding: 0 20px;
  }

  .cards-grid {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    
    
    gap: 0; 
    
    padding-bottom: 20px; 
  }

  .card {
    
    min-width: 100%;
    
    scroll-snap-align: center;
    
   
    padding: 0 20px; 
  }

  .image-wrapper img {
   
    width: 100%;
    
    border-radius: 10px; 
  }
  
  
  .cards-grid::-webkit-scrollbar {
    display: none;
  }
}
</style>