from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

def inicializar():
    glClearColor(0.1, 0.1, 0.1, 1.0)  # Fondo gris oscuro 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-3.3, 3.3, -3.3, 3.3)

def dibujar_ecuacion():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Color blanco
    glBegin(GL_LINES)
    glVertex2f(-3.0, 0.0)
    glVertex2f(3.0, 0.0)
    glVertex2f(0.0, -3.0)
    glVertex2f(0.0, 3.0)
    glEnd()

    glColor3f(0.2, 0.8, 1.0)  # Azul celeste
    glBegin(GL_LINE_STRIP)
    for x in np.linspace(-3.0, 3.0, 400):
        y = np.sin(x)
        glVertex2f(x, y)
    glEnd()

    glColor3f(1.0, 0.4, 0.2)  # Naranja
    glBegin(GL_LINE_STRIP)
    for x in np.linspace(-3.0, 3.0, 400):
        y = np.cos(x)
        glVertex2f(x, y)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Funciones seno y coseno - OpenGL")
    inicializar()
    glutDisplayFunc(dibujar_ecuacion)
    glutMainLoop()

if __name__ == "__main__":
    main()


