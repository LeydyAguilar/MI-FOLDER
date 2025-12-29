from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

escala = 1.0  
angulo = 0.0
posx = 0.0
posy = 0.0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-2.0, 2.0, -2.0, 2.0)
    glMatrixMode(GL_MODELVIEW)

def display():
    global escala, angulo, posx, posy
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Aplicar transformaciones
    glTranslatef(posx, posy, 0.0)
    glRotatef(angulo, 0.0, 0.0, 1.0)
    glScalef(escala, escala, 1.0)


    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 0.5)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.5, -0.5)
    glEnd()

    glFlush()

def keyboard(key, x, y):
    global escala, angulo
    if key == b'+':
        escala += 0.1
    elif key == b'-':
        escala -= 0.1
    elif key == b'l':  
        angulo -= 10
    elif key == b'a': 
        angulo += 10
    glutPostRedisplay()

def special_keys(key, x, y):
    global posx, posy
    paso = 0.1
    if key == GLUT_KEY_UP:
        posy += paso
    elif key == GLUT_KEY_DOWN:
        posy -= paso
    elif key == GLUT_KEY_LEFT:
        posx -= paso
    elif key == GLUT_KEY_RIGHT:
        posx += paso
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Transformaciones 2D - Escala, Traslacion y Rotacion")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_keys)
    glutMainLoop()

if __name__ == "__main__":
    main()

