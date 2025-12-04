<script setup>
</script>

<template>
  <section class="zainmoni-section">
    <div class="container">
      
      <div class="text-column">
        
        <img src="@/assets/01.png" alt="Zainmoni Logo" class="brand-logo desktop-logo" />
        
        <img src="@/assets/zainmoni2.png" alt="Zainmoni Mobile Logo" class="brand-logo mobile-logo" />
        
        <h2>Dependable Agency Banking</h2>

        <div class="desktop-text">
          <p class="description">
            A cutting-edge solution designed to revolutionize the way businesses process payments 
            at the point of sale. With seamless integration, robust features, and unparalleled reliability, 
            ZainPOS Service empowers businesses to streamline transactions, enhance customer experiences, 
            and drive growth.
          </p>

          <div class="feature-item">
            <span class="check-icon">✔</span>
            <p>
              Zainmoni bridges the gap between merchants and service providers, 
              agents and customers by transforming the complexities that come with payment 
              across multiple channels into a single, secured and convenient channel.
            </p>
          </div>
        </div>

        <div class="tablet-text">
          <div class="feature-item">
            <span class="check-icon">✔</span>
            <p>
              Zainmoni is a unified payment solution that offers a converged platform for 
              Merchants, Mobile money operators, Governments and businesses involved in 
              financial services to perform transactions conveniently, securely at a velocity speed.
            </p>
          </div>

          <div class="feature-item">
            <span class="check-icon">✔</span>
            <p>
              Zainmoni bridges the gap between merchants and service providers, 
              agents and customers by transforming the complexities that come with payment 
              across multiple channels into a single, secured and convenient channel.
            </p>
          </div>
        </div>

        <a href="#" class="btn-primary">
          Learn more about Zainmoni <span class="arrow">→</span>
        </a>
      </div>

      <div class="image-column">
        <img src="@/assets/Group 108.png" alt="Zainmoni Visual" />
      </div>

    </div>
  </section>
</template>

<style scoped>
.zainmoni-section {
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


.brand-logo {
  height: 40px;
  margin-bottom: 20px;
}

.desktop-logo { display: block; }
.mobile-logo { display: none; }


.desktop-text { display: block; }
.tablet-text { display: none; }



@media (max-width: 1024px) {
  .container {
    flex-direction: column-reverse; 
    text-align: center; 
  }
  
  .image-column {
    display: block;
    width: 100%;
    margin-bottom: 30px;
  }

  
  .desktop-logo { display: none; }
  .mobile-logo { 
    display: inline-block; 
    margin: 0 auto 20px auto; 
  }

  
  .desktop-text { display: none; }
  .tablet-text { display: block; }

  .text-column { width: 100%; }

  h2 { 
    font-size: 1.8rem; 
    text-align: center; 
  }

 
  .feature-item {
    text-align: left;
    justify-content: flex-start;
  }
  
  .btn-primary {
    display: block;
    width: 80%;
    text-align: center;
    margin-top: 20px;
  }
}


.text-column, .image-column {
  flex: 1; 
}

.image-column img {
  width: 100%;
  height: auto;
  display: block;
}

h2 {
  font-size: 28px;
  color: #0C1A3D;
  margin-bottom: 20px;
  font-weight: 700;
  letter-spacing:-0.02em;
  line-height:1.28;
}

.description {
  color: #536672;
  line-height: 1.6;
  margin-bottom: 30px;
  font-size: 1rem;
}

.feature-item {
  display: flex;
  gap: 15px;
  margin-bottom: 30px;
  align-items: flex-start;
  text-align: left; 
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
  /* font-weight: bold; */
  flex-shrink: 0; 
}

.feature-item p {
  margin: 0;
  line-height: 1.6;
  color: #536672;
}

.btn-primary {
  display: inline-block;
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
</style>