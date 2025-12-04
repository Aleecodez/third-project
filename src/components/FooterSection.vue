<script setup>

const currentYear = new Date().getFullYear();
</script>

<template>
  <footer class="footer">
    <div class="container">
      
      <div class="col brand-col">
        <img src="@/assets/Betastack Logo 1.png" alt="Betastack Logo" class="footer-logo" />
        
        <div class="certifications">
          <img src="@/assets/ndpr.png" alt="NDPR Compliant" class="cert-logo" />
          <img src="@/assets/pcidss.png" alt="PCI DSS" class="cert-logo" />
        </div>
      </div>

      <div class="col">
        <h3>Products</h3>
        <ul>
          <li><a href="#">Zainpay</a></li>
          <li><a href="#">Zainmoni</a></li>
        </ul>
      </div>

      <div class="col">
        <h3>Contact Us</h3>
        <p>
          Plot 320 Aminu Babandi <br />
          Street, Railway Quarters <br />
          Kano State.
        </p>
        <p class="contact-links">
          <a href="mailto:hello@betastack.ng">hello@betastack.ng</a> <br />
          <a href="tel:+2349024655848">+234 902 465 5848</a>
        </p>
      </div>

      <div class="col connect-col">
        <h3>Connect with us</h3>
        
        <div class="social-icons">
          <a href="#"><img src="@/assets/facebook.png" alt="Facebook" /></a>
          <a href="#"><img src="@/assets/twitter.png" alt="Twitter" /></a>
          <a href="#"><img src="@/assets/linkedin.png" alt="LinkedIn" /></a>
          <a href="#"><img src="@/assets/message.png" alt="Email" /></a>
        </div>

        <p class="copyright">© {{ currentYear }} Betastack</p>
      </div>

    </div>
  </footer>
</template>

<style scoped>
.footer {
  background-color: #051024; 
  color: white;
  padding: 60px 20px;
  font-size: 0.9rem;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr 1fr; 
  gap: 40px;
}


@media (max-width: 1024px) {
  .container {
    grid-template-columns: 1fr; 
    gap: 40px;
  }
}


h3 {
  font-size: 1rem;
  margin-bottom: 20px;
  font-weight: 600;
  color: #e0e0e0;
}


ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  margin-bottom: 10px;
}

a {
  text-decoration: none;
  color: #b0b8c4;
  transition: color 0.3s;
}

a:hover {
  color: white;
}

p {
  color: #b0b8c4;
  line-height: 1.6;
  margin-bottom: 15px;
}


.footer-logo {
  height: 35px;
  margin-bottom: 30px;
  display: block;
}

.certifications {
  display: flex;
  gap: 20px;
  align-items: center;
}

.cert-logo {
  height: 30px; 
  width: auto;
}


.social-icons {
  display: flex;
  gap: 15px;
  margin-bottom: 40px;
}

.social-icons img {
  width: 18px;
  height: auto;
  
  filter: brightness(0) invert(1);
  opacity: 0.8;
  transition: opacity 0.3s;
}

.social-icons img:hover {
  opacity: 1;
}

.copyright {
  font-size: 0.8rem;
  color: #667;
  margin-top: auto; 
}
</style>