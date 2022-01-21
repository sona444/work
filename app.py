from flask import Flask, render_template
import pygame
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()

    # Set up the drawing window
screen = pygame.display.set_mode([500, 500])
pygame.quit()
app = Flask(__name__)

# two decorators, same function
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run')
def initi():

    return 'screen'


if __name__ == '__main__':
    app.run(debug=True)