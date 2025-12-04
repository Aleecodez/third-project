<script>
export default {
  name: "Navbar",
  data() {
    return {
      isMenuOpen: false, 
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen; 

      
      if (this.isMenuOpen) {
        document.body.style.overflow = 'hidden';
      } else {
        document.body.style.overflow = 'auto';
      }
    }
  }
};
</script>

<template>
  <nav class="navbar">
    
    <div class="logo">
      <img src="@/assets/betastack.png" alt="Betastack Logo" />
    </div>

    <ul class="nav-links desktop-view">
      <li><a href="#home">Home</a></li>
      <li><a href="#products">Products</a></li>
      <li><a href="#about">About Us</a></li>
      <li><a href="#contact">Contact Us</a></li>
    </ul>

    <div class="social-box desktop-view">
      <a href="#"><img src="@/assets/facebook.png" alt="FB" /></a>
      <a href="#"><img src="@/assets/twitter.png" alt="TW" /></a>
      <a href="#"><img src="@/assets/linkedin.png" alt="LI" /></a>
      <a href="#"><img src="@/assets/message.png" alt="EM" /></a>
    </div>

    <button class="hamburger-btn mobile-view" @click="toggleMenu">
      <span class="bar"></span>
      <span class="bar"></span>
      <span class="bar"></span>
    </button>

    <div v-if="isMenuOpen" class="mobile-menu-overlay">
      
      <div class="mobile-header">
        <img src="@/assets/betastack.png" class="mobile-logo" alt="Logo" />
        
        <button class="close-btn" @click="toggleMenu">✕</button>
      </div>

      <ul class="mobile-links">
        <li><a href="#home" @click="toggleMenu">Home</a></li>
        <li><a href="#products" @click="toggleMenu">Products</a></li>
        <li><a href="#about" @click="toggleMenu">About Us</a></li>
        <li><a href="#products" @click="toggleMenu">Services</a></li>
        <li><a href="#contact" @click="toggleMenu">Contact Us</a></li>
      </ul>

      <div class="mobile-socials">
        <a href="#"><img src="@/assets/facebook.png" alt="FB" /></a>
        <a href="#"><img src="@/assets/twitter.png" alt="TW" /></a>
        <a href="#"><img src="@/assets/linkedin.png" alt="LI" /></a>
        <a href="#"><img src="@/assets/message.png" alt="EM" /></a>
      </div>

    </div>

  </nav>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 80px;
  background-color: white;
  position: relative; 
}


.logo {
  display: flex;
  align-items: center;
  padding-left: 5%;
  z-index: 101; 
}
.logo img {
  height: 40px;
  width: auto;
}


.desktop-view {
  display: flex;
}
.mobile-view {
  display: none; 
}


.nav-links {
  list-style: none;
  gap: 40px;
  margin: 0;
  padding: 0;
}
.nav-links a {
  text-decoration: none;
  color: #0C1A3D;
  font-weight: 700;
  font-size: 16px;
  font-family: sans-serif;
  transition: color 0.3s;
}
.nav-links a:hover {
  color: #0056b3;
}


.social-box {
  background-color: #0d1b2a;
  height: 100%;
  display: flex;
  align-items: center;
  padding: 0 40px;
  gap: 15px;
}


@media (max-width: 1024px) {
  
  
  .desktop-view {
    display: none;
  }

  
  .mobile-view {
    display: block;
  }

  
  .hamburger-btn {
    background: none;
    border: none;
    cursor: pointer;
    padding-right: 5%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 6px;
    height: 100%;
  }
  .hamburger-btn .bar {
    width: 30px;
    height: 3px;
    background-color: #0d1b2a; 
    border-radius: 2px;
  }

  
  .mobile-menu-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background-color: #051024; 
    z-index: 1000;
    padding: 20px;
    display: flex;
    flex-direction: column;
  }

 
  .mobile-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 60px;
  }

  .mobile-logo {
    height: 30px;
    filter: brightness(0) invert(1); 
  }

  .close-btn {
    background: none;
    border: none;
    color: white;
    font-size: 30px;
    cursor: pointer;
  }

 
  .mobile-links {
    list-style: none;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 30px;
  }

  .mobile-links a {
    color: white;
    font-size: 1.2rem;
    font-weight: 500;
    text-decoration: none;
  }

  
  .mobile-socials {
    margin-top: auto; 
    display: flex;
    gap: 20px;
    padding-bottom: 40px;
  }

  .mobile-socials img {
    width: 20px;
    filter: brightness(0) invert(1); 
  }
}
</style>