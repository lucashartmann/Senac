class Obj {
    constructor(x, y, width, height, color) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.color = color;
    };

    draw() {
        // canvas.fillStyle = this.color;
        // canvas.fillRect(this.x, this.y, this.width, this.height);

        var img = new Image();
        img.src = this.color;
        canvas.drawImage(img, this.x, this.y, this.width, this.height);
    };

}

class Bee extends Obj {
    dir = 0;

    move() {
        this.x += this.dir;
    };

    frame = 1;
    timer = 0;

    animation() {
        this.timer += 1;
        if (this.timer > 10) {
            this.timer = 0;
            this.frame += 1;
        }
        if (this.frame > 4) {
            this.frame = 1;
        }

        this.color = "assets/bee" + this.frame + ".png";
    }
}

class Spider extends Obj {

    move() {
        this.y += 4;

        if (this.y > 900) {
            this.y = -50;
            this.x = Math.random() * (400 - 0);
        };

    }
}