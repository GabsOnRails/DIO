const canvas = document.getElementById('rouletteCanvas');
const ctx = canvas.getContext('2d');

const radius = 200;
const ballRadius = 10;
let rouletteAngle = 0;
let rouletteSpeed = 0;
let ballAngle = 0;
let ballSpeed = 0;
let isSpinning = false;

canvas.width = 400;
canvas.height = 400;

function drawRoulette() {
    ctx.save();
    ctx.translate(canvas.width / 2, canvas.height / 2);
    ctx.rotate(rouletteAngle);

    for (let i = 0; i < 12; i++) {
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.arc(0, 0, radius, (i * Math.PI) / 6, ((i + 1) * Math.PI) / 6);
        ctx.fillStyle = i % 2 === 0 ? 'pink' : 'white';
        ctx.fill();
        ctx.stroke();
    }

    ctx.restore();
}

function drawBall() {
    ctx.save();
    ctx.translate(canvas.width / 2, canvas.height / 2);
    ctx.rotate(ballAngle);
    ctx.beginPath();
    ctx.arc(radius, 0, ballRadius, 0, Math.PI * 2);
    ctx.fillStyle = '#000000';
    ctx.fill();
    ctx.restore();
}

function update() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (isSpinning) {
        ballSpeed *= 0.99;
        rouletteSpeed *= 0.99;
        ballAngle += ballSpeed;
        rouletteAngle += rouletteSpeed;

        if (ballSpeed < 0.01 && rouletteSpeed < 0.01) {
            isSpinning = false;
            ballSpeed = 0;
            rouletteSpeed = 0;
        }
    }

    drawRoulette();
    drawBall();
    requestAnimationFrame(update);
}

function spinRoulette() {
    if (!isSpinning) {
        ballSpeed = Math.random() * 0.1 + 0.1;
        rouletteSpeed = (Math.random() * 0.05 + 0.05) * (Math.random() > 0.5 ? 1 : -1);
        isSpinning = true;
    }
}

canvas.addEventListener('click', spinRoulette);
update();