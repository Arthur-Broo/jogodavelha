// ===== NAVBAR SCROLL EFFECT =====
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// ===== REVEAL ON SCROLL =====
const revealElements = document.querySelectorAll('.reveal');
const revealOnScroll = () => {
    revealElements.forEach(el => {
        const rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight * 0.85) {
            el.classList.add('active');
        }
    });
};

window.addEventListener('scroll', revealOnScroll);
window.addEventListener('load', revealOnScroll);

// ===== COUNTER ANIMATION =====
const counters = document.querySelectorAll('.stat-number');
const animateCounters = () => {
    counters.forEach(counter => {
        const target = +counter.getAttribute('data-count');
        if (!target) return;
        
        const rect = counter.getBoundingClientRect();
        if (rect.top < window.innerHeight && !counter.classList.contains('animated')) {
            counter.classList.add('animated');
            let count = 0;
            const inc = target / 50;
            const updateCount = () => {
                if (count < target) {
                    count += inc;
                    counter.innerText = Math.ceil(count);
                    setTimeout(updateCount, 20);
                } else {
                    counter.innerText = target;
                }
            };
            updateCount();
        }
    });
};

window.addEventListener('scroll', animateCounters);

// ===== FORM HANDLING =====
const form = document.getElementById('contatoForm');
if (form) {
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const submitBtn = document.getElementById('formSubmit');
        submitBtn.innerHTML = '<span>Enviando...</span>';
        
        // Simulação de envio
        setTimeout(() => {
            submitBtn.innerHTML = '<span>Enviado com Sucesso!</span>';
            submitBtn.style.background = 'var(--primary-gold)';
            submitBtn.style.color = '#000';
            form.reset();
            
            setTimeout(() => {
                submitBtn.innerHTML = '<span>Enviar Solicitação</span>';
                submitBtn.style.background = '';
                submitBtn.style.color = '';
            }, 3000);
        }, 1500);
    });
}

// ===== MOBILE MENU (Simple toggle) =====
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');

if (navToggle) {
    navToggle.addEventListener('click', () => {
        // Implementação básica de menu mobile se necessário
        alert('Menu mobile em desenvolvimento. Navegação via scroll disponível.');
    });
}
