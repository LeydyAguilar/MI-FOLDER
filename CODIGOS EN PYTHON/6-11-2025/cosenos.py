from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

def inicializar():
    glClearColor(0.1, 0.1, 0.1, 1.0)  # Fondo gris oscuro 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-3.3, 3.3, -3.3, 3.3)  # Definimos el área visible

def dibujar_texto(x, y, texto, r=1.0, g=1.0, b=1.0):
    """Función para dibujar texto en pantalla"""
    glColor3f(r, g, b)
    glRasterPos2f(x, y)
    for ch in texto:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(ch))

def dibujar_ecuacion():
    glClear(GL_COLOR_BUFFER_BIT)

    # Dibujar ejes X e Y
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(-3.0, 0.0)
    glVertex2f(3.0, 0.0)
    glVertex2f(0.0, -3.0)
    glVertex2f(0.0, 3.0)
    glEnd()

    # Marcas y valores del eje X
    for i in range(-3, 4):
        glBegin(GL_LINES)
        glVertex2f(i, -0.05)
        glVertex2f(i, 0.05)
        glEnd()
        if i != 0:
            dibujar_texto(i - 0.1, -0.3, str(i))

    # Marcas y valores del eje Y
    for j in range(-3, 4):
        glBegin(GL_LINES)
        glVertex2f(-0.05, j)
        glVertex2f(0.05, j)
        glEnd()
        if j != 0:
            dibujar_texto(0.1, j - 0.1, str(j))

    # Letras de los ejes
    dibujar_texto(3.1, -0.2, "X", 1.0, 0.8, 0.2)
    dibujar_texto(-0.2, 3.1, "Y", 1.0, 0.8, 0.2)
    dibujar_texto(0.15, -0.3, "O", 1.0, 1.0, 1.0)

    # Dibujar y = sin(x)
    glColor3f(0.2, 0.8, 1.0)  # Azul celeste
    glBegin(GL_LINE_STRIP)
    for x in np.linspace(-3.0, 3.0, 400):
        y = np.sin(x)
        glVertex2f(x, y)
    glEnd()
    dibujar_texto(1.8, np.sin(1.8) + 0.2, "y = sin(x)", 0.2, 0.8, 1.0)

    # Dibujar y = cos(x)
    glColor3f(1.0, 0.4, 0.2)  # Naranja
    glBegin(GL_LINE_STRIP)
    for x in np.linspace(-3.0, 3.0, 400):
        y = np.cos(x)
        glVertex2f(x, y)
    glEnd()
    dibujar_texto(1.8, np.cos(1.8) - 0.5, "y = cos(x)", 1.0, 0.4, 0.2)

    # Letras de cuadrantes
    dibujar_texto(1.5, 1.8, "I", 1.0, 0.6, 0.2)
    dibujar_texto(-2.5, 1.8, "II", 1.0, 0.6, 0.2)
    dibujar_texto(-2.5, -2.0, "III", 1.0, 0.6, 0.2)
    dibujar_texto(1.8, -2.0, "IV", 1.0, 0.6, 0.2)

    # Título
    dibujar_texto(-1.2, 3.2, "Funciones Trigonométricas: y = sin(x), y = cos(x)", 0.9, 1.0, 0.6)

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Funciones seno y coseno - OpenGL (Leydy)")
    inicializar()
    glutDisplayFunc(dibujar_ecuacion)
    glutMainLoop()

if __name__ == "__main__":
    main()
