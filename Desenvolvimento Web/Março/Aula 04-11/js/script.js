var canvas = document.getElementById("canvas").getContext("2d");

var bee = new Bee(200, 500, 100, 100, "assets/bee1.png");
var spider = new Spider(100, 100, 100, 100, "assets/spider1.png");
var bg = new Bg(0, 0, 500, 900, "assets/bg.png");
var bg2 = new Bg(0, -900, 500, 900, "assets/bg.png");

var flower = new Flower(0, 0, 50, 50, "assets/flower1.png");

var text_points = new Text();
var text_lifes = new Text();
var gameover = new Text();
var play = true;

function draw() {
    bg.draw();
    bg2.draw();

    if (play) {
        bee.draw();
        spider.draw();
        flower.draw();

        text_points.draw(bee.pts, 240, 100, "white");
        text_lifes.draw(bee.lifes, 40, 100, "red");
    } else {
        gameover.draw("Game Over", 150, 450, "white");
    }
};

document.addEventListener("keydown", function (event) {
    switch (event.key) {
        case "a":
            bee.dir = -5;
            break;
        case "d":
            bee.dir = + 5;
            break;
    }
});

document.addEventListener("keyup", function (event) {
    switch (event.key) {
        case "a":
        case "d":
            bee.dir = 0;
            break;
    }
});

function update() {
    bg.move(3, 900, 0);
    bg2.move(3, 0, -900);

    if (play) {
        bee.move();
        bee.animation("bee", 4);
        spider.move();
        spider.animation("spider", 4);
        flower.move();
        flower.animation("flower", 2);
        collides();
        gameOver();
    }

};

function gameOver() {
    if (bee.lifes <= 0) {
        play = false;
        return true;
    }
    return false;
}

function collides() {
    if (bee.collide(spider)) {
        spider.respawn();
        bee.lifes -= 1;
        text_lifes.text = bee.lifes;
    } else if (bee.collide(flower)) {
        flower.respawn();
        bee.pts += 1;
        text_points.text = bee.pts;
    }
}

function main() {
    canvas.clearRect(0, 0, 500, 900);
    update();
    draw();
};

setInterval(main, 10);