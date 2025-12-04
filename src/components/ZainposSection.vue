<script setup>
</script>

<template>
  <section class="zainpos-section">
    <div class="container">
      
      <div class="text-column">
        <img src="@/assets/01.png" alt="Zainpos Logo" class="brand-logo" />
        
        <p class="description">
          Zainpay disbursement, ZainBatch is a platform for making payments to individuals or entities. 
          This includes salary payments, loan distributions, grants, dividends, and other financial dispositions.
          <br><br>
          This is an advanced solution designed to simplify and automate the process of disbursing funds securely and efficiently.
        </p>

        <div class="feature-item">
          <span class="check-icon">✔</span>
          <p>
            Zainmoni bridges the gap between merchants and service providers, 
            agents and customers by transforming the complexities that come with payment across multiple channels into a single,secured and convenient channel
          </p>
        </div>

        <a href="#" class="btn-primary">
          Learn more about Zainmoni <span class="arrow">→</span>
        </a>
      </div>

      <div class="image-column">
        <img src="@/assets/Group 108.png" alt="Zainpos Terminal Visual" />
      </div>

    </div>
  </section>
</template>

<style scoped>

.zainpos-section {
  padding: 80px 20px;
  background-color: white;
  color:#536672;
}

.container {
  max-width: 1100px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  gap: 60px;
}

p {
  color: #536672;
  line-height: 1.6;
  font-size: 1rem;
  margin: 0;
}

.text-column, .image-column {
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

.description {
  color: #666;
  line-height: 1.6;
  margin-bottom: 20px;
  font-size: 1rem;
}

.feature-item {
  display: flex;
  gap: 15px;
  margin-bottom: 30px;
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

.btn-primary {
  display: inline-block;
  background-color: #0C1A3D;
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
  
  
  .zainpos-section {
    display: none;
  }

}
</style>