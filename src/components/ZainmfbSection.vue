<script setup>
</script>

<template>
  <section class="zainmfb-section">
    <div class="container">
      
      <div class="image-column">
        <img src="@/assets/womanimage.png" alt="Zainmfb Visual" />
      </div>

      <div class="text-column">
        <img src="@/assets/03.png" alt="Zainmfb Logo" class="brand-logo" />
        
        <h2>Secure payment platform for developers by developers</h2>

        <div class="feature-list">
          <div class="feature-item">
            <span class="check-icon">✔</span>
            <p>
              Zainpay is an online and offline digital bank platform for SMEs, 
              Startups and Innovators to quickly launch payment processing products 
              into the Nigerian market.
            </p>
          </div>

          <div class="feature-item">
            <span class="check-icon">✔</span>
            <p>Zainpay support 3 types of settlements T1, T7 and T30.</p>
          </div>
        </div>

        <a href="#" class="btn-primary">
          Learn more about Zainmfb <span class="arrow">→</span>
        </a>
      </div>

    </div>
  </section>
</template>

<style scoped>
.zainmfb-section {
  padding: 80px 20px;
  background-color: white; 
}

.container {
  max-width: 1100px;
  margin: 0 auto;
  display: flex;
  align-items: center; 
  gap: 60px; 
}

.image-column, .text-column {
  flex: 1; 
}

.image-column img {
  width: 100%;
  height: auto;
  display: block;
}

.brand-logo {
  height: 40px;
  margin-bottom: 20px;
}

h2 {
  font-size: 2rem;
  color: #0d1b2a; 
  margin-bottom: 30px;
  font-weight: 700;
}

.feature-item {
  display: flex;
  gap: 15px;
  margin-bottom: 20px;
  align-items: flex-start;
}

.check-icon {
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 24px;
  height: 24px;
  background-color: #e6f9ef; 
  color: #00c853; 
  border-radius: 50%;
  font-size: 14px;
  font-weight: bold;
}

p {
  color: #536672;
  line-height: 1.6;
  font-size: 1rem;
  margin: 0;
}

.btn-primary {
  display: inline-block;
  margin-top: 20px;
  background-color: #0d1b2a;
  color: white;
  padding: 12px 24px;
  text-decoration: none;
  border-radius: 5px;
  font-weight: 500;
  transition: background 0.3s;
}

.btn-primary:hover {
  background-color: #1b2d42;
}


@media (max-width: 1024px) {
  
 
  .zainmfb-section {
    display: none;
  }
  
}
</style>