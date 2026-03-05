class Obj {
    constructor(x, y, width, height, color) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.color = color;
    }

    draw() {
        // canvas.fillStyle = this.color;
        // canvas.fillRect(this.x, this.y, this.width, this.height);
        var img = new Image();
        img.src = this.color;
        canvas.drawImage(img, this.x, this.y, this.width, this.height);
    }
}

class Bee extends Obj {
    dir = 0;

    move() {
        this.x += this.dir;
    }
}

class Spider extends Obj {
    move() {
        this.y += 2;

        if (this.y > 900) {
            this.y = -50;
            this.x = Math.random() * (400 - 0);
        }
    }
}