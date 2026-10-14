/**
 * JERON OPJER - PROFESSIONAL PORTFOLIO INTERACTIVITY SCRIPT
 * Tech Stack: Bootstrap 5.3 + Typed.js + AOS + Canvas Particles + Theme Engine
 */

document.addEventListener('DOMContentLoaded', () => {

  // =========================================================================
  // 1. BOOTSTRAP 5 TOOLTIPS & TOAST INITIALIZATION
  // =========================================================================
  const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
  const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));

  const toastElement = document.getElementById('liveToast');
  const toastText = document.getElementById('toast-text');
  let bsToast = null;
  if (toastElement) {
    bsToast = new bootstrap.Toast(toastElement, { delay: 3500 });
  }

  function showNotification(message) {
    if (toastText && bsToast) {
      toastText.textContent = message;
      bsToast.show();
    }
  }

  // =========================================================================
  // 2. TYPED.JS HERO HEADLINE DYNAMICS
  // =========================================================================
  if (document.getElementById('typed-text')) {
    new Typed('#typed-text', {
      strings: [
        'Digital Solutions.',
        'Responsive Web Systems.',
        'Database Architectures.',
        'Modern Web Interfaces.'
      ],
      typeSpeed: 55,
      backSpeed: 32,
      backDelay: 2200,
      loop: true,
      showCursor: true,
      cursorChar: '|'
    });
  }

  // =========================================================================
  // 3. AOS (ANIMATE ON SCROLL) INITIALIZATION
  // =========================================================================
  if (typeof AOS !== 'undefined') {
    AOS.init({
      once: true,
      duration: 650,
      easing: 'ease-out-cubic',
      offset: 50
    });
  }

  // =========================================================================
  // 4. SUBTLE INTERACTIVE PARTICLES CANVAS
  // =========================================================================
  const canvas = document.getElementById('bg-canvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;

    window.addEventListener('resize', () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    });

    const particles = [];
    const particleCount = Math.min(width > 768 ? 45 : 20, 50);

    for (let i = 0; i < particleCount; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.4,
        vy: (Math.random() - 0.5) * 0.4,
        radius: Math.random() * 1.8 + 0.8
      });
    }

    let mouse = { x: null, y: null };
    window.addEventListener('mousemove', (e) => {
      mouse.x = e.clientX;
      mouse.y = e.clientY;
    });

    window.addEventListener('mouseout', () => {
      mouse.x = null;
      mouse.y = null;
    });

    function animateParticles() {
      ctx.clearRect(0, 0, width, height);

      const isLight = document.body.getAttribute('data-theme') === 'soft-light';
      const dotColor = isLight ? 'rgba(37, 99, 235, 0.25)' : 'rgba(79, 123, 245, 0.35)';
      const lineColor = isLight ? 'rgba(37, 99, 235, 0.08)' : 'rgba(79, 123, 245, 0.12)';

      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];

        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0) p.x = width;
        if (p.x > width) p.x = 0;
        if (p.y < 0) p.y = height;
        if (p.y > height) p.y = 0;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = dotColor;
        ctx.fill();

        // Connect adjacent particles
        for (let j = i + 1; j < particles.length; j++) {
          const p2 = particles[j];
          const dist = Math.hypot(p.x - p2.x, p.y - p2.y);
          if (dist < 110) {
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.strokeStyle = lineColor;
            ctx.lineWidth = 0.75;
            ctx.stroke();
          }
        }
      }

      requestAnimationFrame(animateParticles);
    }

    animateParticles();
  }

  // =========================================================================
  // 5. PROJECT DATA & TAB SWITCHER + BOOTSTRAP MODAL
  // =========================================================================
  const projectsData = [
    {
      title: "GOVSUPPLY CONNECT: A MUNICIPAL PROCUREMENT TRANSPARENCY AND SUPPLY DISTRIBUTION MONITORING SYSTEM",
      badge: "Municipality of E.B. Magalona Portal",
      image: "assets/govsupply_connect.png",
      category: "Municipal Procurement & Supply Chain Monitoring",
      desc: "Official Municipal Government Portal engineered for the Municipality of E.B. Magalona. Deployed for end-to-end procurement transparency, supply distribution tracking, multi-department requisitions, and audit-ready public accountability.",
      tags: ["Web System / PHP", "Procurement Transparency", "Supply Distribution", "Municipal Portal", "MySQL"],
      features: [
        "Secure municipal portal authentication for department heads and supply officers",
        "Real-time tracking of procurement requests, purchase orders, and inventory distribution",
        "Automated transparency logging and reporting aligned with municipal governance standards",
        "Inter-office requisition workflows with audit trails for accountability and public service"
      ]
    },
    {
      title: "Public Project Transparency & Monitoring System",
      badge: "Civic Infrastructure & Public Access",
      image: "assets/project_transparency.png",
      category: "Civic Tech & Public Monitoring Portal",
      desc: "A secure civic transparency and monitoring platform built with Python/Django. Features role-based access for government officials, administrative staff, and public citizens to monitor municipal project milestones, fund disbursements, and physical progress.",
      tags: ["Python / Django", "Project Monitoring", "Role-Based Access (RBAC)", "Civic Transparency", "PostgreSQL"],
      features: [
        "Secure multi-tier access portal (Official, Staff, Admin, and Public Access)",
        "Granular project milestone tracking with physical completion vs. budget utilization curves",
        "Django administrative backend with robust database integrity and audit logs",
        "Public-facing dashboard empowering citizens with open governance insights"
      ]
    }
  ];

  let currentProjectIndex = 0;

  const projectTabBtns = document.querySelectorAll('.proj-tab-btn');
  const projImg = document.getElementById('featured-proj-img');
  const projBadge = document.getElementById('featured-proj-badge');
  const projTitle = document.getElementById('featured-proj-title');
  const projDesc = document.getElementById('featured-proj-desc');
  const projTags = document.getElementById('featured-proj-tags');

  function updateFeaturedProject(index) {
    currentProjectIndex = index;
    const project = projectsData[index];
    if (!project) return;

    projectTabBtns.forEach((btn, i) => {
      if (i === index) {
        btn.classList.add('active');
        btn.setAttribute('aria-selected', 'true');
      } else {
        btn.classList.remove('active');
        btn.setAttribute('aria-selected', 'false');
      }
    });

    if (projImg) {
      projImg.style.opacity = '0.35';
      setTimeout(() => {
        projImg.src = project.image;
        if (projBadge) projBadge.innerHTML = `<i class="bi bi-shield-check me-1"></i> ${project.badge}`;
        if (projTitle) projTitle.textContent = project.title;
        if (projDesc) projDesc.textContent = project.desc;

        if (projTags) {
          projTags.innerHTML = '';
          project.tags.forEach(tag => {
            const span = document.createElement('span');
            span.className = 'tech-tag';
            span.textContent = tag;
            projTags.appendChild(span);
          });
        }

        projImg.style.opacity = '1';
      }, 160);
    }
  }

  projectTabBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      const idx = parseInt(btn.getAttribute('data-index'), 10);
      updateFeaturedProject(idx);
    });
  });

  // Bootstrap Modal Integration
  const modalEl = document.getElementById('bootstrapProjectModal');
  const openModalBtn = document.getElementById('open-modal-btn');
  let bsProjectModal = null;
  if (modalEl && typeof bootstrap !== 'undefined') {
    bsProjectModal = new bootstrap.Modal(modalEl);
  }

  const modalCategory = document.getElementById('modal-category');
  const modalTitle = document.getElementById('modal-title');
  const modalImg = document.getElementById('modal-img');
  const modalDesc = document.getElementById('modal-desc');
  const modalFeatures = document.getElementById('modal-features');

  if (openModalBtn && bsProjectModal) {
    openModalBtn.addEventListener('click', () => {
      const proj = projectsData[currentProjectIndex];
      if (!proj) return;

      if (modalCategory) modalCategory.textContent = proj.category;
      if (modalTitle) modalTitle.textContent = proj.title;
      if (modalImg) modalImg.src = proj.image;
      if (modalDesc) modalDesc.textContent = proj.desc;

      if (modalFeatures) {
        modalFeatures.innerHTML = '';
        proj.features.forEach(feat => {
          const li = document.createElement('li');
          li.textContent = feat;
          modalFeatures.appendChild(li);
        });
      }

      bsProjectModal.show();
    });
  }

  // About & Hobbies Modal initialization
  const aboutModalEl = document.getElementById('aboutBioModal');
  let bsAboutModal = null;
  if (aboutModalEl && typeof bootstrap !== 'undefined') {
    bsAboutModal = new bootstrap.Modal(aboutModalEl);
  }

  const aboutShowcaseEl = document.querySelector('.about-id-showcase');
  if (aboutShowcaseEl && bsAboutModal) {
    aboutShowcaseEl.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        bsAboutModal.show();
      }
    });
  }

  // =========================================================================
  // 6. SKILLS CATEGORY FILTERING (if present)
  // =========================================================================
  const skillFilterBtns = document.querySelectorAll('.skill-tab-btn');
  const skillCards = document.querySelectorAll('.skill-badge-card');

  if (skillFilterBtns.length > 0) {
    skillFilterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        skillFilterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filter = btn.getAttribute('data-filter');

        skillCards.forEach(card => {
          const cat = card.getAttribute('data-category');
          if (filter === 'all' || filter === cat) {
            card.style.display = 'flex';
            card.style.opacity = '1';
          } else {
            card.style.display = 'none';
            card.style.opacity = '0';
          }
        });
      });
    });
  }

  // =========================================================================
  // 7. COLORWAY THEME SWITCHER
  // =========================================================================
  const themeBtns = document.querySelectorAll('.theme-btn');
  const savedTheme = localStorage.getItem('jeron_portfolio_theme') || 'default';

  function applyTheme(themeName) {
    if (themeName === 'default') {
      document.body.removeAttribute('data-theme');
    } else {
      document.body.setAttribute('data-theme', themeName);
    }

    themeBtns.forEach(btn => {
      if (btn.getAttribute('data-colorway') === themeName) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });

    localStorage.setItem('jeron_portfolio_theme', themeName);
  }

  applyTheme(savedTheme);

  themeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const theme = btn.getAttribute('data-colorway');
      applyTheme(theme);
      showNotification(`Switched theme to ${btn.textContent.trim()}`);
    });
  });

  // =========================================================================
  // 8. ONE-CLICK COPY TO CLIPBOARD
  // =========================================================================
  const copyBtns = document.querySelectorAll('.copy-badge-btn');
  copyBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      const textToCopy = btn.getAttribute('data-copy');
      if (textToCopy) {
        navigator.clipboard.writeText(textToCopy).then(() => {
          showNotification(`Copied "${textToCopy}" to clipboard!`);
          const icon = btn.querySelector('i');
          if (icon) {
            icon.className = 'bi bi-check-lg text-success';
            setTimeout(() => {
              icon.className = 'bi bi-clipboard';
            }, 2000);
          }
        }).catch(() => {
          showNotification(`Unable to copy automatically.`);
        });
      }
    });
  });

  // =========================================================================
  // 9. CONTACT FORM INTERACTIVE SUBMISSION
  // =========================================================================
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const nameInput = document.getElementById('contact-name');
      const emailInput = document.getElementById('contact-email');
      const messageInput = document.getElementById('contact-message');

      if (!nameInput.value.trim()) {
        showNotification('Please enter your name.');
        nameInput.focus();
        return;
      }

      if (!emailInput.value.trim() || !emailInput.value.includes('@')) {
        showNotification('Please enter a valid email address.');
        emailInput.focus();
        return;
      }

      if (!messageInput.value.trim()) {
        showNotification('Please enter your message.');
        messageInput.focus();
        return;
      }

      const submitBtn = document.getElementById('submit-btn');
      const origHtml = submitBtn.innerHTML;
      submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span> Sending...';
      submitBtn.disabled = true;

      setTimeout(() => {
        showNotification(`Thank you, ${nameInput.value.trim()}! Your message has been received.`);
        contactForm.reset();
        submitBtn.innerHTML = '<i class="bi bi-check-circle-fill me-1"></i> Sent Successfully!';
        
        setTimeout(() => {
          submitBtn.innerHTML = origHtml;
          submitBtn.disabled = false;
        }, 3000);
      }, 850);
    });
  }

  // =========================================================================
  // 10. MOBILE NAVIGATION DRAWER
  // =========================================================================
  const mobileToggle = document.getElementById('mobile-toggle');
  const mainSidebar = document.getElementById('main-sidebar');

  if (mobileToggle && mainSidebar) {
    mobileToggle.addEventListener('click', () => {
      mainSidebar.classList.toggle('mobile-open');
      const isOpen = mainSidebar.classList.contains('mobile-open');
      mobileToggle.innerHTML = isOpen ? '<i class="bi bi-x-lg"></i>' : '<i class="bi bi-list"></i>';
    });

    const sidebarNavLinks = mainSidebar.querySelectorAll('.nav-item-btn');
    sidebarNavLinks.forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth <= 900) {
          mainSidebar.classList.remove('mobile-open');
          mobileToggle.innerHTML = '<i class="bi bi-list"></i>';
        }
      });
    });
  }

  // =========================================================================
  // 11. SCROLLSPY ACTIVE INDICATOR
  // =========================================================================
  const sections = document.querySelectorAll('section[id], footer[id]');
  const navLinks = document.querySelectorAll('.nav-item-btn');

  function highlightCurrentNav() {
    let scrollY = window.pageYOffset;

    sections.forEach(sec => {
      const sectionHeight = sec.offsetHeight;
      const sectionTop = sec.offsetTop - 120;
      const sectionId = sec.getAttribute('id');

      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        navLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${sectionId}`) {
            link.classList.add('active');
          }
        });
      }
    });
  }

  window.addEventListener('scroll', highlightCurrentNav);
});
