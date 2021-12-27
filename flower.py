TOTAL_DEGREES = 360

def setup():
    global displayWidth, displayHeight
    size(displayWidth/2, displayHeight/2)
    noFill()
    stroke(255, 25)
    background(0)


def draw():
    # background(0)
    radius = height / 2
    center_x = width / 2
    center_y = height / 2
    
    global TOTAL_DEGREES
    
    beginShape()
    for i in range(TOTAL_DEGREES):
        noiseFactor = noise(i * 0.02, float(frameCount) / 150)
        x = center_x + radius * cos(radians(i)) * noiseFactor
        y = center_y + radius * sin(radians(i))* noiseFactor
        curveVertex(x, y)
    endShape(CLOSE)