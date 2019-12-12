let imag; 

function preload(){
  imag = loadImage('xmasw.jpeg');
}


  function setup() {
  createCanvas(1620, 1080);
  imageMode(CENTER);
  noStroke();
  background(255);
  imag.loadPixels();
  frameRate(150);
}

function draw() {
    let x = floor(random(imag.width));
    let y = floor(random(imag.height));
    let pix = imag.get(x, y);
    fill(pix, 100);
    ellipse(x, y, 1, 100);
}
