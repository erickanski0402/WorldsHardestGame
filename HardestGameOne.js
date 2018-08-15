var keyState = {};
window.addEventListener('keydown',function(e){
    keyState[e.keyCode || e.which] = true;
},true);
window.addEventListener('keyup',function(e){
    keyState[e.keyCode || e.which] = false;
},true);

var iteration;
let dots = [];
let player;
let enemyRadius = 20;
var img;

function setup(){
    createCanvas(1100, 500);
    background(100, 140, 200);
    img = loadImage("./squidward_dab.jpg")

    // dots.push(new Enemy(325, 225, true));
    // dots.push(new Enemy(775, 275, false));
    // dots.push(new Enemy(325, 325, true));
    // dots.push(new Enemy(775, 375, false));
    dots.push(new Enemy([[325,225],[775, 225]], 325, 225, 0, [775,225]));
    dots.push(new Enemy([[775,275],[325, 275]], 775, 275, 0, [325,275]));
    dots.push(new Enemy([[325,325],[775, 325]], 325, 325, 0, [775,325]));
    dots.push(new Enemy([[775,375],[325, 375]], 775, 375, 0, [325,375]));

    player = new Player(130, 0, 0, 200, 0, 0, true);

    iteration = 0;
}

function draw(){
    drawStartGoalAreas();
    drawDangerAreas();
    drawMapFrame();
    drawEnemies();
    //counts the number of times draw is updated
    iteration++;

    for(let i = 0; i < 4; i++){
        dots[i].enemyMovement();
    }

    player.alive = checkForEnemyCollisions();
    if(checkForWinCondition()){
        image(img, 325, 10, img.width*2, img.height*2);
    }

    //drawing the player
    if(player.alive){
        player.prevX = player.posX;
        player.prevY = player.posY;

        if(keyState[38]){
            //up arrow
            player.posYC = -2;
        }
        if(keyState[40]){
            //down arrow
            player.posYC = 2;
        }
        if(keyState[37]){
            //left arrow
            player.posXC = -2;
        }
        if(keyState[39]){
            //right arrow
            player.posXC = 2;
        }

        if(checkForWallCollisions(player.posX + player.posXC, player.posY)){
            player.movePlayerX();
        }
        if(checkForWallCollisions(player.posX, player.posY + player.posYC)){
            player.movePlayerY();
        }
    }else{
        player.posX = 130;
        player.posY = 200;
    }

    drawPlayer();
}

function drawStartGoalAreas(){
    noStroke(); //removes lines from shapes
    fill(100, 200, 140);    //pastel green?
    rect(50, 150, 200, 300);    //starting area
    rect(850, 150, 200, 300);   //goal area
}

function drawDangerAreas(){
    fill(200, 200, 200);    //pastel gray?
    rect(250, 400, 100, 50);    //leaving the starting area
    rect(750, 150, 100, 50);    //Leading to the goal area
    rect(300, 200, 500, 200);   //Danger area
}

function drawMapFrame(){
    //  Frame for the map
    stroke(50);
    strokeWeight(4);
    line(50, 150, 50, 450);
    line(50, 450, 350, 450);
    line(350, 450, 350, 400);
    line(350, 400, 800, 400);
    line(800, 400, 800, 200);
    line(800, 200, 850, 200);
    line(850, 200, 850, 450);
    line(850, 450, 1050, 450);
    line(1050, 450, 1050, 150);
    line(1050, 150, 750, 150);
    line(750, 150, 750, 200);
    line(750, 200, 300, 200);
    line(300, 200, 300, 400);
    line(300, 400, 250, 400);
    line(250, 400, 250, 150);
    line(250, 150, 50, 150);
}

function drawEnemies(){
    fill(0, 0, 255);
    strokeWeight(2);

    for(let i = 0; i < 4; i++){
        ellipse(dots[i].posX, dots[i].posY, enemyRadius, enemyRadius);
    }
}

function drawPlayer(){
    strokeWeight(5);
    fill(255, 0, 0);
    rect(player.posX, player.posY, 35, 35);
}

function checkForEnemyCollisions(){
    for(let i = 0; i < 4; i++){
        if(Math.sqrt(Math.pow(dots[i].posX - player.posX, 2) + Math.pow(dots[i].posY - player.posY, 2)) <= 20){
            return false;
        }
    }
    return true;
}

function checkForWinCondition(){
    if(player.posX > 850){
        return true;
    }

    return false;
}

function checkForWallCollisions(tempX, tempY){
    //console.log("X: " + tempX + "   Y: " + tempY);
    if(tempX < 50 || tempX > 1015){
        //player.posX = player.prevX;
        return false;
    }

    if(tempY < 150 || tempY > 415){
        //player.posY = player.prevY;
        return false;
    }

    if((tempX > 215 && tempX < 300) && (tempY > 115 && tempY < 400)){
        //player.posX = player.prevX;
        //player.posY = player.prevY;
        return false;
    }

    if((tempX > 215 && tempX < 750) && (tempY > 115 && tempY < 200)){
        //player.posX = player.prevX;
        //player.posY = player.prevY;
        return false;
    }

    if((tempX > 315 && tempX < 850) && (tempY > 365 && tempY < 450)){
        //player.posX = player.prevX;
        //player.posY = player.prevY;
        return false;
    }

    if((tempX > 765 && tempX < 850) && (tempY > 165 && tempY < 450)){
        //player.posX = player.prevX;
        //player.posY = player.prevY;
        return false;
    }

    return true;
}
