var canvas = document.getElementById("canvas").getContext("2d");

var bee = new Bee(200, 500, 100, 100, "yellow");
var spider = new Spider(100, 100, 100, 100, "black");

function draw() {
    bee.draw();
    spider.draw();
}

document.addEventListener("keydown", function (event) {
    switch (event.key) {
        case "a":
            bee.dir = -5;
            break;
        case "d":
            bee.dir = 5;
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
    bee.move();
    spider.move();
}

function main() {
    canvas.clearRect(0, 0, 1280, 720);
    update();
    draw();
}

setInterval(main, 10);

