// This file contains the JavaScript code that implements the functionality of the roulette game.

const canvas = document.getElementById('rouletteCanvas');
const ctx = canvas.getContext('2d');

canvas.width = 500;
canvas.height = 500;

const colors = ['#FF0000', '#000000', '#00FF00'];
const sections = 36;
const anglePerSection = (2 * Math.PI) / sections;
let currentAngle = 0;
let spinAngle = 0;
let isSpinning = false;

function drawRoulette() {
    for (let i = 0; i < sections; i++) {
        const angle = i * anglePerSection;
        ctx.beginPath();
        ctx.moveTo(canvas.width / 2, canvas.height / 2);
        ctx.arc(canvas.width / 2, canvas.height / 2, 200, angle, angle + anglePerSection);
        ctx.fillStyle = colors[i % colors.length];
        ctx.fill();
        ctx.stroke();
    }
}

function spinRoulette() {
    if (!isSpinning) {
        isSpinning = true;
        spinAngle = Math.random() * 10 + 10; // Random spin speed
        requestAnimationFrame(rotateRoulette);
    }
}

function rotateRoulette() {
    if (spinAngle > 0) {
        currentAngle += spinAngle;
        spinAngle *= 0.99; // Deceleration
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.save();
        ctx.translate(canvas.width / 2, canvas.height / 2);
        ctx.rotate(currentAngle);
        ctx.translate(-canvas.width / 2, -canvas.height / 2);
        drawRoulette();
        ctx.restore();
        requestAnimationFrame(rotateRoulette);
    } else {
        isSpinning = false;
    }
}

document.addEventListener('click', spinRoulette);
drawRoulette();