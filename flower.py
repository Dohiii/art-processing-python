s = second()

TOTAL_DEGREES = 360
radius = 360


def setup():
    global displayWidth, displayHeight, radius
    size(displayWidth, displayHeight )
    background(0)
    stroke(0, 25)
    noFill()
    fill(248,248,255)
    rect(18,18,745,1000)

def draw():
    
    
    translate(frameCount, 0)
    # background(0)
    
    center_x = 400
    center_y = height / 2
    global TOTAL_DEGREES, radius, start, s

    beginShape()
    
    noFill()
    for i in range(TOTAL_DEGREES):
        noiseFactor = noise(i * 0.02, float(frameCount) / 150)
        x = center_x + radius * cos(radians(i)) * noiseFactor
        y = center_y + radius * sin(radians(i))* noiseFactor
        curveVertex(x, y)
    endShape(CLOSE)

    radius -= 1
    
    if radius == 0:
        stroke(255, 25)
    
    if radius == -600:
        noLoop()
        
    
    
