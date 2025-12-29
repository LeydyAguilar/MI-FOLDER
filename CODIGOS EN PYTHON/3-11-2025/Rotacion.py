from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

angulo = 0.0
posx = 0.0
posy = 0.0

def init():
    glClearColor(0.1, 0.1, 0.1, 1.0)  # Fondo gris oscuro
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # 🔹 Límites más amplios para notar la traslación
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)

def display():
    global angulo, posx, posy
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Aplicar traslación y rotación
    glTranslatef(posx, posy, 0.0)
    glRotatef(angulo, 0.0, 0.0, 1.0)

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 0.5)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.5, -0.5)
    glEnd()

    glFlush()

def Keyboard(key, x, y):
    global posx, posy
    paso = 0.05  

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
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Traslacion visible - PyOpenGL")
    init()
    glutDisplayFunc(display)
    glutSpecialFunc(Keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()


    
