<script setup>
</script>

<template>
  <section class="zainpay-section">
    <div class="container">
      
      <div class="image-column">
        <img src="@/assets/womanimage.png" alt="Zainpay Features" />
      </div>

      <div class="text-column">
        
        <img src="@/assets/zainpay.png" alt="Zainpay Logo" class="brand-logo desktop-logo" />

        <img src="@/assets/zainpay2.png" alt="Zainpay Mobile Logo" class="brand-logo mobile-logo" />
        
        <h2>Secure payment platform for developers by developers</h2>

        <div class="feature-list">
          <div class="feature-item">
            <span class="check-icon">✔</span>
            <p>
              Zainpay is an online and offline digital bank platform for SMEs, 
              Startups and Innovators to quickly launch payment processing products 
              into the Nigerian market. Zainpay provides virtual accounts and 
              auto-settlements services to business with simple integration features.
            </p>
          </div>

          <div class="feature-item">
            <span class="check-icon">✔</span>
            <p>Zainpay support 3 types of settlements T1, T7 and T30.</p>
          </div>
        </div>

        <a href="#" class="btn-primary">
          Learn more about Zainpay <span class="arrow">→</span>
        </a>
      </div>

    </div>
  </section>
</template>

<style scoped>
.zainpay-section {
  padding: 80px 20px;
  background-color: #F6F8F8; 
}

.container {
  max-width: 1100px;
  margin: 0 auto;
  display: flex;
  align-items: center; 
  gap: 30px; 
}


.brand-logo {
  height: 40px;
  margin-bottom: 20px;
}

.mobile-logo {
  display: none; 
}

.desktop-logo {
  display: block;
}



@media (max-width: 1024px) {
  .container {
    flex-direction: column;
    text-align: center;
  }

  
  .image-column {
    display: block;
    width: 100%;
    margin-bottom: 30px; 
  }

  
  .desktop-logo {
    display: none;
  }

  .mobile-logo {
    display: inline-block; 
    margin: 0 auto 5px auto; 
  }

 
  .text-column {
    width: 100%; 
  }

  h2 {
    font-size: 1.5rem; 
  }
}


.image-column {
  flex: 1; 
}

.image-column img {
  width: 100%;
  height: auto;
  display: block;

}

.text-column {
  flex: 1; 
}

h2 {
  font-size: 28px;
  color: #0C1A3D; 
  margin-bottom: 30px;
  line-height: 128%;
  font-weight: 700;
  letter-spacing: -0.02em;
  text-align: center;
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
  color: #1EBD53; 
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

.arrow {
  margin-left: 8px;
}
</style>