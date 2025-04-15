import { initHeroSection } from './HeroSection.js';
import { initAboutSection } from './AboutSection.js';
import { initProductSection } from './ProductSection.js';

document.addEventListener('DOMContentLoaded', () => {
  initHeroSection();
  initAboutSection();
  initProductSection();
});
import * as THREE from 'three';

export function initHeroSection() {
  const heroElement = document.getElementById('hero');
  const canvas = document.createElement('canvas');
  heroElement.appendChild(canvas);

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true });
  renderer.setSize(window.innerWidth, window.innerHeight);

  const geometry = new THREE.BoxGeometry();
  const material = new THREE.MeshBasicMaterial({ color: 0x8cbf88, wireframe: true });
  const cube = new THREE.Mesh(geometry, material);
  scene.add(cube);

  camera.position.z = 5;

  function animate() {
    requestAnimationFrame(animate);
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;
    renderer.render(scene, camera);
  }

  animate();
}
export function initAboutSection() {
    const aboutSection = document.getElementById('about');
    aboutSection.innerHTML = `
      <h2>Our Story</h2>
      <p>Experience nature through pure, organic skincare...</p>
    `;
  
    window.addEventListener('scroll', () => {
      const sectionPos = aboutSection.getBoundingClientRect().top;
      const scrollPos = window.innerHeight / 1.5;
  
      if (sectionPos < scrollPos) {
        aboutSection.style.opacity = 1;
        aboutSection.style.transform = 'translateY(0)';
      } else {
        aboutSection.style.opacity = 0;
        aboutSection.style.transform = 'translateY(50px)';
      }
    });
  }
  import * as THREE from 'three';

export function initProductSection() {
  const productsElement = document.getElementById('products');
  productsElement.innerHTML = '<h2>Our Products</h2>';

  const canvas = document.createElement('canvas');
  productsElement.appendChild(canvas);

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true });
  renderer.setSize(window.innerWidth / 2, window.innerHeight / 2);

  // Product geometry and material setup
  const geometry = new THREE.SphereGeometry(1, 32, 32);
  const material = new THREE.MeshBasicMaterial({ color: 0x333399 });
  const productSphere = new THREE.Mesh(geometry, material);
  scene.add(productSphere);

  camera.position.z = 3;

  function animateProduct() {
    requestAnimationFrame(animateProduct);
    productSphere.rotation.y += 0.01;
    renderer.render(scene, camera);
  }

  animateProduct();
}
