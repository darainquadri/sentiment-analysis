"use strict";

const canvas = document.getElementById('cnv');
const ctx = canvas.getContext('2d');

let particle_properties = { 'color': '#c1ded1', 'line_color': '#dff2ea' };
let particles = [];
let animationId;

function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    cancelAnimationFrame(animationId);
    init();
}

class Particle {
    constructor(x, y, dx, dy, size) {
        this.x = x;
        this.y = y;
        this.dx = dx;
        this.dy = dy;
        this.size = size;
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, 2 * Math.PI, false);
        ctx.fillStyle = particle_properties.color;
        ctx.fill();
    }

    update() {
        this.draw();

        if (this.x > canvas.width || this.x < 0) {
            this.dx = -this.dx;
        }
        if (this.y > canvas.height || this.y < 0) {
            this.dy = -this.dy;
        }

        this.x += this.dx;
        this.y += this.dy;
    }
}

window.addEventListener('resize', resize);

document.addEventListener('DOMContentLoaded', () => {
    resize();
});

function init() {

    particles = [];
    particle_properties.length = (canvas.width * canvas.height) / 7200;

    for (let i = 0; i < particle_properties.length; i++) {
        let size = Math.random() * 4 + 1;
        let x = Math.random() * (canvas.width - size * 2);
        let y = Math.random() * (canvas.height - size * 2);
        let dx = (Math.random() * 3) - 1.5;
        let dy = (Math.random() * 3) - 1.5;
        particles.push(new Particle(x, y, dx, dy, size));
    }

    animate();
}

function animate() {
    animationId = requestAnimationFrame(animate);
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    connect();

    particles.forEach((particle) => {
        particle.update();
    });
}

function connect() {
    for (let i = 0; i < particle_properties.length; i++) {
        let a = particles[i];
        for (let j = 0; j < particle_properties.length; j++) {
            let b = particles[j];
            let dist = Math.sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
            if (dist < canvas.width / 14) {
                ctx.strokeStyle = particle_properties.line_color;
                ctx.lineWidth = 1;
                ctx.beginPath();
                ctx.moveTo(a.x, a.y);
                ctx.lineTo(b.x, b.y);
                ctx.stroke();
            }
        }
    }
}