<script setup>
</script>

<template>
  <section class="services-section">
    <div class="container">
      
      <div class="header">
        <h2>Services</h2>
        <p>
          Our services integrate digital technology with technical know-how 
          and tools which we implement into aspects of your business to 
          improve your operations and deliver the best value for you and your customers.
        </p>
      </div>

      <div class="services-grid">
        
        <div class="card">
          <img src="@/assets/laptop.png" alt="Software Development" />
          <div class="card-content">
            <h3>Software Development</h3>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
              Rhoncus, facilisi lectus nunc, felis, elementum eget eu augue magna.
            </p>
            <a href="#" class="btn-learn">Learn more <span class="arrow">→</span></a>
          </div>
        </div>

        <div class="card">
          <img src="@/assets/pos.jpg" alt="Payment Solutions" />
          <div class="card-content">
            <h3>Payment Processing Solutions</h3>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
              Rhoncus, facilisi lectus nunc, felis, elementum eget eu augue magna.
            </p>
            <a href="#" class="btn-learn">Learn more <span class="arrow">→</span></a>
          </div>
        </div>

        <div class="card">
          <img src="@/assets/mobile.jpg" alt="Mobile Development" />
          <div class="card-content">
            <h3>Mobile Application Development</h3>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
              Rhoncus, facilisi lectus nunc, felis, elementum eget eu augue magna.
            </p>
            <a href="#" class="btn-learn">Learn more <span class="arrow">→</span></a>
          </div>
        </div>

      </div>

    </div>
  </section>
</template>

<style scoped>
.services-section {
  padding: 80px 20px;
  background-color: white;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}


.header {
  text-align: center;
  max-width: 800px;
  margin: 0 auto 60px; 
}

.header h2 {
  font-size: 2.5rem;
  color: #0C1A3D;
  margin-bottom: 20px;
  font-weight: 700;
}

.header p {
  color:#536672;
  line-height: 1.6;
}


.services-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr); 
  gap: 30px;
}



@media (max-width: 1024px) {
  .services-grid {
    display: flex;
    overflow-x: auto;
    gap: 20px;
    padding: 10px 5px 30px 5px; 
    
  }

 
  .card {
    min-width: 280px; 
    flex: 0 0 auto;   
   
  }

 
  
}


.card {
  background: white;
  border-radius: 20px;
  overflow: hidden; 
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05); 
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-5px); 
}

.card img {
  width: 100%;
  height: 250px;
  object-fit: cover;
}

.card-content {
  padding: 30px;
}

.card h3 {
  color: #303C5A;
  margin-bottom: 15px;
  font-size: 1.2rem;
}

.card p {
  color: #303C5A;
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 25px;
}

.btn-learn {
  display: inline-flex;
  align-items: center;
  background-color: #0C1A3D;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  transition: background 0.3s;
}

.btn-learn:hover {
  background-color: #1b2d42;
}

.arrow {
  margin-left: 8px;
}



@media (max-width: 768px) {
  
  .cards-grid {
   
    display: flex;
    overflow-x: auto;
    gap: 20px;
    padding-bottom: 20px;
  }

  .image-wrapper {
    display: block; 
    width: 100%;
  }

  .card {
    min-width: 85%; 
    text-align: left; 
    border-bottom: none;
  }

  
  h3 {
    font-size: 1.3rem;
  }
}
</style>